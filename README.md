# DAT5501_Assignment

## Education Attainment & Socio-Economic Deprivation Analysis (England)

This project analyses the relationship between educational attainment and socio-economic deprivation across English local authorities. Using publicly available government datasets, the analysis explores how attainment at Levels 2 and 3 varies with Index of Multiple Deprivation (IMD) rank, with a focus on structural inequality and workforce planning implications.

The project is exploratory and analytical in nature and does not aim to produce predictive models.

---

## Research Objectives

- Examine the relationship between IMD rank and educational attainment  
- Compare attainment patterns across gender  
- Identify structural disadvantage at local authority level  
- Inform education providers, local authorities, and employers  

---

## Data Sources

All datasets used in this project are publicly available:

- **Educational Attainment Data (Levels 2 & 3)**  
  Department for Education – Explore Education Statistics  
  https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/eef8c02f-af0d-4a73-9d5d-4ac15de37da3

- **Index of Multiple Deprivation (IMD)**  
  Ministry of Housing, Communities & Local Government  
  https://deprivation.communities.gov.uk/download-all

---

## Processed Datasets

- `attainment_cleaned_female.csv` – Female attainment by local authority  
- `attainment_cleaned_male.csv` – Male attainment by local authority  
- `imd_data.csv` – IMD ranks by local authority  

> Large raw datasets are managed using Git LFS and are not fully included in the repository.

---

## Methodology

- Data cleaning and preprocessing using **Python (pandas, numpy)**  
- Exploratory data analysis and visualisation using **matplotlib**  
- Scatter plots with fitted OLS regression lines  
- Correlation analysis and summary statistics  
- Basic unit tests to validate data transformations  

---

## Project Structure
DAT5501_Assignment/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── scripts/
│   ├── cleaning/
│   └── analysis/
├── figures/
├── tests/
├── README.md
└── requirements.txt

---

## Setup

```bash
git clone https://github.com/YaminKas/DAT5501_Assignment.git
cd DAT5501_Assignment
pip install -r requirements.txt
git lfs install
git lfs pull

Key Limitations
	•	Analysis is conducted at local authority level, not individual level
	•	IMD rank alone cannot explain all variation in attainment
	•	Data coverage is uneven across deprivation ranks
	•	Findings represent structural trends rather than causal conclusions

Intended Audience
	•	Teachers and education providers
	•	Local authorities and policymakers
	•	Employers and workforce planners


