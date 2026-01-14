import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import pearsonr, spearmanr, ttest_ind

BASE_DIR = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment"
CLEAN_DIR = os.path.join(BASE_DIR, "data/cleaned")

GENDER_FILES = ["male_merged.csv", "female_merged.csv"]

# -----------------------------
# 1. Cleaning tests
# -----------------------------
def test_no_missing_values():
    """Ensure no missing la_name, imd_rank, or value in cleaned datasets."""
    for f in GENDER_FILES:
        df = pd.read_csv(os.path.join(CLEAN_DIR, f))
        for col in ["la_name", "imd_rank", "value"]:
            missing = df[col].isnull().sum()
            assert missing == 0, f"{missing} missing values in {col} of {f}"

# -----------------------------
# 2. Correlation tests
# -----------------------------
def test_correlation_finite():
    """Pearson and Spearman correlations should be finite numbers."""
    for f in GENDER_FILES:
        df = pd.read_csv(os.path.join(CLEAN_DIR, f))
        x = df["imd_rank"]
        y = df["value"]
        pearson_r, _ = pearsonr(x, y)
        spearman_r, _ = spearmanr(x, y)
        assert np.isfinite(pearson_r), f"Pearson r not finite in {f}"
        assert np.isfinite(spearman_r), f"Spearman r not finite in {f}"

# -----------------------------
# 3. Regression tests
# -----------------------------
def test_regression_coefficients_finite():
    """Regression runs and coefficients are finite."""
    for f in GENDER_FILES:
        df = pd.read_csv(os.path.join(CLEAN_DIR, f))
        X = sm.add_constant(df["imd_rank"])
        y = df["value"]
        model = sm.OLS(y, X).fit()
        assert all(np.isfinite(model.params)), f"Regression coefficients contain NaN or inf in {f}"
        assert np.isfinite(model.rsquared), f"R-squared is NaN or inf in {f}"

# -----------------------------
# 4. Gender comparison (t-test)
# -----------------------------
def test_ttest_valid():
    """T-test between male and female attainment should return finite t and p-values."""
    male = pd.read_csv(os.path.join(CLEAN_DIR, "male_merged.csv"))
    female = pd.read_csv(os.path.join(CLEAN_DIR, "female_merged.csv"))
    t_stat, p_val = ttest_ind(male["value"], female["value"], equal_var=False)
    assert np.isfinite(t_stat), "t-statistic is not finite"
    assert np.isfinite(p_val), "p-value is not finite"