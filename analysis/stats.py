# /Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/analysis/stats.py

import pandas as pd

# ---------------------------
# 1. Load data
# ---------------------------
def load_data():
    imd_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/imd_cleaned.csv'
    male_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/merged/male_merged.csv'
    female_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/merged/female_merged.csv'

    imd = pd.read_csv(imd_path)
    male = pd.read_csv(male_path)
    female = pd.read_csv(female_path)

    print("Files loaded successfully!\n")
    return imd, male, female

# ---------------------------
# 2. IMD summary
# ---------------------------
def imd_summary(imd):
    print("\n=== IMD Dataset Info ===")
    print(imd.info())
    print("\nFirst 5 rows:")
    print(imd.head())
    print("\nSummary statistics:")
    print(imd.describe())
    print("\nMissing values per column:")
    print(imd.isnull().sum())

# ---------------------------
# 3. Attainment summary
# ---------------------------
def attainment_summary(df, gender):
    print(f"\n=== {gender} attainment Summary (value column) ===")
    print(df['value'].describe())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Example: top/bottom 5
    la_avg = df.groupby('la_name')['value'].mean().sort_values(ascending=False)
    print(f"\nTop 5 local authorities by average {gender} attainment:")
    print(la_avg.head())
    print(f"\nBottom 5 local authorities by average {gender} attainment:")
    print(la_avg.tail())

# ---------------------------
# 4. Run all stats
# ---------------------------
def run_statistics():
    imd, male, female = load_data()
    
    # IMD summary
    imd_summary(imd)
    
    # Attainment summaries
    attainment_summary(male, 'Male')
    attainment_summary(female, 'Female')

# ---------------------------
# 5. Execute if run directly
# ---------------------------
if __name__ == "__main__":
    run_statistics()