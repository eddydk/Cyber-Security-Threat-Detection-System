from sagemaker import image_uris
from sagemaker.estimator import Estimator

xgboost_image_uri = image_uris.retrieve("xgboost", region=session.boto_region_name, version="1.3-1")

xgb = Estimator(
    image_uri=xgboost_image_uri,
    role=sagemaker.get_execution_role(),
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=f's3://cybersecurity-ml-data1/xgboost-model-output',
    sagemaker_session=session
)

xgb.set_hyperparameters(
    objective='binary:logistic',
    num_round=100,
    max_depth=5,
    eta=0.2,
    gamma=4,
    min_child_weight=6,
    subsample=0.8,
    verbosity=1
)
