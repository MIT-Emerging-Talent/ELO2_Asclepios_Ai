# Data Cleaning Pipeline For TEDS Datasets

## Overview

This folder contains the data cleaning and preprocessing pipeline for the TEDS-A
and TEDS-D 2023 datasets, used in the project: **Optimization of Treatment**
**Planning and Resource**
**Allocation in Substance Use Disorder (SUD) Rehabilitation Facilities using**
**Artificial Intelligence and Predictive Analytics**.

## Dataset Information

### TEDS-A (Admissions)

- **Source:** SAMHSA (Substance Abuse and Mental Health Services Administration)
- **Dataset:** Treatment Episode Data Set - Admissions (TEDS-A), 2023
- **Records:** ~1.6 million admission records
- **Original Variables:** 60 variables
- **Cleaned Variables:** 50 relevant variables

### TEDS-D (Discharges)

- **Source:** SAMHSA (Substance Abuse and Mental Health Services Administration)
- **Dataset:** Treatment Episode Data Set - Discharges (TEDS-D), 2023
- **Records:** ~1.5 million discharge records
- **Original Variables:** ~50 variables
- **Cleaned Variables:** 74 relevant variables

---

## Files

### TEDS-A Processing

#### 1. `cleaning_teds_a.ipynb`

**Purpose:** Main data cleaning script that processes raw TEDS-A data.

**Pipeline Steps:**

1. Load raw CSV data
2. Handle missing values (convert -9 codes to NaN)
3. Optimize data types (reduce memory by ~70%)
4. Engineer 17 new features for treatment optimization
5. Decode categorical codes to readable labels
6. Select and rename 50 relevant columns
7. Save cleaned dataset

**Input:** `1_datasets/raw/tedsa_puf_2023.csv`  
**Output:** `1_datasets/processed/teds_a_2023_cleaned.csv`

---

#### 2. `missing_value_handling_teds_a.ipynb`

**Purpose:** Advanced missing value analysis and handling strategy for different
analysis types.

**Processing Steps:**

1. Analyze missing value patterns and percentages
2. Identify critical variables (cannot be missing)
3. Create analysis-ready dataset (minimal removal, ~95% retention)
4. Create ML-ready dataset (imputation, 100% retention)
5. Generate missing value report

**Input:** `1_datasets/processed/teds_a_2023_cleaned.csv`

**Outputs:**

- `1_datasets/processed/teds_analysis_ready.csv` - For statistical analysis
(pairwise deletion)
- `1_datasets/processed/teds_ml_ready.csv` - For machine learning (imputed values)

---

### TEDS-D Processing

#### 3. `cleaning_teds_d.ipynb`

**Purpose:** Main data cleaning script that processes raw TEDS-D data.

**Pipeline Steps:**

1. Load raw CSV data
2. Handle missing values (convert -9 codes to NaN)
3. Optimize data types (reduce memory usage)
4. Engineer discharge-specific features (treatment outcomes, improvements)
5. Decode categorical codes to readable labels
6. Select and rename 74 relevant columns
7. Save cleaned dataset

**Input:** `1_datasets/raw/tedsd_puf_2023.csv`  
**Output:** `1_datasets/processed/teds_d_2023_cleaned.csv`

---

#### 4. `missing_value_handling_teds_d.ipynb`

**Purpose:** Advanced missing value analysis and handling strategy for
discharge data.

**Processing Steps:**

1. Analyze missing value patterns and percentages
2. Identify critical variables (cannot be missing)
3. Create analysis-ready dataset (minimal removal, ~100% retention)
4. Create ML-ready dataset (comprehensive imputation, 100% retention)
5. Generate missing value report

**Input:** `1_datasets/processed/teds_d_2023_cleaned.csv`

**Outputs:**

- `1_datasets/processed/teds_d_analysis_ready.csv` - For statistical analysis
(pairwise deletion)
- `1_datasets/processed/teds_d_ml_ready.csv` - For machine learning (fully imputed)

---

## Input/Output Summary

### TEDS-A Workflow

#### Input

- **File:** `1_datasets/raw/tedsa_puf_2023.csv`
- **Format:** CSV file with TEDS-A 2023 admission records
- **Size:** ~1.6M rows × 60 columns

#### Outputs

##### 1. Primary Cleaned Dataset

- **File:** `1_datasets/processed/teds_a_2023_cleaned.csv`
- **Records:** ~1.6M rows × 50 columns
- **Features:** Human-readable column names and decoded categorical values
- **Use:** EDA
- **Missing Data:** Preserved as NaN

##### 2. Analysis-Ready Dataset

- **File:** `1_datasets/processed/teds_analysis_ready.csv`
- **Records:** ~1.54M rows (95% retention)
- **Strategy:** Minimal removal - only rows missing critical variables
- **Use:** Statistical hypothesis testing, correlation analysis
- **Missing Data:** Present in non-critical variables (handled via pairwise deletion)

##### 3. ML-Ready Dataset

- **File:** `1_datasets/processed/teds_ml_ready.csv`
- **Records:** ~1.6M rows (100% retention)
- **Strategy:** Statistical imputation (median/mode)
- **Use:** Machine learning model training
- **Missing Data:** None (imputed)

##### 4. Sample Dataset

- **File:** `1_datasets/sample/tedsa_sample.csv`
- **Records:** 1000 rows (0.0625% sample)
- **Strategy:** Random sampling
- **Use:** Visualization, initial exploration
- **Missing Data:** Preserved from original sample

---

### TEDS-D Workflow

#### Input - TEDS-A

- **File:** `1_datasets/raw/tedsd_puf_2023.csv`
- **Format:** CSV file with TEDS-D 2023 discharge records
- **Size:** ~1.5M rows × ~50 columns

#### Outputs - TEDS-A

##### 1. Primary Cleaned Dataset - TEDS-A

- **File:** `1_datasets/processed/teds_d_2023_cleaned.csv`
- **Records:** 1,474,025 rows × 74 columns
- **Features:** Human-readable column names, decoded categorical values,
discharge outcomes
- **Use:** EDA, discharge analysis
- **Missing Data:** Preserved as NaN

##### 2. Analysis-Ready Dataset - TEDS-A

- **File:** `1_datasets/processed/teds_d_analysis_ready.csv`
- **Records:** ~1,474,000 rows (~100% retention)
- **Strategy:** Minimal removal - only rows missing `patient_id` or `discharge_reason`
- **Use:** Statistical hypothesis testing, outcome analysis
- **Missing Data:** Present in non-critical variables (handled via pairwise
deletion)
- **Note:** `length_of_stay` has 64.55% missing data and is NOT used as critical
variable

##### 3. ML-Ready Dataset - TEDS-A

- **File:** `1_datasets/processed/teds_d_ml_ready.csv`
- **Records:** 1,474,025 rows (100% retention)
- **Strategy:** Comprehensive imputation across all 74 variables
- **Use:** Machine learning model training, predictive modeling
- **Missing Data:** None (fully imputed)

---

## Engineered Features

### TEDS-A Features (17 New Variables)

| Feature | Description | Type |
|---------|-------------|------|
| `years_using` | Years between first use and admission | Continuous |
| `number_of_substances` | Count of substances used (0-3) | Discrete |
| `is_polysubstance` | Uses 2+ substances | Binary |
| `is_opioid_primary` | Primary substance is opioid | Binary |
| `is_stimulant_primary` | Primary substance is stimulant | Binary |
| `is_alcohol_primary` | Primary substance is alcohol | Binary |
| `is_injection_user` | Uses injection route | Binary |
| `is_criminal_justice_referral` | Referred by criminal justice | Binary |
| `has_recent_arrest` | Arrested in past 30 days | Binary |
| `is_chronic_treatment` | 3+ prior treatment episodes | Binary |
| `is_first_treatment` | No prior treatment | Binary |
| `has_long_wait` | Waited 15+ days for treatment | Binary |
| `is_adolescent` | Age 12-17 | Binary |
| `is_older_adult` | Age 55+ | Binary |
| `is_pregnant` | Pregnant at admission | Binary |
| `is_homeless` | Experiencing homelessness | Binary |
| `has_no_income` | No source of income | Binary |
| `has_mental_health_disorder` | Co-occurring mental health disorder | Binary |

### TEDS-D Features (Additional Discharge-Specific)

| Feature | Description | Type |
|---------|-------------|------|
| `completed_treatment` | Successfully completed treatment | Binary |
| `dropped_out` | Left against medical advice | Binary |
| `terminated` | Terminated by facility | Binary |
| `transferred` | Transferred to another facility | Binary |
| `short_stay` | Length of stay < 30 days | Binary |
| `long_stay` | Length of stay > 90 days | Binary |
| `employment_improved` | Employment status improved at discharge | Binary |
| `housing_improved` | Living arrangement improved at discharge | Binary |
| `arrests_reduced` | Arrests reduced from admission to discharge | Binary |
| `number_of_substances_discharge` | Substance count at discharge | Discrete |
| All TEDS-A features | Admission baseline features | Various |

---

## Final Variables

### TEDS-A (50 Columns)

#### Demographics (10)

- `patient_id`, `age_group`, `sex`, `race`, `ethnicity`, `marital_status`,
`education_level`, `employment_status`, `living_arrangement`, `income_source`

#### Treatment Planning (8)

- `service_type`, `wait_time_days`, `referral_source`, `prior_treatments`,
`medication_assisted_therapy`, `dsm_diagnosis`, `self_help_attendance`,
`payment_source`

#### Substance Use Profile (10)

- `primary_substance`, `secondary_substance`, `tertiary_substance`,
`route_primary`, `route_secondary`, `route_tertiary`, `frequency_primary`,
`frequency_secondary`, `frequency_tertiary`, `age_first_use_primary`

#### Clinical Indicators (11)

- `injection_drug_use`, `years_using`, `number_of_substances`,
`substance_category`, `is_polysubstance`, `is_opioid_primary`,
`is_stimulant_primary`, `is_injection_user`, `has_cooccurring_mental_health`,
`has_mental_health_disorder`, `pregnant`

#### Risk Factors (6)

- `recent_arrests`, `is_criminal_justice_referral`, `has_recent_arrest`,
`is_homeless`, `has_no_income`, `is_pregnant`

#### Treatment History (2)

- `is_chronic_treatment`, `is_first_treatment`

#### Other (3)

- `state`, `region`, `veteran_status`, `health_insurance`, `has_long_wait`,
`is_adolescent`, `is_older_adult`

---

### TEDS-D (74 Columns)

Includes all TEDS-A variables PLUS discharge-specific variables:

#### Discharge Outcomes (4)

- `discharge_reason`, `completed_treatment`, `dropped_out`, `terminated`, `transferred`

#### Length of Stay (3)

- `length_of_stay`, `short_stay`, `long_stay`

#### Improvement Metrics (3)

- `employment_improved`, `housing_improved`, `arrests_reduced`

#### Discharge Status Variables (14)

- `employment_discharge`, `living_arrangement_discharge`, `arrests_discharge`
- `primary_substance_discharge`, `secondary_substance_discharge`, `tertiary_substance_discharge`
- `frequency_primary_discharge`, `self_help_attendance_discharge`
- `number_of_substances_discharge`
- Plus admission baseline versions of all discharge variables for comparison

---

## Key Transformations

### Missing Values

- **Original:** `-9` codes indicate missing/unknown/not collected
- **Cleaned:** Converted to `NaN` for proper pandas handling

### Categorical Decoding

All categorical variables decoded from numeric codes to text labels:

| Variable | Before | After |
|----------|--------|-------|
| AGE | `7` | `'35-39'` |
| SEX | `1` | `'Male'` |
| SUB1 | `5` | `'Heroin'` |
| SERVICES | `7` | `'Non-intensive Outpatient'` |
| EMPLOY | `3` | `'Unemployed'` |
| REASON | `1` | `'Treatment Completed'` |

### Column Renaming

All columns renamed for clarity:

| Original | Cleaned |
|----------|---------|
| `CASEID` | `patient_id` |
| `SERVICES` | `service_type_admit` (TEDS-D) |
| `DAYWAIT` | `wait_time_days` |
| `NOPRIOR` | `prior_treatments` |
| `LIVARAG` | `living_arrangement_admit` (TEDS-D) |
| `REASON` | `discharge_reason` (TEDS-D) |
| `LOS` | `length_of_stay` (TEDS-D) |

---

## Data Quality Notes

### TEDS-A Missing Data Strategy

#### 1. Minimal Removal (Analysis-Ready)

- Remove only rows missing: `patient_id`, `service_type`, `primary_substance`,
`age_group`, `sex`
- Retains ~95% of data
- Uses pairwise deletion for remaining variables
- Maximizes statistical power

#### 2. Imputation (ML-Ready)

- Median for continuous variables
- Mode for categorical variables
- 0 for binary flags
- Retains 100% of data

#### Missing Data Patterns

Key variables with high missing rates (>20%):

- `wait_time_days` (53.7%)
- `payment_source` (53.4%)
- `income_source` (34.6%)
- `marital_status` (29.2%)
- `education_level` (20.9%)

---

### TEDS-D Missing Data Strategy

#### 1. Minimal Removal (Analysis-Ready) - TEDS-D

- Remove only rows missing: `patient_id`, `discharge_reason`
- Retains ~100% of data
- Uses pairwise deletion for remaining variables
- **Note:** `length_of_stay` has 64.55% missing and is NOT used as critical variable

#### 2. Comprehensive Imputation (ML-Ready)

- **Numeric variables:** Median imputation (3 variables)
- **Categorical variables:** Mode imputation (10 variables)
- **Binary variables:** Zero-fill imputation (27 variables)
- **Remaining variables:** Type-based imputation (27 variables)
  - Categorical: mode or 'Unknown'
  - Numeric: median or 0
- Retains 100% of data with 0 missing values

#### Missing Data Patterns - TEDS-D

Key variables with high missing rates (>50%):

- `arrests_discharge` (95.7%)
- `arrests_admit` (94.2%)
- `tertiary_substance_discharge` (84.7%)
- `tertiary_substance_admit` (82.0%)
- `pregnant` (67.4%)
- `length_of_stay` (64.6%)
- `health_insurance` (58.1%)
- `payment_source` (56.5%)

---

## Workflow

### Step 1: Data Cleaning

#### TEDS-A

```bash
# Run main cleaning notebook
jupyter notebook cleaning_teds_a.ipynb
```

**Output:** `teds_a_2023_cleaned.csv`

#### TEDS-D

```bash
# Run main cleaning notebook
jupyter notebook cleaning_teds_d.ipynb
```

**Output:** `teds_d_2023_cleaned.csv`

---

### Step 2: Missing Value Handling

#### TEDS-A Handling

```bash
# Run missing value handling notebook
jupyter notebook missing_value_handling_teds_a.ipynb
```

**Outputs:**

- `teds_analysis_ready.csv`
- `teds_ml_ready.csv`

#### TEDS-D Handling

```bash
# Run missing value handling notebook
jupyter notebook missing_value_handling_teds_d.ipynb
```

**Outputs:**

- `teds_d_analysis_ready.csv`
- `teds_d_ml_ready.csv`

---

### Step 3: Choose Dataset for Your Analysis

#### For Admissions Analysis

- **For EDA:** Use `teds_a_2023_cleaned.csv`
- **For Statistical Tests:** Use `teds_analysis_ready.csv`
- **For ML Models:** Use `teds_ml_ready.csv`

#### For Discharge/Outcomes Analysis

- **For EDA:** Use `teds_d_2023_cleaned.csv`
- **For Statistical Tests:** Use `teds_d_analysis_ready.csv`
- **For ML Models:** Use `teds_d_ml_ready.csv`

#### For Longitudinal Analysis

- Use both TEDS-A and TEDS-D datasets
- Match records using `patient_id`
- Analyze admission → discharge trajectories

---

## Usage

### As Jupyter Notebook

#### Main Cleaning (TEDS-A or TEDS-D)

1. Open appropriate cleaning notebook (`cleaning_teds_a.ipynb` or `cleaning_teds_d.ipynb`)
2. Update file paths if needed
3. Run all cells sequentially
4. Cleaned data will be saved automatically

#### Missing Value Handling (TEDS-A or TEDS-D)

1. Open appropriate missing value notebook
2. Ensure cleaned dataset exists
3. Run all cells sequentially
4. Two datasets will be created for different analyses

---

## Notes for TEDS-D

**Length of Stay:** This variable has 64.55% missing data and should NOT be
used as a critical variable for row removal. It can still be analyzed using
pairwise deletion in the analysis-ready dataset or is imputed in the ML-ready
dataset.

**High Missing Variables:** Many discharge-specific variables (arrests,
tertiary substances, pregnancy status) have >60% missing data. This is
expected and should be considered when interpreting results.

**ML-Ready Dataset:** All 74 variables are fully imputed with 0 missing values,
using appropriate strategies for each data type.
