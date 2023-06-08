# written by Channabasav Angadi

## here i used dummy (means not used any credentials because of security issue in the production it can be replaced)

import pandas as pd
import psycopg2

# Step 1: Load the movie dataset
movie_data = pd.read_csv('movie_dataset.csv')  # please Replace 'movie_dataset.csv' with the actual dataset file here i used dummy one for example purpose
# Step 2: Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='your-database-host',
    port='your-database-port',
    database='your-database-name',
    user='your-database-username',
    password='your-database-password'
)

# Step 3: Create the movie data warehouse table  i used columns as per my convenience
create_table_query = '''
    CREATE TABLE movie_recommendation (
        user_id INT,
        movie_id INT,
        rating FLOAT,
        completed BOOLEAN
    )
'''
with conn.cursor() as cursor:
    cursor.execute(create_table_query)
conn.commit()

# Step 4: Insert movie data into the data warehouse table
insert_query = '''
    INSERT INTO movie_recommendation (user_id, movie_id, rating, completed)
    VALUES (%s, %s, %s, %s)
'''

with conn.cursor() as cursor:
    for _, row in movie_data.iterrows():
        cursor.execute(insert_query, (row['user_id'], row['movie_id'], row['rating'], row['completed']))
conn.commit()

# Step 5: Perform data analysis and exploration
# here you can run any analysis on data ware house tables
# i left it blank 

# Step 6: Build the recommendation system
# here you can build any recoommendation using any ML librabry
# i left it blank

# Step 7: Close the database connection
conn.close()
