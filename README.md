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

# PRE-REQUISITES: STEPS TO BE PERFORMED: 
- Create an IAM Role for SageMaker
- Set Up Amazon SageMaker Notebook Instance (Jupyter)
- Download & Upload a Public Dataset to S3
- Load & Explore the Dataset in SageMaker
- Clean and Normalize the Data
- Feature Engineering
- Save the Preprocessed Data to S3
