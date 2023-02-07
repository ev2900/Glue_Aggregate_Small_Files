# Glue Aggregate Small Parquet Files

When storing data in S3 it is important to consider the size of the files you store in S3. Parquet file have an ideal file size of 500 MB - 1 GB. Storing data in many small files can decrease the performance of data processing tools accessing data in S3. 

This repository provides a Glue script 
