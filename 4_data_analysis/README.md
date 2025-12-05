# Data Analysis

 Asclepios AI: Predictive Core & Twin-Engine Architecture

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
