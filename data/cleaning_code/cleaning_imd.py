import pandas as pd

# File path
raw_file = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/raw/populationbyimdenglandandwales2020.xlsx"

# Read second sheet, skip first 4 rows (0-indexed)
df = pd.read_excel(raw_file, sheet_name=1, header=None, skiprows=4)

# Set column names: first two are 'Sex' and 'Decile', rest are age groups
df.columns = ['Sex', 'Decile'] + list(df.columns[2:])

# Fill down 'Sex' column for empty cells
df['Sex'] = df['Sex'].ffill()

# Reshape from wide to long
age_columns = df.columns[2:]
df_long = df.melt(
    id_vars=['Sex', 'Decile'], 
    value_vars=age_columns, 
    var_name='Age', 
    value_name='Population'
)

# Convert to numeric
df_long['Decile'] = pd.to_numeric(df_long['Decile'], errors='coerce')
df_long['Age'] = pd.to_numeric(df_long['Age'], errors='coerce')
df_long['Population'] = pd.to_numeric(df_long['Population'], errors='coerce')

# Drop rows with missing values
df_long = df_long.dropna(subset=['Decile', 'Age', 'Population'])

# Optional: save cleaned dataset
df_long.to_csv("/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/imd_population_cleaned.csv", index=False)

# Preview
print(df_long.head(10))