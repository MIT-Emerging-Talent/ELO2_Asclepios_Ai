# Domain Research
# Recovery Duration Optimizer — Asclepios AI (SUD Treatment Predictive Analytics)

Asclepios AI helps SUD facilities predict optimal treatment duration, reduce readmissions, and maximize clinician efficiency — shifting care from reactive relapse management to proactive recovery planning.

---

## Purpose
This repository collects research, datasets, notes, and implementation ideas for building data-driven tools that support treatment planning for Substance Use Disorder (SUD). The focus is on models and operational designs that recommend individualized treatment duration, estimate relapse risk, and improve clinical throughput while attending to fairness, safety, and policy constraints.

---

## Scope
- Predictive modeling for time-to-relapse and optimal treatment length
- Survival analysis, time-to-event modeling, and risk scoring
- Reinforcement learning and decision policies for treatment planning
- Feature engineering that includes clinical, social-determinant, and system-level signals
- Fairness, privacy, and ethical evaluation of clinical models
- Cost and workforce efficiency modeling for program design

---

## High-value Datasets & Sources
- SAMHSA — Treatment Episode Data Set (TEDS): https://www.samhsa.gov/data/data-we-collect/teds/datafiles  
- NSDUH — National Survey on Drug Use and Health: https://www.samhsa.gov/data/data-we-collect/nsduh/datafiles  
- CDC WONDER — Mortality & overdose: https://wonder.cdc.gov/  
- Medicaid State Drug Utilization & CMS behavioral health resources: https://www.cms.gov/  
- RAND OPTIC, NIH HEAL, NIDA resources for policy and outcome context

---

## Methods & Tools
- Survival analysis: Kaplan–Meier, Cox PH, AFT models (lifelines, scikit-survival)  
- Gradient-boosted survival models: XGBoost AFT and survival objectives  
- Reinforcement learning for sequential decision-making (Stable-Baselines3, custom simulators)  
- Explainability & fairness: SHAP, Fairlearn, group calibration and counterfactual checks  
- Infrastructure: Python, Jupyter, ML workflow tooling (MLflow, DVC), secure data handling practices (de-identification, controlled access)

---

## Recommended Reading (starter list)
- “Predicting Relapse in Substance Use Disorder: Machine Learning Approaches” — Frontiers in Psychiatry (2021)  
- “Reinforcement Learning for Treatment Planning” — Nature Medicine (2022)  
- “Fairness in Machine Learning Models for Health Data” — JAMA Network (2023)  
- Lifelines and scikit-survival documentation for survival methods

---

## Quick start for new contributors
1. Review datasets referenced above and note licensing/access requirements.  
2. Read the notebooks in /notes/ and experiments in /papers/ to learn prior approaches.  
3. Start with a survival baseline (Kaplan–Meier + Cox PH) on a cleaned dataset to establish time-to-relapse baselines.  
4. Iterate with uplift/individualized treatment-duration modeling and include fairness audits for protected groups.  
5. Document all experiments and model decisions in /notes/ and track artifacts with MLflow or DVC.

---

## Folder structure
/0_domain_study
- README.md                # This file
- papers/                  # Collected research PDFs and summaries
- datasets/                # Dataset links, access notes, ingestion scripts
- notes/                   # Readme-driven summaries, experiment notes, notebooks
- web_links.txt            # Additional URLs and bookmarks

---

## Ethics, Privacy & Governance
- Prioritize de-identification and minimum necessary data access.  
- Perform subgroup fairness and calibration checks before any clinical deployment.  
- Engage clinical stakeholders and IRBs for study design and prospective validation.  
- Maintain an audit trail for model changes and decisions that could affect care.

---

## Maintainer
Wuor Bhang — Asclepios AI  
Date: October 18, 2025
