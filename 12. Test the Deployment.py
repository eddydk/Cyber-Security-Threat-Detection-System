import boto3
import numpy as np

runtime_client = boto3.client("sagemaker-runtime")

# Sample input in CSV format
sample_input = "0.5,0.3,0.8,0.2,0.1,0.6,0.9,0.4"

# Invoke the endpoint
response = runtime_client.invoke_endpoint(
    EndpointName="cybersecurity-threat-endpoint",  # or use endpoint_name if defined
    ContentType="text/csv",
    Body=sample_input
)

# Get prediction from response
result = response["Body"].read().decode("utf-8")
prediction_score = float(result.strip())

# Interpret prediction
predicted_label = "THREAT" if prediction_score > 0.5 else "SAFE"

print(f"Prediction: {predicted_label}")