#!/bin/bash


# written by Channabasav Angadi

# Install Java Development Kit (JDK)
sudo apt update
sudo apt install default-jdk -y

# Install Apache Spark
SPARK_VERSION="3.1.2"
HADOOP_VERSION="3.2"
wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
sudo mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark
rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Install Python and PIP
sudo apt install python3 python3-pip -y

# Install required Python packages
pip3 install pyspark
pip3 install spark-redshift

# Install PostgreSQL driver for Redshift
sudo apt install libpq-dev -y

# Install JDBC driver for Redshift
wget https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/1.2.45.1069/RedshiftJDBC42-1.2.45.1069.jar
sudo mv RedshiftJDBC42-1.2.45.1069.jar /opt/spark/jars/

echo "Packages installation completed."
