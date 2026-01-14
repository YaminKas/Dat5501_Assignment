import pandas as pd
import os

# File paths
raw_file = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/raw/aggregated_attainment_by_region_characteristic_202125.csv"
processed_file = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_cleaned.csv"

# Make sure processed folder exists
os.makedirs(os.path.dirname(processed_file), exist_ok=True)

# Read CSV with low_memory to avoid DtypeWarning
df = pd.read_csv(raw_file, low_memory=False)

# Identify numeric columns
numeric_cols = [col for col in df.columns if
                'number_of_students' in col or
                'aps_per_entry' in col or
                col.startswith('pc_')]

# Convert numeric columns to floats (errors='coerce' will turn non-numeric to NaN)
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Columns to keep as identifiers
id_cols = [
    'time_period', 'time_identifier', 'geographic_level',
    'country_code', 'country_name', 'version', 'region_code', 'region_name',
    'old_la_code', 'new_la_code', 'la_name', 'characteristic_type', 'characteristic_value',
    'establishment_type', 'establishment_type_group'
]

# Melt to long format
df_long = df.melt(
    id_vars=id_cols,
    value_vars=numeric_cols,
    var_name='metric',
    value_name='value'
)

# Save cleaned data
df_long.to_csv(processed_file, index=False)

# Quick check
print(df_long.head())
print(df_long.info())