import pandas as pd
import numpy as np
from scipy.stats import zscore

df_cleaned = df.dropna()

# remove outliers with a z-score over 2.5 
def remove_outliers(df_cleaned, column):
    z_scores = zscore(df_cleaned[column])
    return df_cleaned[np.abs(z_scores) < 2.5 ]

# Loop over each column in the dataset to remove outliers
for column in df_cleaned.columns:
    df_cleaned = remove_outliers(df_cleaned, column)

df_cleaned.to_csv('cleaned_dataset.csv', index=False)