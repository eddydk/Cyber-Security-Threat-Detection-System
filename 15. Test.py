# Test automation
import boto3

s3_client = boto3.client('s3')

# Upload a test file to trigger the pipeline
test_content = "This is test data for pipeline automation"
s3_client.put_object(
    Bucket='cybersecurity-ml-data1',
    Key='new-data/test-trigger.txt',
    Body=test_content
)

print("Test file uploaded! Check Lambda logs to see if pipeline triggered.")