# Create Small Files in S3
If you need example small files in an S3 bucket follow these instructions. You may want to generate small files to test the Glue script in this repository that can aggregate small parquet files ie [Aggregate_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Aggregate_Small_Parquet_Files.py).

## How to create small parquet files

1. Upload the [Create_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Example/Create_Small_Parquet_Files.py) file to a S3 bucket

2. Run the CloudFormation stack below to create a Glue job that will generate small parquet files

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=create-small-files-glue&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/Glue_Job_Deployment_Create_Small_Parquet_Files.yaml)

As you follow the prompts to deploy the CloudFormation stack ensure that you fill out the *S3GlueScriptLocation* parameter with the S3 URI of the [Create_Small_Parquet_Files.py](https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/cloud_formation/Example/Create_Small_Parquet_Files.py) that you uploaded to a S3 bucket in the first step

<img width="800" alt="cat_indicies_1" src="https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Example/README/cloudformation-parameter.png">

3. Update and run the Glue job

The CloudFormation stack deployed a Glue job named *Create_Small_Parquet_Files*. Navigate to the [Glue console](https://us-east-1.console.aws.amazon.com/gluestudio/home). Select *ETL jobs* and then the *Create_Small_Parquet_Files*

Update *<s3_bucket_name>* with the name of the S3 bucket the Glue job will create the small files in

<img width="600" alt="cat_indicies_1" src="https://github.com/ev2900/Glue_Aggregate_Small_Files/blob/main/Example/README/update-glue-script.png">

After you update the S3 bucket name, save and run the Glue job. When the Glue job finishes you will have small parquet files in the specified S3 location
