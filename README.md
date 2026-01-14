# DAT5501_Assignment

## Education Attainment & Socioeconomic Analysis for Workforce Planning

This project analyses UK educational attainment and socioeconomic data to explore patterns in learner outcomes and workforce readiness. Focus areas include Level 2 & 3 attainment, gender differences, and deprivation scores across local authorities.

## Datasets

- `attainment_cleaned_female.csv` – Cleaned attainment data for female students.  
- `attainment_cleaned_male.csv` – Cleaned attainment data for male students.  
- `imd_data.csv` – Index of Multiple Deprivation scores by local authority.  

> Note: Large datasets (e.g., `attainment_cleaned.csv`) are tracked with Git LFS and not included in the repo. Tests requiring these files will pass locally but may fail on GitHub CI.

## Project Structure

DAT5501_Assignment/
├── data/
│   ├── raw/
│   ├── processed/
├── notebooks/
├── scripts/
│   ├── cleaning/
│   ├── analysis/
├── figures/
├── .circleci/
├── README.md
└── requirements.txt

## Setup

```bash
git clone https://github.com/YaminKas/DAT5501_Assignment.git
cd DAT5501_Assignment
pip install -r requirements.txt
git lfs install
git lfs pull