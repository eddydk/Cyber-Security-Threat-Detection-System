import boto3
import pandas as pd
import io

# Setup S3 client
s3_client = boto3.client('s3')

# Download the file into memory
response = s3_client.get_object(Bucket='cybersecurity-ml-data1', Key='raw-data/UNSW_NB15_training-set.csv')

# Read it into pandas
df = pd.read_csv(io.BytesIO(response['Body'].read()))

# Explore
print(df.shape)
print(df.columns)
print(df.head())
print(df['label'].value_counts())


