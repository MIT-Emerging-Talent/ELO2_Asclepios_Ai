# 🏥 Asclepios Treatment Intelligence

## AI-Powered Substance Use Treatment Prediction App

Built with **Streamlit**, **Plotly**, **Pandas**, and **Joblib**

------------------------------------------------------------------------

## 📌 Overview

The **Asclepios Treatment Intelligence** app is an interactive Streamlit
application designed to provide AI-driven predictions for substance-use
treatment patients.

The system loads pre-trained ML models (High-Risk Prediction +
Length-of-Stay Predictors) and generates:

- High-risk admission likelihood
- Detox length-of-stay (LOS) prediction
- Rehab length-of-stay (LOS) prediction
- Patient risk insights & feature-engineered scores
- Interactive UI with professional medical-themed styling

This application is ideal for clinical researchers, treatment
facilities, and data-science practitioners exploring applied predictive
healthcare analytics.

------------------------------------------------------------------------

## 🚀 Key Features

### 🔮 Predictive Modeling

- High-risk treatment prediction
- Estimated Length-of-Stay (Detox + Rehab)
- Advanced feature engineering:
- Years using substance
- SDOH Score
- Risk synergy indicators
- Acuity scoring
- Legal mandate flag
- MAT (methadone) maintenance flag

### 🎨 Custom UI/UX

- Fully customized Streamlit theme
- Styled headers, cards, tabs, buttons
- Sidebar navigation
- Risk badges & visual cues
- Gradient backgrounds and shadow effects

------------------------------------------------------------------------

## 🧠 Model Architecture

The application loads saved models via:

    ../models/model_high_risk.pkl
    ../models/asclepios_los_detox.pkl
    ../models/asclepios_los_rehab.pkl
    ../models/model_features_high_risk.pkl
    ../models/model_features_los.pkl

------------------------------------------------------------------------

## 📁 Project Structure

    5_communication_strategy/
    |
    |── Streamlit/
    │     ├── app.py                    # Streamlit app
    │── models/
    │     ├── model_high_risk.pkl
    │     ├── asclepios_los_detox.pkl
    │     ├── asclepios_los_rehab.pkl
    │     ├── model_features_high_risk.pkl
    │     └── model_features_los.pkl
    │── README.md

------------------------------------------------------------------------

## 🧩 How It Works

### 1️⃣ Model Loading

The app uses `@st.cache_resource` to efficiently load trained models:

<!-- markdownlint-disable-next-line MD046 -->
```python
models = {
    "high risk": joblib.load("../models/model_high_risk.pkl"),
    "detox los": joblib.load("../models/asclepios_los_detox.pkl"),
    "rehab los": joblib.load("../models/asclepios_los_rehab.pkl"),
    "features high risk": joblib.load("../models/model_features_high_risk.pkl"),
    "features los": joblib.load("../models/model_features_los.pkl"),
}
```

### 2️⃣ Feature Engineering

The app builds clinical-grade engineered features, including:

- Years_Using_Substance
- SDOH_Score
- Risk synergy features
- Acuity scoring
- MAT maintenance
- Legal mandate flag

These are dynamically computed from user inputs.

### 3️⃣ Prediction Workflow

The `render_prediction_interface()` function:

- Collects patient inputs via Streamlit UI
- Generates patient profile badges
- Builds a prediction dataframe
- Runs ML models
- Displays results with styled metrics and insight cards

------------------------------------------------------------------------

## 🖼️ User Interface Modules

### 🎯 Patient Predictions

Main interactive page:

- Demographics
- Clinical input
- Substance history
- Social factors
- Prediction results

### 📊 Model Insights

***displays analytic charts or model information***
[![Screenshot-from-2025-12-08-20-22-37.png](https://i.postimg.cc/4dc6f6HD/Screenshot-from-2025-12-08-20-22-37.png)](https://postimg.cc/ph2hknZC)


### 📚 About

Project description and usage details.

------------------------------------------------------------------------

## 🛠️ Installation & Run

### 1. Install dependencies

<!-- markdownlint-disable-next-line MD046 -->
``` bash
pip install streamlit pandas plotly joblib
```

### 2. Run the app

<!-- markdownlint-disable-next-line MD046 -->
``` bash
streamlit run app.py
```

Ensure the `models/` directory exists and contains the `.pkl` model
files.

------------------------------------------------------------------------

## 🧪 Model Inputs Used

### Demographics

- Age
- Sex
- Race
- Education
- Marital Status

### Clinical Factors

- Treatment Service Type
- Psychiatric Problems
- Methadone Usage
- Primary Substance + Route + Frequency

### Substance History

- Age First Use
- Secondary/Tertiary Substances
- Prior Treatments
- DSM Criteria

### Social Determinants

- Employment
- Living Conditions
- Arrests
- Referral Source
- State FIPS
- Insurance

------------------------------------------------------------------------

## 🎨 Custom Styling

The app uses **200+ lines of handcrafted CSS** to transform Streamlit UI
components:

- Cards
- Buttons
- Tabs
- Metrics
- Badges
- Progress bars
- Sidebar
- Input fields

Brand colors used:

    #764e7e
    #1A2A4F
    #F87B1B
    #F7A5A5

------------------------------------------------------------------------

## 📜 License

This project is for **research and educational purposes**.\
Modify freely but ensure dataset and model usage comply with privacy and
ethical guidelines.

------------------------------------------------------------------------

## 👨‍💻 Author

**Bhang (Wuor Bhang)**\
**Rafaa Ali**\
**Caesar Ghazi**\
**Moe Alwathiq**

MIT Emerging Talent • Data Scientist\
AI/ML Healthcare & Treatment Analytics Researcher
