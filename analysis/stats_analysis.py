import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, ttest_ind
import statsmodels.api as sm


def run_statistics():
    
    # All the paths
    BASE_DIR = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment"

    male_path = f"{BASE_DIR}/data/merged/male_merged.csv"
    female_path = f"{BASE_DIR}/data/merged/female_merged.csv"

    stats_dir = f"{BASE_DIR}/data/analysis/stats_output"
    figures_dir = f"{BASE_DIR}/analysis/figures"

    os.makedirs(stats_dir, exist_ok=True)
    os.makedirs(figures_dir, exist_ok=True)

    
    # Load data
    
    male = pd.read_csv(male_path)
    female = pd.read_csv(female_path)

    male_clean = male[["la_name", "value", "imd_rank"]].dropna()
    female_clean = female[["la_name", "value", "imd_rank"]].dropna()

    
    #Correlation Analysis
    
    results = []

    for label, df in [("Male", male_clean), ("Female", female_clean)]:
        pearson_r, pearson_p = pearsonr(df["imd_rank"], df["value"])
        spearman_r, spearman_p = spearmanr(df["imd_rank"], df["value"])

        results.append({
            "gender": label,
            "pearson_r": pearson_r,
            "pearson_p": pearson_p,
            "spearman_r": spearman_r,
            "spearman_p": spearman_p
        })

    corr_df = pd.DataFrame(results)
    corr_df.to_csv(f"{stats_dir}/correlations.csv", index=False)

    
    # Gender Comparison (t-test)
    
    t_stat, p_val = ttest_ind(
        male_clean["value"],
        female_clean["value"],
        equal_var=False
    )

    ttest_df = pd.DataFrame([{
        "t_statistic": t_stat,
        "p_value": p_val,
        "male_mean": male_clean["value"].mean(),
        "female_mean": female_clean["value"].mean()
    }])

    ttest_df.to_csv(f"{stats_dir}/gender_ttest_results.csv", index=False)

    
    #Regression Analysis
    
    def run_regression(df, label):
        X = sm.add_constant(df["imd_rank"])
        y = df["value"]
        model = sm.OLS(y, X).fit()

        return {
            "gender": label,
            "intercept": model.params["const"],
            "imd_coef": model.params["imd_rank"],
            "p_value": model.pvalues["imd_rank"],
            "r_squared": model.rsquared
        }, model

    male_reg, male_model = run_regression(male_clean, "Male")
    female_reg, female_model = run_regression(female_clean, "Female")

    reg_df = pd.DataFrame([male_reg, female_reg])
    reg_df.to_csv(f"{stats_dir}/regression_results.csv", index=False)

    
    #Scatter + Regression Plots
    
    def scatter_plot(df, model, title, filename):
        plt.figure(figsize=(8, 6))
        plt.scatter(df["imd_rank"], df["value"], alpha=0.4)

        x_vals = np.linspace(df["imd_rank"].min(), df["imd_rank"].max(), 100)
        y_vals = model.params["const"] + model.params["imd_rank"] * x_vals

        plt.plot(x_vals, y_vals)
        plt.xlabel("IMD Rank (higher = less deprived)")
        plt.ylabel("Attainment")
        plt.title(title)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    scatter_plot(
        male_clean,
        male_model,
        "IMD Rank vs Male Attainment",
        f"{figures_dir}/scatter_imd_vs_attainment_male.png"
    )

    scatter_plot(
        female_clean,
        female_model,
        "IMD Rank vs Female Attainment",
        f"{figures_dir}/scatter_imd_vs_attainment_female.png"
    )

    print("Statistics analysis complete.")
    print(f"Stats saved to {stats_dir}")
    print(f"Figures saved to {figures_dir}")


if __name__ == "__main__":
    run_statistics()