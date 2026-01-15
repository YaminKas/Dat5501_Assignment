import pandas as pd
import os

# File paths
male_file = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_male.csv'
female_file = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_female.csv'
imd_file = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/imd_cleaned.csv'
output_folder = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/merged'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read CSVs
male_df = pd.read_csv(male_file)
female_df = pd.read_csv(female_file)
imd_df = pd.read_csv(imd_file)

#Male + the IMD
male_merged = pd.merge(
    male_df,
    imd_df,
    left_on=['new_la_code', 'la_name'],
    right_on=['la_code', 'la_name'],
    how='left'
)
male_merged = male_merged.drop(columns=['la_code'])
male_merged.to_csv(os.path.join(output_folder, 'male_merged.csv'), index=False)
print("Saved male_merged.csv")

# Female +  IMD
female_merged = pd.merge(
    female_df,
    imd_df,
    left_on=['new_la_code', 'la_name'],
    right_on=['la_code', 'la_name'],
    how='left'
)
female_merged = female_merged.drop(columns=['la_code'])
female_merged.to_csv(os.path.join(output_folder, 'female_merged.csv'), index=False)
print("Saved female_merged.csv")

# Combined Male & Female + IMD 
male_df_renamed = male_df.rename(columns={'value': 'value_male'})
female_df_renamed = female_df.rename(columns={'value': 'value_female'})

merge_keys = [
    'time_period', 'time_identifier', 'geographic_level', 'country_code',
    'country_name', 'version', 'region_code', 'region_name', 
    'old_la_code', 'new_la_code', 'la_name', 'characteristic_type',
    'characteristic_value', 'establishment_type', 'establishment_type_group', 'metric'
]

combined = pd.merge(male_df_renamed, female_df_renamed, on=merge_keys, how='outer')

# Merge with IMD
combined_merged = pd.merge(
    combined,
    imd_df,
    left_on=['new_la_code', 'la_name'],
    right_on=['la_code', 'la_name'],
    how='left'
)
combined_merged = combined_merged.drop(columns=['la_code'])
combined_merged.to_csv(os.path.join(output_folder, 'combined_merged.csv'), index=False)
print("Saved combined_merged.csv")