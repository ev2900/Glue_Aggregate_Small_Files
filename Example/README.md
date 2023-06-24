# Create Small Files in S3
If you need example small files in an S3 bucket follow these instructions. You may want to generate small files to test the Glue script in this repository that can aggregate small parquet files ie [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Aggregate_Small_Parquet_Files.py).

## How to create small parquet files

1. Upload the [Create_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Example/Create_Small_Parquet_Files.py) file to a S3 bucket

2. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=agg-small-file-glue-job&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/Aggregate_Small_Parquet_File_Glue_Job_Deployment.yaml)
