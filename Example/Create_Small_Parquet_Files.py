import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from datetime import datetime
from pyspark.sql.functions import *
from pyspark.sql.types import * 

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Create a sample data frame
data = [
        ("1", "Chris", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("2", "Will", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("3", "Emma", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("4", "John", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("5", "Eric", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("6", "Adam", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
]

schema = StructType([
        StructField("id", StringType(), False),
        StructField("name", StringType(), False), 
        StructField("create_date", StringType(), False),             
        StructField("last_update_time", TimestampType(), False)
])

sampleDF = spark.createDataFrame(data=data,schema=schema)

sampleDF = sampleDF.coalesce(6)

# Write the sample data frame to S3 as 6 seperate small parquet files
sampleDF.write.parquet("s3://<s3_bucket_name>/sampleDF/prefix1/", mode = "overwrite")

job.commit()