# Datasets Folder

## Overview

This folder contains all datasets for the **Optimization of Treatment**
**Planning and Resource Allocation in Substance Use Disorder (SUD)**
**Rehabilitation Facilities** project. Data is organized into raw and
processed subfolders following best practices for reproducible research.

## Folder Structure

```text
1_datasets/
├── raw/
│   ├── tedsa_puf_2023.csv
│   └── tedsd_puf_2023.csv   
├── processed/
│   ├── teds_a_2023_cleaned.csv
│   ├── teds_analysis_ready.csv
│   ├── teds_ml_ready.csv
│   ├── teds_d_2023_cleaned.csv
│   ├── teds_d_analysis_ready.csv
│   └── teds_d_ml_ready.csv
├── sample/
│    └── tedsa_sample.csv
└── README.md

```

---

## Raw Data

### `raw/tedsa_puf_2023.csv`

**Source:** SAMHSA (Substance Abuse and Mental Health Services Administration)  
**Dataset:** Treatment Episode Data Set - Admissions (TEDS-A), 2023 Public Use
File  
**Download:** [SAMHSA TEDS Data](https://www.samhsa.gov/data/data-we-collect/teds-treatment-episode-data-set/datafiles)

**Characteristics:**

- **Records:** ~1,625,833 admission records
- **Variables:** 60 variables
- **Year:** 2023 admissions
- **Coverage:** 50 U.S. states, DC, Puerto Rico (excluding Delaware, South
Carolina, West Virginia)
- **Format:** CSV with numeric codes for categorical variables
- **Size:** ~300 MB

**Key Variables:**

- Demographics: Age, sex, race, ethnicity, education, employment
- Substance use: Primary/secondary/tertiary substances, route, frequency, age
at first use
- Treatment: Service type, referral source, prior episodes, medication-assisted therapy
- Clinical: DSM diagnosis, co-occurring mental health disorders
- Socioeconomic: Income, insurance, living arrangement, arrests
- Geographic: State, region, CBSA codes

**Data Restrictions:**

- Public use file with disclosure protection measures
- Data swapping applied to protect confidentiality
- Some geographic detail suppressed for small populations

---

### `raw/tedsd_puf_2023.csv`

**Source:** SAMHSA (Substance Abuse and Mental Health Services Administration)  
**Dataset:** Treatment Episode Data Set - Discharges (TEDS-D), 2023 Public Use
File  
**Download:** [SAMHSA TEDS Data](https://www.samhsa.gov/data/data-we-collect/teds-treatment-episode-data-set/datafiles)

**Characteristics:**

- **Records:** ~1,474,000 discharge records
- **Variables:** ~50 variables
- **Year:** 2023 discharges
- **Coverage:** 50 U.S. states, DC, Puerto Rico
- **Format:** CSV with numeric codes for categorical variables
- **Size:** ~300 MB

**Key Variables:**

- Demographics, substance use, treatment, clinical, socioeconomic, geographic  
- Discharge-specific: _D suffix variables track patient status at discharge

---

## Processed Data

### `processed/teds_a_2023_cleaned.csv`

**Created by:** `2_data_preparation\cleaning_teds_a.ipynb`  
**Purpose:** Fully cleaned and human-readable dataset for all analyses

**Processing Steps:**

1. Missing value codes (-9) converted to NaN
2. Data types optimized (categorical, Int8, Int64)
3. 17 new features engineered for treatment optimization
4. Categorical codes decoded to readable labels
5. 50 relevant variables selected and renamed

**Characteristics:**

- **Records:** ~1,625,833 (all original records retained)
- **Variables:** 50 variables
- **Format:** CSV with human-readable text labels
- **Size:** ~500MB
- **Missing Data:** Preserved as NaN for proper handling

**Variables:** See main project README or data dictionary for complete list

**Use Cases:**

- Exploratory Data Analysis (EDA)
- Initial statistical exploration
- Visualization and reporting
- General data inspection

### `processed/teds_d_2023_cleaned.csv`

**Created by:** `2_data_preparation/cleaning_teds_d.ipynb`  
**Purpose:** Fully cleaned TEDS-D dataset, human-readable

**Processing Steps:**

1. Missing value codes (-9) converted to NaN
2. Data types optimized (categorical, Int8, Int64)
3. New features engineered for treatment optimization
4. Categorical codes decoded to readable labels
5. Relevant variables selected and renamed

**Characteristics:**

- **Records:** ~1,474,000 (all original records retained)
- **Variables:** 74 variables
- **Format:** CSV with human-readable text labels
- **Size:** ~500MB
- **Missing Data:** Preserved as NaN for proper handling

**Use Cases:**

- Exploratory Data Analysis (EDA)
- Initial statistical exploration
- Visualization and reporting
- General data inspection

---

### `processed/teds_analysis_ready.csv`

**Created by:** `2_data_preparation\missing_value_handling_teds_a.ipynb`  
**Purpose:** Optimized for statistical analysis with minimal data loss

**Processing Steps:**

- Removed rows missing critical variables only:
  - `patient_id`
  - `service_type`
  - `primary_substance`
  - `age_group`
  - `sex`
- All other missing values preserved for pairwise deletion

**Characteristics:**

- **Records:** ~1,540,000 (95% retention)
- **Variables:** 50 variables
- **Missing Data:** Present in non-critical variables
- **Strategy:** Pairwise deletion (each test uses available data)

**Use Cases:**

- Statistical hypothesis testing
- Correlation analysis
- Chi-square tests
- Group comparisons (t-tests, ANOVA, Mann-Whitney)
- Regression analysis

**Advantages:**

- Maximizes statistical power
- Minimizes selection bias
- Standard practice in epidemiological research

---

### `processed/teds_d_analysis_ready.csv`

**Created by:** `2_data_preparation/missing_value_handling_teds_d.ipynb`  
**Purpose:** Optimized for statistical analysis with minimal data loss

**Processing Steps:**

- Removed rows missing critical variables only:
  - `patient_id`
  - `discharge_reason`
  - `length_of_stay`
- All other missing values preserved for pairwise deletion

**Characteristics:**

- **Records:** ~1,400,000 (95% retention)
- **Variables:** 74 variables
- **Missing Data:** Present in non-critical variables
- **Strategy:** Pairwise deletion (each test uses available data)

**Use Cases:**

- Statistical hypothesis testing
- Correlation analysis
- Chi-square tests
- Group comparisons (t-tests, ANOVA, Mann-Whitney)
- Regression analysis

**Advantages:**

- Maximizes statistical power
- Minimizes selection bias
- Standard practice in epidemiological research

---

### `processed/teds_ml_ready.csv`

**Created by:** `2_data_preparation\missing_value_handling_teds_a.ipynb`  
**Purpose:** Imputed dataset ready for machine learning models

**Processing Steps:**

1. **Numeric variables:** Imputed with median
   - `years_using`, `number_of_substances`

2. **Categorical variables:** Imputed with mode
   - `wait_time_days`, `prior_treatments`, `employment_status`
   - `education_level`, `living_arrangement`, `income_source`

3. **Binary variables:** Imputed with 0 (negative/absent)
   - All `is_*` and `has_*` flags

**Characteristics:**

- **Records:** ~1,625,833 (100% retention)
- **Variables:** 50 variables
- **Missing Data:** Imputed (no NaN values)
- **Strategy:** Statistical imputation

**Use Cases:**

- Machine learning model training
- Predictive modeling
- Classification and regression algorithms
- Neural networks
- Ensemble methods

**Important Notes:**

- Imputation may introduce bias
- Use with caution for inferential statistics
- Document imputation methods in model cards
- Consider multiple imputation for sensitivity analysis

### `processed/teds_d_ml_ready.csv`

**Created by:** `2_data_preparation/missing_value_handling_teds_d.ipynb`  
**Purpose:** Imputed dataset ready for machine learning models

**Processing Steps:**

1. **Numeric variables:** Imputed with median
   - `years_using`, `number_of_substances_admit`, `number_of_substances_discharge`

2. **Categorical variables:** Imputed with mode
   - `wait_time_days`, `prior_treatments`, `employment_admit`, `employment_discharge`
   - `education_level`, `living_arrangement_admit`, `living_arrangement_discharge`
   - `income_source`, `length_of_stay`, `discharge_reason`

3. **Binary variables:** Imputed with 0 (negative/absent)
   - All `is_*` and `has_*` flags
   - Treatment outcomes: `completed_treatment`, `dropped_out`, `terminated`, `transferred`
   - Stay indicators: `short_stay`, `long_stay`
   - Improvement metrics: `employment_improved`, `housing_improved`, `arrests_reduced`

4. **Remaining variables:** Imputed based on data type
   - Categorical: mode or 'Unknown'
   - Numeric: median or 0
   - Includes: demographics (sex, race, ethnicity, marital_status), arrests
data, substance details, clinical variables

**Characteristics:**

- **Records:** 1,474,025 (100% retention)
- **Variables:** 74 variables
- **Missing Data:** None (fully imputed)
- **Strategy:** Statistical imputation (median/mode/zero-filling)

**Use Cases:**

- Machine learning model training
- Predictive modeling
- Classification and regression algorithms
- Neural networks
- Ensemble methods

**Important Notes:**

- Imputation may introduce bias
- Use with caution for inferential statistics
- Document imputation methods in model cards
- Consider multiple imputation for sensitivity analysis

---

## Data Quality Summary

| Dataset | Records | Missing Data | Data Loss | Primary Use |
|---------|---------|--------------|-----------|-------------|
| **Raw TEDS-A** | 1,625,833 | Yes (-9 codes) | 0% | Source data |
| **Cleaned TEDS-A** | 1,625,833 | Yes (NaN) | 0% | EDA, visualization |
| **Analysis Ready TEDS-A** | ~1,540,000 | Yes (non-critical) | ~5% | tests |
| **ML Ready TEDS-A** | 1,625,833 | No (imputed) | 0% | Machine learning |
| **Raw TEDS-D** | 1,474,025 | Yes (-9 codes) | 0% | Source data |
| **Cleaned TEDS-D** | 1,474,025 | Yes (NaN) | 0% | EDA, visualization |
| **Analysis Ready TEDS-D** | ~1,400,000 | Yes (non-critical) | ~5% | tests |
| **ML Ready TEDS-D** | 1,474,025 | No (imputed) | 0% | Machine learning |

---

## Missing Data Patterns - TEDS-A

### High Missing Variables (>20%)

- `wait_time_days`: 53.7%
- `marital_status`: 29.2%
- `income_source`: 34.6%
- `education_level`: 20.9%
- `payment_source`: 53.4%

### Low Missing Variables (<5%)

- `patient_id`: 0%
- `age_group`: 0%
- `sex`: 0.1%
- `service_type`: 0%
- `primary_substance`: 18.2%

---

## Missing Data Patterns - TEDS-D

### High Missing Variables (>50%)

- `arrests_discharge`: 95.7%
- `arrests_admit`: 94.2%
- `tertiary_substance_discharge`: 84.7%
- `tertiary_substance_admit`: 82.0%
- `pregnant`: 67.4%
- `health_insurance`: 58.1%
- `payment_source`: 56.5%

### Low Missing Variables (<2%)

- `patient_id`: 0%
- `age_group`: 0%
- `sex`: 0.06%
- `service_type_admit`: 0%
- `discharge_reason`: 0%
- `length_of_stay`: 0%

---

## Data Processing Pipeline

```text
Raw Data (tedsx_puf_2023.csv)
    ↓
[Data Cleaning Pipeline]
    ↓
Cleaned Data (teds_x_2023_cleaned.csv)
    ↓
[Missing Value Strategy]
    ↓
    ├── Analysis Ready (95% data, pairwise deletion)
    └── ML Ready (100% data, imputation)
```

> **Note:** The TEDS-x dataset is not included in this repository due to size
and data governance considerations.  
> To reproduce analyses, download the dataset directly from SAMHSA TEDS Data.
> and place it in the `1_datasets/raw/` folder.
> x refers to A and D both.

### Reproducing Results

To reproduce cleaning and preprocessing:

1. Download `tedsa_puf_2023.csv` and `tedsd_puf_2023.csv`
2. Place it in `1_datasets/raw/`
3. Run `2_data_preparation/cleaning_teds_a.ipynb`,
`2_data_preparation/cleaning_teds_d.ipynb`
and `2_data_preparation/missing_value_handling_teds_a.ipynb`,
`2_data_preparation/missing_value_handling_teds_d.ipynb`.
4. Output files will appear in `1_datasets/processed/`
