# Import Libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

plt.style.use("seaborn-v0_8")
sns.set_theme(style="whitegrid")

path = kagglehub.dataset_download("bhavyamotiyani/diabetes-dataset-with-missing-value-for-practice")
file_path = os.path.join(path, "Diabetes Missing Data.csv")
# Task 1: Load the dataset into a pandas DataFrame using pd.read_csv(). 
# Print the first five rows, the column data types (.dtypes), and the DataFrame shape.

df = pd.read_csv(file_path)

print(df.head())
print(f"\nData Types\n{df.dtypes}")
print(f"\nShape : {df.shape}")

# Task 2: Null value analysis: 
# Compute the count and percentage of missing values in every column using df.isnull().sum() 
# and (df.isnull().sum() / df.shape[0]) * 100. 

null_count = df.isnull().sum()
null_percent = (df.isnull().sum()/df.shape[0])*100

null_table = pd.DataFrame({
    "Missing Count":null_count,
    "Missing %":null_percent
})
print(null_table)

# Report which columns exceed a 20% null rate. 

print("\nColumns >20% missing")
print(null_table[null_table["Missing %"]>20])

# For columns below 20% nulls, fill numeric columns with the column median using fillna(df[col].median()). 
# Justify in the README why you chose the median rather than the mean.

for col in df.columns:

    if df[col].isnull().mean()*100 <20:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())

# Task 3: Duplicate detection and removal: 
# Use df.duplicated().sum() to count duplicates. Remove them with df.drop_duplicates(). 
# Report how many rows were removed and whether the removal changes the null percentage.

duplicates = df.duplicated().sum()
print("Duplicates =",duplicates)
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print("Rows Removed =",before-after)
print(df.isnull().mean()*100)

