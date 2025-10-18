# 📊 Datasets: Guide

This folder is dedicated to storing all **datasets** used in the Asclepios
 AI project — an AI-powered platform designed to predict optimal treatment
  duration and prevent costly readmissions for patients undergoing Substance
   Use Disorder (SUD) treatment.

---

## 🧠 Purpose

To ensure **reproducibility** and **data transparency**, all raw datasets should
 be stored here exactly as downloaded. You may clean, preprocess, or enrich
  them, but **never overwrite or modify the originals**.

---

## 🗂️ Folder Structure Example

```/datasets
│
├── raw/
│   ├── teds_treatment_episodes.raw.csv
│   ├── nsduh_substance_use.raw.csv
│
├── processed/
│   ├── cleaned_treatment_data.csv
│   ├── patient_predictions_ready.csv
│
└── README.md
```

---

## 📑 Dataset Documentation

### 1. SAMHSA Treatment Episode Dataset (TEDS)

- **Source:** [SAMHSA.gov Data Portal](https://www.samhsa.gov/data/data-we-collect/teds-treatment-episode-data-set)
- **Description:** National data system on admissions to and discharges from
 substance abuse treatment facilities.
- **Data Type:** Structured (Tabular)
- **Format:** CSV
- **Use in Project:** Train model to predict optimal treatment duration and
 readmission risk.

### 2. UCI Drug Consumption Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29)
- **Description:** Self-reported data on drug consumption and related
 demographic variables.
- **Data Type:** Structured (Tabular)
- **Format:** CSV
- **Use in Project:** Explore correlation between demographics, personality
 traits, and substance use patterns.

### 3. National Survey on Drug Use and Health (NSDUH)

- **Source:** [SAMHSA Data Files](https://www.datafiles.samhsa.gov/)
- **Description:** Annual survey on the use of tobacco, alcohol, illicit drugs,
 and mental health in the U.S.
- **Data Type:** Structured (Tabular, Time Series)
- **Format:** CSV / XLSX
- **Use in Project:** Feature engineering for population-level risk prediction
 and treatment outcome benchmarking.

### 4. Synthetic Treatment Dataset

- **Source:** Generated using [Synthetic Data Vault (SDV)](https://sdv.dev/)
 or [YData Synthetic](https://ydata.ai/products/ydata-synthetic)
- **Description:** Artificial patient-level data simulating real clinical
 treatment records.
- **Data Type:** Structured (Tabular)
- **Format:** CSV / SQLite
- **Use in Project:** Model testing, EDA, and algorithm benchmarking when real
 data is restricted.

---

## 📘 Types of Datasets

### **Classification by Data Type**

| Type | Description | Example |
|------|--------------|----------|
| Continuous | Can take any real value | Blood pressure, time in treatment |
| Discrete | Countable quantities | Number of therapy sessions |
| Nominal | Categories without order | Gender, facility name |
| Ordinal | Ordered categories | Treatment stage (early, mid, late) |
| Binary | Two possible outcomes | Readmission (yes/no) |
| Time Series | Sequential data over time | Patient recovery progress |

---

### **Classification by Structure**

- **Structured Data:** CSV, Excel, SQL tables  
- **Semi-Structured Data:** JSON, XML (EHRs)  
- **Unstructured Data:** Clinical notes, text summaries

---

### **Classification by Collection Method**

- **Primary Data:** Collected directly through surveys or treatment centers  
- **Secondary Data:** Published datasets (e.g., TEDS, NSDUH)  
- **Synthetic Data:** Generated for simulation and model testing  
- **Observational Data:** Real-world treatment outcomes  
- **Experimental Data:** Controlled clinical trials

---

### **Classification by Size and Complexity**

- **Small Data:** Patient-level samples (< 10k rows)
- **Big Data:** Aggregated health records (> 1M rows)
- **High-Dimensional:** Many features (psychological, behavioral, demographic variables)

---

### **Classification by Access Type**

| Type | Access | Example |
|------|---------|----------|
| Public | Freely available | UCI, SAMHSA datasets |
| Private | Restricted | Hospital records |
| Proprietary | Paid / Licensed | Clinical research databases |

---

### **Classification by Purpose**

- **Transactional:** Treatment logs, appointments  
- **Analytical:** Aggregated outcome metrics  
- **Master:** Patient demographics, facility info  
- **Metadata:** Dataset descriptions, schema info  

---

### **Classification by Format**

| Format | Description | Example |
|---------|-------------|----------|
| CSV / XLSX | Tabular | patient_data.csv |
| JSON | Semi-structured | patient_record.json |
| SQLite | Lightweight DB | treatment.db |
| GeoJSON | Spatial | facility_locations.geojson |
| Time Series | Temporal | relapse_trends.csv |

---

## 🔍 Data Quality Checklist

- **Completeness:** Handle missing values carefully  
- **Accuracy:** Validate entries, detect outliers  
- **Consistency:** Ensure logical coherence  
- **Timeliness:** Prefer recent and updated data  
- **Ethics:** Anonymize sensitive patient information  

---

## ⚖️ Ethical Considerations

- Respect patient privacy (HIPAA, GDPR compliance)  
- Avoid bias in model training (gender, race, socioeconomic)  
- Use transparent methods and cite data sources properly  
- Provide opt-out or anonymization mechanisms for sensitive data  

---

## 🧩 Example Dataset Naming Conventions

| Type | Example Name |
|------|---------------|
| Raw | `treatment_records.raw.csv` |
| Cleaned | `treatment_records.cleaned.csv` |
| Processed | `patient_outcomes_model_ready.csv` |
| Synthetic | `synthetic_patient_data.csv` |

---

### 🧷 Notes

This dataset documentation ensures anyone can **clone, replicate, and validate**
 your results with minimal effort. Always keep your **data lineage**
  (raw → cleaned → processed) clear and traceable.

---
© 2025 Asclepios AI — All Rights Reserved.
