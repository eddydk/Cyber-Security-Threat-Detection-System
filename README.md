# Cyber-Security-Threat-Detection-System
Cyber Security Threat System using SageMaker

# Overview of Project
This project involves building and deploying a Cybersecurity Threat Detection System using Amazon SageMaker. The system identifies anomalous network activity that may indicate cyberattacks, such as DDoS attacks, unauthorized access, or phishing attempts. The machine learning pipeline automates data ingestion, preprocessing, model training, deployment, and inference.

# Key components include:
- **Data Ingestion & Preprocessing**: Raw network traffic logs are collected, transformed, and feature-engineered to create a structured dataset.
- **Model Training & Evaluation**: An XGBoost model is trained to classify network activity as normal or malicious.
- **Deployment & Inference**: The trained model is deployed as an endpoint to detect real-time security threats.
- **Pipeline Automation**: An end-to-end SageMaker Pipeline automates data transformation, model training, and deployment.

# Services Used
- Amazon SageMaker: Trains, deploys, and serves the machine learning model. [Machine Learning]
- Amazon S3: Stores raw network traffic logs, preprocessed data, and model artifacts. [Storage]
- AWS Lambda: Automates data preprocessing tasks and feature extraction. [Compute]
- Amazon CloudWatch: Monitors model performance and logs security threats. [Monitoring]
- AWS IAM: Manages permissions and security policies for accessing AWS services. [Security]

# STEP 1: Preprocess Data and Feature Engineering
- Create an IAM Role for SageMaker with the following Access: **AmazonSageMakerFullAccess** and **AmazonS3FullAccess**
- Set Up Amazon SageMaker Notebook Instance using `ml.t2.medium`.
- Download a Public Dataset to S3: https://drive.google.com/uc?export=download&id=1ShuzJvAe5uANn6-0FQMW5gAL5sYa0Ncf
- Create bucket **'cybersecurity-ml-data1'** in S3, create a folder called **'raw data'** and Upload csv file there
- In SageMaker Notebook, open Jupyter (NOTE: All the code samples shown below need to be run in Jupyter. Just make sure you're using the correct S3 endpoint)
- Load & Explore the Dataset in SageMaker: `run 1.Load and Explore.py`
- Clean and Normalize the Data: run `2. Clean and normalize data.py`
- Implement Feature Engineering: run `3. Feature Engineering.py`
- Save the Preprocessed Data to S3: run `4. Save to S3.py`

# STEP 2: Training and Testing a Model using XGBoost
- Load Preprocessed Data from S3: run `5. Load Preprocessed Data from S3.py`
- Split Data into Train/Test Sets: run `6. Split Data into Train And Test Sets.py`
- Upload Training and Test Data to S3: run `7.Upload Training and Test Data to S3.py`
- Set Up the XGBoost Training Job: run `8. Setup XGBoost Training job.py`
- Train the Model: using `xgb.fit({'train': train_input, 'validation': test_input})`
- Install XGBoost using `!pip install xgboost`
- Evaluate Model Performance run `9. Evaluate Model Performance.py`

# STEP 3: Deploy and Serve the Model
- Create a SageMaker Model from the Trained Model Artifact: run `10. Create SageMaker Model from the Trained Model Artifact.py`
- Deploy the Model as a SageMaker Endpoint: run `11. Deploy the Model as Endpoint.py`
- Test the Deployed Endpoint: run `12. Test the Deployment.py`

# STEP 4: Automating with SageMaker Pipelines
- Define the SageMaker Pipeline Workflow. Steps in Our ML Pipeline
  - Data Processing Step → Load & preprocess raw data (S3 storage).
  - Training Step → Train XGBoost model on preprocessed data.
  - Evaluation Step → Check model performance (Accuracy, F1-score).
  - Conditional Deployment Step → Deploy the model only if it meets accuracy requirements.
- Create a SageMaker Pipeline Definition, run `13. Create SageMake Pipeline Definition.py`
- Trigger the Pipeline Execution, run `execution = run_pipeline()` and run `status = execution.describe()['PipelineExecutionStatus']`
- Automate Retraining with AWS EventBridge:
  - Create a Python3.9 Lambda function, paste the code in `14. trigger_cybersecurity_pipeline.py` -> Deploy Function
  - Create EventBridge Rule to execute function every time there is new data in S3
- Test the Automation:
  - Enable S3 Event Notifications -> Destination Lambda function
  - Test by running the following in notebook `15. Test.py`


# STEP 5: Test Setup
- Create a test file in your notebook and run `15. Test.py`
- What happens:
  -  New Data Arrives → File uploaded to s3://cybersecurity-ml-data1/new-data/
  -  S3 Notifies EventBridge → S3 sends event to EventBridge
  -  EventBridge Triggers Lambda → Lambda function receives the event
  -  Lambda Starts Pipeline → Your SageMaker pipeline begins training
  -  Automatic Retraining → Model updates without manual intervention
