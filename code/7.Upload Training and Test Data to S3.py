import sagemaker

session = sagemaker.Session()
bucket = 'cybersecurity-ml-data1'
train_prefix = 'xgboost-data/train'
test_prefix = 'xgboost-data/test'

train_input = session.upload_data('train.libsvm', bucket=bucket, key_prefix=train_prefix)
test_input = session.upload_data('test.libsvm', bucket=bucket, key_prefix=test_prefix)

print(f"Training data: {train_input}")
print(f"Testing data: {test_input}")
