# SageMaker Pipeline
import boto3
import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep
from sagemaker.workflow.parameters import ParameterString
from sagemaker.inputs import TrainingInput
from sagemaker import image_uris

# Setup
session = sagemaker.Session()
role = sagemaker.get_execution_role()
bucket = 'cybersecurity-ml-data1'

# Parameters
training_instance_type = ParameterString(
    name="TrainingInstanceType", 
    default_value="ml.m5.large"
)

# Use built-in XGBoost (same as your step 3.3)
xgb_estimator = sagemaker.estimator.Estimator(
    image_uri=image_uris.retrieve("xgboost", session.boto_region_name, version="1.3-1"),
    role=role,
    instance_count=1,
    instance_type=training_instance_type,
    output_path=f's3://{bucket}/pipeline-model-output/',
    hyperparameters={
        'objective': 'binary:logistic',
        'num_round': 100,
        'max_depth': 5,
        'eta': 0.2,
        'gamma': 4,
        'min_child_weight': 6,
        'subsample': 0.8,
        'verbosity': 1
    }
)

# Training Step
step_train = TrainingStep(
    name="TrainCybersecurityModel",
    estimator=xgb_estimator,
    inputs={
        "train": TrainingInput(
            s3_data=f's3://{bucket}/xgboost-data/train/train.libsvm',
            content_type="text/libsvm"
        ),
        "validation": TrainingInput(
            s3_data=f's3://{bucket}/xgboost-data/test/test.libsvm',
            content_type="text/libsvm"
        )
    }
)

# Create Pipeline
pipeline = Pipeline(
    name="simple-cybersecurity-pipeline",
    parameters=[training_instance_type],
    steps=[step_train],
    sagemaker_session=session,
)

# Run Pipeline
def run_pipeline():
    pipeline.upsert(role_arn=role)
    print("Pipeline created successfully!")
    
    execution = pipeline.start()
    print(f"Pipeline execution started: {execution.arn}")
    return execution

print("Automated pipeline ready! Run: execution = run_pipeline()")