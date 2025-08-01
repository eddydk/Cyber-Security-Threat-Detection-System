import pandas as pd
import boto3
import sagemaker

# Set up session and bucket
session = sagemaker.Session()
bucket = 'cybersecurity-ml-data1'
processed_prefix = 'processed-data'

# Download preprocessed data from S3
s3 = boto3.client('s3')
file_name = 'preprocessed_data.csv'
s3.download_file(bucket, f'{processed_prefix}/{file_name}', file_name)

# Load into pandas
df = pd.read_csv(file_name)
df.head()