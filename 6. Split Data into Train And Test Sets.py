from sklearn.model_selection import train_test_split
from sklearn.datasets import dump_svmlight_file
import pandas as pd

# Load data
df = pd.read_csv('preprocessed_data.csv')

X = df.drop(columns=['label'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# CSV for inspection
train_df = pd.concat([y_train, X_train], axis=1)
test_df = pd.concat([y_test, X_test], axis=1)
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

# LIBSVM for SageMaker
dump_svmlight_file(X_train, y_train, 'train.libsvm', zero_based=True)
dump_svmlight_file(X_test, y_test, 'test.libsvm', zero_based=True)