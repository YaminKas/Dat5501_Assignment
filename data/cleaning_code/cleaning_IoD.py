import pandas as pd

# Load the CSV
imd_file = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/raw/IoD2025 Local Authority District Summaries (lower-tier) - Rank of average rank.csv"
imd_df = pd.read_csv(imd_file)

# Inspect the columns
print(imd_df.columns)

# Optional: rename columns to match your attainment CSV for merging
imd_df = imd_df.rename(columns={
    "Local Authority District code (2024)": "la_code",
    "Local Authority District name (2024)": "la_name",
    "Index of Multiple Deprivation (IMD) Rank (where 1 is most deprived)": "imd_rank",
    "Income - Rank (where 1 is most deprived)": "imd_income_rank",
    "Employment - Rank (where 1 is most deprived)": "imd_employment_rank",
    "Education, Skills and Training - Rank (where 1 is most deprived)": "imd_education_rank",
    "Health Deprivation and Disability - Rank (where 1 is most deprived)": "imd_health_rank",
    "Crime - Rank (where 1 is most deprived)": "imd_crime_rank",
    "Barriers to Housing and Services - Rank (where 1 is most deprived)": "imd_housing_rank",
    "Living Environment - Rank (where 1 is most deprived)": "imd_living_env_rank",
    "IDACI - Rank (where 1 is most deprived)": "idaci_rank",
    "IDAOPI - Rank (where 1 is most deprived)": "idaopi_rank"
})

# Optional: drop any duplicates just in case
imd_df = imd_df.drop_duplicates(subset="la_code")

# Optional: check first rows
print(imd_df.head())

# Save cleaned version (optional)
imd_df.to_csv("/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/imd_cleaned.csv", index=False)