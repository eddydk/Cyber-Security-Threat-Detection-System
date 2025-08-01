import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report

# Load and convert data
train_data = pd.read_csv('train.csv', header=None, dtype=str)
test_data = pd.read_csv('test.csv', header=None, dtype=str)

# Convert all columns to numeric
train_data = train_data.apply(pd.to_numeric, errors='coerce')
test_data = test_data.apply(pd.to_numeric, errors='coerce')

# Drop any rows with NaNs
train_data = train_data.dropna()
test_data = test_data.dropna()

# Split into features (X) and labels (y)
X_train = train_data.iloc[:, 1:]
y_train = train_data.iloc[:, 0]
X_test = test_data.iloc[:, 1:]
y_test = test_data.iloc[:, 0]

# Convert to DMatrix format
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

# Set parameters and train the model
params = {
    "objective": "binary:logistic",
    "max_depth": 5,
    "eta": 0.2,
    "gamma": 4,
    "min_child_weight": 6,
    "subsample": 0.8,
    "verbosity": 1
}

model = xgb.train(params=params, dtrain=dtrain, num_boost_round=100)

# Predict
y_pred_prob = model.predict(dtest)
y_pred = [1 if p > 0.5 else 0 for p in y_pred_prob]

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
