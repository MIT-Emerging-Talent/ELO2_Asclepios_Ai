# Data Analysis

 Asclepios AI: Predictive Core and Twin-Engine Architecture

- **Readmission Risk Engine:** Identifies patients with "Chronic Relapse"
  phenotypes.
- **LOS Optimization Engine:** Prescribes the optimal Length of Stay based on
  clinical acuity.

This pipeline uses TEDS-D (Discharges) for
ground-truth label generation and implements a "Twin-Engine" architecture to
handle the statistical variance between Detox and Rehab settings.

## Methodology & Innovations

### 1. Solving the "Ghost Patient" Problem (Feature Engineering)

**The Challenge:** TEDS data is episode-level (no unique Patient ID), making
it impossible to track readmission history directly. Additionally, the NOPRIOR
variable in the 2023 dataset was found to be binary-corrupted.

**The Solution:** We engineered a Chronicity Proxy (Years_Using_Substance).

- **Logic:** Age At Admission - Age of First Use.
- **Validation:** EDA confirmed that "Short Duration" (<5 years) correlates
  with high volatility/dropout, while "Long Duration" (>20 years) correlates
  with stability.

### 2. The "Twin-Engine" Architecture (LOS Prediction)

**The Challenge:** A single regression model failed to predict Length of Stay
(LOS) accurately because "Detox" (3-5 days) and "Residential Rehab"
(30-90 days) follow fundamentally different distributions.

**The Solution:** We split the inference logic into two specialized models:

- **Engine A (Detox):** Trained only on acute care settings
  (Hospital/Residential Detox).
- **Engine B (Rehab):** Trained on long-term care settings.

**Result:** This reduced Mean Absolute Error (MAE) from 8+ days to 6.04 days.

### 3. Bias Stress Testing

**The Challenge:** Does the model predict LOS based on patient health, or just
state funding rules?

**The Solution:** We ran a "State-Blind" Stress Test by removing all geographic
features (STFIPS, REGION). The model performance remained stable (Delta < 0.1
days), proving it relies on clinical factors, not geography.

## 🤖 The Models

### Model 1: Readmission Risk Classifier

- **Algorithm:** XGBoost Classifier.
- **Target:** target_chronic_risk (Derived phenotype of chronic relapse).
- **Key Features:** Years_Using_Substance, Primary_Substance,
  Risk_Synergy_Speedball (Opioid+Stimulant interaction).
- **Performance:** AUC 0.75 (Strong discriminatory power).
- **Output:** Probability score (0-100%) of chronic relapse risk.

### Model 2: Optimal LOS Regressor (Twin Engine)

- **Algorithm:** XGBoost Quantile Regressor (Objective: reg:absoluteerror).
- **Target:** Length_of_Stay_Days (Median).
- **Why Median?** Healthcare data has extreme outliers (stays > 300 days).
  Predicting the Mean results in unrealistic recommendations. Predicting the
  Median ensures robust, clinically standard suggestions.
- **Performance:** MAE 6.1 Days (Precision window of +/- 1 week).

---

## Resource Demand Forecasting Model

This system is a predictive modeling pipeline designed to estimate
**treatment admissions**, **bed capacity**, **workforce requirements**, and
**clinical complexity** at the facility level.
It applies machine learning to aggregated TEDS patient data.

The model transforms raw episode-level treatment records into a structured,
decision-ready planning tool capable of predicting demand across multiple
treatment modalities, including:

- Detox 24-hour residential
- Short-term rehab
- Long-term rehab
- Intensive outpatient
- Non-intensive outpatient

---

## Methodology

### **1. Turning Patient-Level Episodes into Facility-Level Intelligence**

We engineered an **aggregation architecture** that transforms millions of
individual encounters into facility-type level population statistics. We computed:

- Total admissions (episode count)
- Average demographic distributions
- Average clinical-severity indicators
- Facility-level prevalence rates (e.g., % polysubstance use, % homeless,
% injection users)

By computing **means on one-hot encoded demographic fields**, the system
creates interpretable, population-level indicators.
Example:
`sex_Female = 0.42` to 42% of the facility’s patients are female.

This process allows the model to see patient composition instead of individual outliers.

---

### **2. Constructing the Facility Complexity Score**

We built a synthetic **Complexity Score**, representing clinical and
social risk intensity. It is a weighted combination of high-impact risk factors:

- Polysubstance use
- Chronic treatment history
- Co-occurring mental health disorder
- Homelessness
- Injection drug use

This score is later used not only for prediction but also for
**adjusting staffing needs**, because complex patients need more staff
per admission than low-acuity ones.

---

### **3. Training Pipeline (True Production Simulation)**

We built a **strict leakage-prevention pipeline**:

- Train/test split applied *before* imputation
- Imputer fit only on training data
- Scaler fit only on training data
- Log-transform applied to the target to reduce extreme skew

This ensures that the performance metrics reflect true real-world behavior.

---

### **4. The Model Framework (Multi-Algorithm Evaluation)**

A three-model ensemble evaluation was performed:

- **Ridge Regression** (linear, baseline)
- **Random Forest Regressor** (non-linear)
- **Gradient Boosting Regressor** (final winner)

#### Why Gradient Boosting Won

- Handles mixed-scale features effectively
- Robust against moderate noise
- Excellent for skewed target variables
- Achieved **R² = 0.623** on held-out test data
- Mean Absolute Error reduced to **≈ 3,000 admissions**

Cross-validation score:
**0.799 R² ± 0.048**, indicating strong generalization.

---

### **5. Full-Data Production Engine with Bias Correction**

Because Regression models trained on log-transformed targets tend to
underpredict population totals when transformed back to the original
scale (exp bias) the pipeline computes a **Bias Correction Factor**:

```text
Correction = Sum(actual) / Sum(predicted)
≈ 1.0014
```

This ensures that total predicted admissions match real-world
aggregate demand—critical for policy-level forecasting.

---

### **6. Translating Predictions Into Real Resource Requirements**

Predicted admissions alone don’t solve staffing or capacity questions.
We translate model outputs into **operational planning metrics**:

#### Beds Required

```text
1 bed per 12 annual admissions  
```

This reflects average turnover and realistic occupancy levels.

#### Staff Required

```text
1 staff per 50 admissions
Adjusted upward based on the facility’s Complexity Score
```

Facilities with severe populations require proportionally more clinical support.

#### High-Demand Flag

Facilities above median predicted admissions are labeled high-priority for:

- Funding
- Workforce allocation
- Surge planning

---

## The Predictive Architecture

### **Model: Facility Admission Forecaster (Primary Engine)**

- **Algorithm:** Gradient Boosting Regressor
- **Target:** Log-transformed annual admissions
- **Inputs:**

  - Demographic prevalence vectors
  - Clinical risk indicators
  - Social determinants
  - Complexity score
  - Treatment modality and geography indicators

### Key Predictive Signals (Feature Importance)

Top drivers include:

- Race/ethnicity prevalence patterns
- Age cohort distributions
- Education level indicators
- Service type
- Risk cluster prevalence

These patterns reveal that admissions are driven by **population composition**,
not just sheer size or location.

---

## Outputs & Deliverables

The final dataset includes:

- **Predicted Admissions**
- **Recommended Beds**
- **Recommended Staff (complexity-adjusted)**
- **Complexity Score**
- **High Demand Flag**
- **Top High-Demand Facilities Report**
- **Full Visualization Dashboard**
