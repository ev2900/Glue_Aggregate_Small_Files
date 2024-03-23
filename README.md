# Glue Aggregate Small Parquet Files

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-22-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-2163-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-567-green">

When storing data in S3 it is important to consider the size of files you store in S3. Parquet files have an ideal file size of 512 MB - 1 GB. Storing data in many small files can decrease the performance of data processing tools ie. Spark.

This repository provides a PySpark script [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py)  that can consolidate small parquet files in an S3 prefix into larger parquet files.

## How to run the Glue job to aggregate small parquet files

*Note* if you are testing the [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py) and need to generate small parquet files as test data. You can follow the instructions in the [Example](https://github.com/ev2900/Glue_Aggregate_Small_Files/tree/main/Example) folder to create small file test data.

1. Upload  the [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py) file to a S3 bucket

2. Run the CloudFormation stack below to create a Glue job that will generate small parquet files

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=aggregate-small-files-glue&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/Aggregate_Small_Parquet_File_Glue_Job_Deployment.yaml)

As you follow the prompts to deploy the CloudFormation stack ensure that you fill out the *S3GlueScriptLocation* parameter with the S3 URI of the [Create_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Example/Create_Small_Parquet_Files.py) that you uploaded to a S3 bucket in the first step

<img width="800" alt="cat_indicies_1" src="https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/README/cloudformation-parameter.png">

3. Update and run the Glue job

The CloudFormation stack deployed a Glue job named *Aggregate_Small_Parquet_Files*. Navigate to the [Glue console](https://us-east-1.console.aws.amazon.com/gluestudio/home). Select *ETL jobs* and then the *Aggregate_Small_Parquet_Files*

Update <s3_bucket_name> with the name of the S3 bucket with the small files that need to be aggregated
Update <path_to_prefix> with the path to the prefix of a single partition with small files to aggregate in it
Optional: update the *total_prefix_size* to the desired target size of the aggregated parquet file(s)

<img width="800" alt="cat_indicies_1" src="https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/README/configuration_information.png">

After you update the S3 bucket name and the path to the prefix, save and run the Glue job. When the Glue job finishes you will have small parquet files in the specified S3 location will have been aggregated.
