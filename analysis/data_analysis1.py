# /Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/analysis/data_analysis1.py

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
# 2. Dataset information
# ---------------------------
def dataset_info(df, name):
    print(f"\n=== {name} Dataset Info ===")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nSummary statistics:")
    print(df.describe(include='all'))
    print("\nMissing values per column:")
    print(df.isnull().sum())

# ---------------------------
# 3. IMD summary
# ---------------------------
def imd_summary(imd):
    print("\nTop 5 most deprived areas (IMD rank):")
    print(imd[['la_name', 'imd_rank']].sort_values('imd_rank').head())
    
    print("\nTop 5 least deprived areas (IMD rank):")
    print(imd[['la_name', 'imd_rank']].sort_values('imd_rank', ascending=False).head())

# ---------------------------
# 4. Attainment summary
# ---------------------------
def attainment_summary(df, gender):
    print(f"\n{gender} attainment summary (value column):")
    print(df['value'].describe())

    # Example: average attainment per LA
    la_avg = df.groupby('la_name')['value'].mean().sort_values(ascending=False)
    print(f"\nTop 5 local authorities by average {gender} attainment:")
    print(la_avg.head())

    print(f"\nBottom 5 local authorities by average {gender} attainment:")
    print(la_avg.tail())

# ---------------------------
# 5. Run all EDA
# ---------------------------
def run_eda():
    imd, male, female = load_data()
    
    # Info & summaries
    dataset_info(imd, 'IMD')
    dataset_info(male, 'Male Attainment')
    dataset_info(female, 'Female Attainment')
    
    # Quick analysis
    imd_summary(imd)
    attainment_summary(male, 'Male')
    attainment_summary(female, 'Female')

# ---------------------------
# 6. Main function for import
# ---------------------------
def main():
    run_eda()

# ---------------------------
# 7. Execute if run directly
# ---------------------------
if __name__ == "__main__":
    main()