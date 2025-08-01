import sagemaker
from sagemaker import get_execution_role

# Create SageMaker session and define bucket
session = sagemaker.Session()
bucket = 'cybersecurity-ml-data1'  # Replace with your actual S3 bucket name
processed_prefix = 'processed-data'      # Folder in S3 to store processed files

# Save preprocessed data locally
df.to_csv('preprocessed_data.csv', index=False)

# Upload to S3 inside the 'processed-data/' folder
s3_path = session.upload_data(
    path='preprocessed_data.csv',
    bucket=bucket,
    key_prefix=processed_prefix
)

print(f"Preprocessed data uploaded to: {s3_path}")