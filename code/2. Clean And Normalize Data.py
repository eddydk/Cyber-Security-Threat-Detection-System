import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Drop columns that aren't useful for training
df = df.drop(columns=['id', 'attack_cat'])

# 2. Handle categorical columns using one-hot encoding
categorical_cols = ['proto', 'service', 'state']
df = pd.get_dummies(df, columns=categorical_cols)

# Fix: Convert any boolean columns to integers (True → 1, False → 0)
df = df.astype({col: 'int' for col in df.columns if df[col].dtype == 'bool'})

# 3. Normalize numerical columns (excluding the label)
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
numerical_cols.remove('label')

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Basic checks
print(df.shape)
print(df.columns)
print(df.head())
print(df['label'].value_counts())
