import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

logger = glueContext.get_logger()

# Configuration information
s3_bucket_name = 'fdfsd4534' # Do not include trailing / or s3://
prefix = 'sampleDF' # Do not include trailing / 
target_file_size_in_bytes = 536870912  # 536,870,912 (.5 GB) - 1,073,741,824 (1 GB) is recomended

# Validate configuration information
s3_bucket_name = s3_bucket_name.rstrip()
prefix = prefix.rstrip()

# Calculate the target number of files
import boto3
import math

session = boto3.Session()
s3 = session.resource('s3')
my_bucket = s3.Bucket(s3_bucket_name)

total_prefix_size = 0

for my_bucket_object in my_bucket.objects.filter(Prefix=prefix + '/'):
    object = s3.Object(s3_bucket_name, my_bucket_object.key)
    total_prefix_size = total_prefix_size + object.content_length
    # Optional - log each file + size in the prefix
    # logger.info(my_bucket_object.key + ": " + str(object.content_length) + " bytes")

logger.info('Total prefix size of ' + prefix + '/: ' + str(total_prefix_size) + ' bytes')

target_number_of_files =  math.ceil(total_prefix_size / target_file_size_in_bytes)

logger.info('Target number of files: ' + str(target_number_of_files))

# Read the prefix and coalesce the dataframe to the target number of file
prefix_df = spark.read.parquet('s3://' + s3_bucket_name + '/' + prefix + '/*')
prefix_df = prefix_df.coalesce(target_number_of_files)

# Write data to a new temp prefix
prefix_df.write.parquet('s3://' + s3_bucket_name + '/' + prefix + '_temp/', mode = "overwrite")

logger.info('Coalesced data to prefix: ' + prefix + '_temp/')

# Delete the prefix
for my_bucket_object in my_bucket.objects.filter(Prefix=prefix + '/'):
    my_bucket_object.delete()

logger.info('Deleted prefix: ' + prefix + '/')

# 'Rename' the temp prefix
for my_bucket_object in my_bucket.objects.filter(Prefix=prefix + '_temp/'):
    old_source = {'Bucket': s3_bucket_name, 'Key': my_bucket_object.key}
    new_key = my_bucket_object.key.replace(prefix + '_temp/', prefix + '/', 1)
    new_obj = my_bucket.Object(new_key)
    new_obj.copy(old_source)

logger.info('Copied prefix: ' + prefix + '_temp/ to prefix' + prefix + '/')
    
for my_bucket_object in my_bucket.objects.filter(Prefix=prefix + '_temp/'):
    my_bucket_object.delete()

logger.info('Deleted prefix: ' + prefix + '_temp/')