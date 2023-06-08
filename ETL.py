# written by Channabasav Angadi

# i have written bash script (ETL.sh) to install all required package at on shot 

## here i used dummy (means not used any credentials because of security issue in the production it can be replaced)

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Song Data ETL") \
    .getOrCreate()

# Configure your AWS credentials and Redshift connection according yout environment here i used dummy
aws_access_key_id = "your-aws-access-key"
aws_secret_access_key = "your-aws-secret-access-key"
redshift_url = "jdbc:redshift://your-redshift-cluster-endpoint:5439/your-database"
redshift_table = "your_table"
redshift_username = "your-username"
redshift_password = "your-password"

# Read song data from S3 into DataFrame

# Update with your S3 bucket and song data folder here i used dummy

s3_song_data_path = "s3://your-bucket/song-data-folder"  
df_song_data = spark.read.json(s3_song_data_path)

# Perform necessary transformations on song data
# ...

# Write song data to Redshift with all the data which we fetched
df_song_data.write \
    .format("com.databricks.spark.redshift") \
    .option("url", redshift_url) \
    .option("dbtable", redshift_table) \
    .option("tempdir", "s3://your-bucket/temp-folder") \
    .option("aws_iam_role", "your-redshift-iam-role") \
    .option("extracopyoptions", "COMPUPDATE OFF") \
    .option("forward_spark_s3_credentials", "true") \
    .option("user", redshift_username) \
    .option("password", redshift_password) \
    .mode("overwrite") \
    .save()

# above i written overwrite which means that if the target table already exists, it will be truncated and the new data will be written. 


# Read log data from S3 into DataFrame
s3_log_data_path = "s3://your-bucket/log-data-folder"  # Update with your S3 bucket and log data folder here i used dummy
df_log_data = spark.read.json(s3_log_data_path)

# Perform necessary transformations on log data
# ...

# Write log data to Redshift which we fetched
df_log_data.write \
    .format("com.databricks.spark.redshift") \
    .option("url", redshift_url) \
    .option("dbtable", redshift_table) \
    .option("tempdir", "s3://your-bucket/temp-folder") \
    .option("aws_iam_role", "your-redshift-iam-role") \
    .option("extracopyoptions", "COMPUPDATE OFF") \
    .option("forward_spark_s3_credentials", "true") \
    .option("user", redshift_username) \
    .option("password", redshift_password) \
    .mode("append") \
    .save()

# above i written append which means add the data to an existing table because we need all logs for future refrence
