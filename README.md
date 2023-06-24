# Glue Aggregate Small Parquet Files

When storing data in S3 it is important to consider the size of files you store in S3. Parquet files have an ideal file size of 512 MB - 1 GB. Storing data in many small files can decrease the performance of data processing tools ie. Spark. 

This repository provides a PySpark script [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py)  that can consolidate small parquet files in an S3 prefix into larger parquet files.

## How to run the Glue job to aggregate small parquet files

1. Upload  the [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Aggregate_Small_Parquet_Files.py) file to a S3 bucket

2. Run the CloudFormation stack below to create a Glue job that will generate small parquet files

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=aggregate-small-files-glue&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/Aggregate_Small_Parquet_File_Glue_Job_Deployment.yaml)

As you follow the prompts to deploy the CloudFormation stack ensure that you fill out the *S3GlueScriptLocation* parameter with the S3 URI of the [Create_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Example/Create_Small_Parquet_Files.py) that you uploaded to a S3 bucket in the first step

<img width="800" alt="cat_indicies_1" src="https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Example/README/cloudformation-parameter.png">
