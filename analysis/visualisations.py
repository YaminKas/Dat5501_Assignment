import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualisations():
    # Paths to your merged data
    male_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/merged/male_merged.csv'
    female_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/merged/female_merged.csv'
    imd_path = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/data/processed/imd_cleaned.csv'

    # Load data
    male = pd.read_csv(male_path)
    female = pd.read_csv(female_path)
    imd = pd.read_csv(imd_path)

    # Create figures directory if it doesn't exist
    figures_dir = '/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment/analysis/figures'
    os.makedirs(figures_dir, exist_ok=True)

    # --------------------------
    # IMD Distribution
    # --------------------------
    plt.figure(figsize=(10,6))
    sns.histplot(imd['imd_rank'], bins=30, kde=True, color='steelblue')
    plt.title('Distribution of IMD Ranks')
    plt.xlabel('IMD Rank')
    plt.ylabel('Count')
    plt.savefig(os.path.join(figures_dir, 'imd_distribution.png'))
    plt.close()

    # --------------------------
    # Male Attainment Top/Bottom 5
    # --------------------------
    male_avg = male.groupby('la_name')['value'].mean().reset_index()

    # Top 5
    top5 = male_avg.sort_values('value', ascending=False).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top5['value'], y=top5['la_name'], color='green')
    plt.title('Top 5 Local Authorities by Male Attainment')
    plt.xlabel('Average Attainment')
    plt.ylabel('Local Authority')
    plt.savefig(os.path.join(figures_dir, 'top5_male_attainment.png'))
    plt.close()

    # Bottom 5
    bottom5 = male_avg.sort_values('value', ascending=True).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(x=bottom5['value'], y=bottom5['la_name'], color='red')
    plt.title('Bottom 5 Local Authorities by Male Attainment')
    plt.xlabel('Average Attainment')
    plt.ylabel('Local Authority')
    plt.savefig(os.path.join(figures_dir, 'bottom5_male_attainment.png'))
    plt.close()

    # --------------------------
    # Female Attainment Top/Bottom 5
    # --------------------------
    female_avg = female.groupby('la_name')['value'].mean().reset_index()

    # Top 5
    top5_f = female_avg.sort_values('value', ascending=False).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top5_f['value'], y=top5_f['la_name'], color='green')
    plt.title('Top 5 Local Authorities by Female Attainment')
    plt.xlabel('Average Attainment')
    plt.ylabel('Local Authority')
    plt.savefig(os.path.join(figures_dir, 'top5_female_attainment.png'))
    plt.close()

    # Bottom 5
    bottom5_f = female_avg.sort_values('value', ascending=True).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(x=bottom5_f['value'], y=bottom5_f['la_name'], color='red')
    plt.title('Bottom 5 Local Authorities by Female Attainment')
    plt.xlabel('Average Attainment')
    plt.ylabel('Local Authority')
    plt.savefig(os.path.join(figures_dir, 'bottom5_female_attainment.png'))
    plt.close()

    print(f"All figures saved to {figures_dir}")

    # --------------------------
    # IMD vs Attainment Scatter Plots
    # --------------------------

    # Merge IMD with male and female averages
    male_imd = male_avg.merge(imd[['la_name', 'imd_rank']], on='la_name', how='inner')
    female_imd = female_avg.merge(imd[['la_name', 'imd_rank']], on='la_name', how='inner')

    # Male scatter
    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=male_imd,
        x='imd_rank',
        y='value',
        alpha=0.6
    )
    sns.regplot(
        data=male_imd,
        x='imd_rank',
        y='value',
        scatter=False
    )
    plt.title('IMD Rank vs Male Attainment')
    plt.xlabel('IMD Rank (Higher = Less Deprived)')
    plt.ylabel('Average Male Attainment')
    plt.savefig(os.path.join(figures_dir, 'imd_vs_male_attainment.png'))
    plt.close()

    # Female scatter
    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=female_imd,
        x='imd_rank',
        y='value',
        alpha=0.6
    )
    sns.regplot(
        data=female_imd,
        x='imd_rank',
        y='value',
        scatter=False
    )
    plt.title('IMD Rank vs Female Attainment')
    plt.xlabel('IMD Rank (Higher = Less Deprived)')
    plt.ylabel('Average Female Attainment')
    plt.savefig(os.path.join(figures_dir, 'imd_vs_female_attainment.png'))
    plt.close()


    # --------------------------
    # Combined Male vs Female IMD Scatter
    # --------------------------

    combined = pd.concat([
        male_imd.assign(gender='Male'),
        female_imd.assign(gender='Female')
    ])

    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=combined,
        x='imd_rank',
        y='value',
        hue='gender',
        alpha=0.6
    )

    sns.regplot(
        data=male_imd,
        x='imd_rank',
        y='value',
        scatter=False,
        label='Male Trend'
    )

    sns.regplot(
        data=female_imd,
        x='imd_rank',
        y='value',
        scatter=False,
        label='Female Trend'
    )

    plt.title('IMD Rank vs Attainment by Gender')
    plt.xlabel('IMD Rank (Higher = Less Deprived)')
    plt.ylabel('Average Attainment')
    plt.legend(title='Gender')
    plt.savefig(os.path.join(figures_dir, 'imd_vs_attainment_gender_comparison.png'))
    plt.close()