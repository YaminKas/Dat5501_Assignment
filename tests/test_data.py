import os
import pandas as pd

BASE_DIR = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment"
MERGED_DIR = os.path.join(BASE_DIR, "data/merged")

def test_merged_files_exist():
    male_path = os.path.join(MERGED_DIR, "male_merged.csv")
    female_path = os.path.join(MERGED_DIR, "female_merged.csv")
    assert os.path.isfile(male_path), "Male merged CSV not found."
    assert os.path.isfile(female_path), "Female merged CSV not found."

def test_merged_files_not_empty():
    male = pd.read_csv(os.path.join(MERGED_DIR, "male_merged.csv"))
    female = pd.read_csv(os.path.join(MERGED_DIR, "female_merged.csv"))
    assert not male.empty, "Male merged CSV is empty."
    assert not female.empty, "Female merged CSV is empty."