import pandas as pd

# Correct path to your cleaned attainment file
file_path = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_cleaned.csv"

# Read the file
df = pd.read_csv(file_path)

# Filter by sex
df_female = df[df['characteristic_value'] == 'Female']
df_male = df[df['characteristic_value'] == 'Male']

# Save each to the processed folder
df_female.to_csv("/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_female.csv", index=False)
df_male.to_csv("/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/attainment_male.csv", index=False)

print("Files saved: attainment_female.csv and attainment_male.csv")