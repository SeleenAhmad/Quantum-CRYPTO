#importing imp libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#assigning the file path
file_path= r'C:\Users\DELL\Downloads\quantum_vs_classical_fraud_dataset.csv'
df=pd.read_csv(file_path)
print(df.describe())
df.info()
df['latency_ms']=df['latency_ms'].fillna(df['latency_ms'].median())
df['transaction_value_usd']=df['transaction_value_usd'].fillna(df['transaction_value_usd'].median())
df['expected_profit_usd']=df['expected_profit_usd'].fillna(df['expected_profit_usd'].median())
df['region'] = df['region'].fillna(df['region'].mode()[0])
df.duplicated().sum()
df = df.drop_duplicates()
df.info()
df.to_csv("quantum_vs_classical_fraud_cleaned.csv", index=False)

