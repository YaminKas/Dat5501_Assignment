import os
import pandas as pd
import numpy as np
import statsmodels.api as sm

BASE_DIR = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment"
MERGED_DIR = os.path.join(BASE_DIR, "data/merged")
CLEAN_DIR = os.path.join(BASE_DIR, "data/cleaned")

os.makedirs(CLEAN_DIR, exist_ok=True)

def clean_dataset(filename):
    """Load merged dataset, drop rows with missing key data, and save cleaned version."""
    df = pd.read_csv(os.path.join(MERGED_DIR, filename))
    
    #Drop rows where LA name, IMD rank, or attainment value are missing
    df_clean = df.dropna(subset=["la_name", "imd_rank", "value"])
    
    #Optional: reset index
    df_clean = df_clean.reset_index(drop=True)
    
    # Save cleaned version
    clean_path = os.path.join(CLEAN_DIR, filename)
    df_clean.to_csv(clean_path, index=False)
    print(f"Saved cleaned dataset: {clean_path}")
    return df_clean

# Clean both datasets
male_clean = clean_dataset("male_merged.csv")
female_clean = clean_dataset("female_merged.csv")