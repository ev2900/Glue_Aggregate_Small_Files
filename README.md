# Glue Aggregate Small Parquet Files

When storing data in S3 it is important to consider the size of files you store in S3. Parquet files have an ideal file size of 512 MB - 1 GB. Storing data in many small files can decrease the performance of data processing tools ie. Spark. 

This repository provides a PySpark script [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py)  that can consolidate small parquet files in an S3 prefix into larger parquet files.
