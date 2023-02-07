# Spark Aggregate Small Parquet Files

When storing data in S3 it is important to consider the size of files you store in S3. Parquet files have an ideal file size of 500 MB - 1 GB. Storing data in many small files can decrease the performance of data processing tools accessing data in S3. 

This repository provides several an example PySpark script designed to be run in AWS Glue. A description of each script is provided below

1. 
