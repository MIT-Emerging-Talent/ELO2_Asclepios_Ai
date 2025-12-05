# **Asclepios AI: Data-Driven Treatment Optimization for Substance Use Disorder (SUD)**

Asclepios AI is a data-driven exploration into how machine learning,
domain knowledge, and thoughtful analysis can help improve outcomes for
individuals undergoing Substance Use Disorder (SUD) treatment. Using real
admissions and treatment episode data, our goal is to identify patterns
that can help facilities personalize treatment duration, improve completion
rates, and reduce relapse/readmission.

## Our Team

This project is being developed by a collaborative team:

- **Caesar Ghazi** ([@CaesarGhazi](https://github.com/CaesarGhazi))
- **Moe Alwathiq** ([Moe-phantom](https://github.com/Moe-phantom))
- **Rafaa Ali** ([@RafaaAli](https://github.com/RafaaAli))
- **Wuor Bhang** ([@WuorBhang](https://github.com/WuorBhang))

## **Primary Research Question**

How accurately can patient demographics, history, and treatment factors
predict an optimal treatment duration that minimizes relapse risk in Substance
Use Disorder treatment?

## Problem Statement

Despite the critical importance of completing adequate treatment for
sustained recovery, SUD facilities lack systematic approaches to personalizing
treatment length based on patient characteristics and predicted outcomes.
Approximately **30% of patients are readmitted within one year**, suggesting
many individuals either receive insufficient treatment or discontinue prematurely.

At the same time, treatment facilities struggle with capacity planning. They
often cannot effectively match the timing and volume of new admissions with
available beds and staff. This mismatch leads to under-used treatment slots,
prolonged waitlists, and reduced access to care.

Asclepios AI aims to use data-driven insights to address these challenges.

## What We're Building

We're creating a smart system that helps treatment centers:

- Predict how long each patient needs treatment for the best chance of recovery
- Reduce the number of patients who return after treatment (readmissions)
- Make the most of their available resources (beds, staff, time)

Think of it like a personalized recommendation system - just like how Netflix
recommends movies you might like, our system recommends the optimal treatment
plan for each patient based on their unique situation.

## Why This Matters

Substance use disorders affect millions of people worldwide and cost society
billions of dollars each year. Unfortunately:

- About 30% of patients return to treatment within a year
- Treatment facilities struggle to match the right treatment length to each
  patient
- Resources are often wasted or underused due to poor planning

Our AI system aims to solve these problems by using data to make better
predictions about what each patient needs.

## Data Overview

We use publicly available SUD admissions and treatment episode datasets,
which include variables such as:

- Patient demographics
- Substance use patterns
- Co-occurring issues
- Treatment history
- Treatment length
- Completion status
- Readmission / relapse factors

### Repository Data Folders

- 📁 **Raw Data:** [`1_datasets/raw/`](./1_datasets/raw/)
- 📁 **Processed Data:** [`1_datasets/processed/`](./1_datasets/processed/)
- 📁 **Sample Data:** [`1_datasets/sample/`](./1_datasets/sample/)
- 📄 **Data Documentation:** [`1_datasets/README.md`](./1_datasets/README.md)

---

## Data Preparation

This step includes:

- Cleaning and formatting raw datasets
- Handling missing or inconsistent data
- Encoding categorical variables
- Normalizing and transforming features
- Structuring datasets for modeling

📁 Folder:
 **[`2_data_preparation/`](./2_data_preparation/)**

---

## Exploratory Data Analysis (EDA)

We explore:

- Relationships between treatment factors and outcomes
- Duration patterns across substance types
- Demographic and behavioral trends
- Variables most correlated with relapse or completion
- Facility-level patterns affecting patient success

📁 Folder:
 **[`3_data_exploration/`](./3_data_exploration/)**

---

## Modeling & Analysis

We will build models to:

- Predict relapse likelihood
- Identify high-risk patients
- Predict facility resource demand
- Evaluate model fairness and robustness

Analysis includes:

- Feature engineering
- Training and validation
- Model comparison
- Interpretability

📁 Folder:
 **[`4_data_analysis/`](./4_data_analysis/)**

---

## Communicating Results

Our communication will include:

- Insight summaries
- Visual dashboards or graphs
- Interpretations for clinicians and decision-makers
- Recommendations based on model findings
- Limitations and ethical considerations

📁 Folder:
 **[`5_communication_strategy/`](./5_communication_strategy/)**

---

## Final Presentation

Our final deliverables will recap the entire analysis with:

- A structured summary of findings
- Visualizations
- Model results
- Recommendations for treatment facilities
- Reflections and next steps

📁 Folder:
 **[`6_final_presentation/`](./6_final_presentation/)**

---

## Repository Structure

Below is the full layout of the project repository:

```text
Asclepios_Ai/
│
├── 0_domain_study/
├── 1_datasets/
│   ├── processed/
│   ├── sample/
│   └── raw/
├── 2_data_preparation/
├── 3_data_exploration/
├── 4_data_analysis/
├── 5_communication_strategy/
└── 6_final_presentation/
```

### License

This project is licensed under the **MIT License**.
📄 [View License](./LICENSE)
