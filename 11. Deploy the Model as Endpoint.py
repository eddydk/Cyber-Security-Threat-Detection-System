import boto3
from sagemaker import image_uris

sagemaker_client = boto3.client("sagemaker")
region = "us-east-1"
bucket_name = "cybersecurity-ml-data1"
model_artifact = f"s3://cybersecurity-ml-data1/xgboost-model-output/sagemaker-xgboost-2025-05-21-08-48-39-127/output/model.tar.gz"
model_name = "cybersecurity-threat-xgboost"

# Get XGBoost image URI
image_uri = image_uris.retrieve("xgboost", region=region, version="1.3-1")

# Use actual IAM Role ARN
execution_role = "arn:aws:iam::252366102382:role/SageMakerCybersecurityRole"

# Register the model
response = sagemaker_client.create_model(
    ModelName=model_name,
    PrimaryContainer={
        "Image": image_uri,
        "ModelDataUrl": model_artifact
    },
    ExecutionRoleArn=execution_role
)

print(f"Model {model_name} registered successfully in SageMaker!")