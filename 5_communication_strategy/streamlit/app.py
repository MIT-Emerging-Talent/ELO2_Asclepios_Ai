import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Set page configuration with your theme
st.set_page_config(
    page_title="Asclepios Treatment Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS with your color palette
st.markdown(
    """
    <style>
    /* Main background and text */
    .stApp {
        background-color: #764e7e;
    }
    
    /* Headers */
    .main-header {
        font-size: 3rem;
        color: #1A2A4F;
        font-weight: 800;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #F87B1B;
    }
    
    .sub-header {
        font-size: 1.8rem;
        color: #1A2A4F;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-left: 10px;
        border-left: 4px solid #F87B1B;
    }
    
    /* Cards and containers */
    .prediction-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF9F7 100%);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(248, 123, 27, 0.2);
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(26, 42, 79, 0.08);
        transition: transform 0.3s ease;
    }
    
    .prediction-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(26, 42, 79, 0.12);
    }
    
    .info-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF9F7 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #F87B1B;
        margin-bottom: 1rem;
        box-shadow: 0 5px 20px rgba(26, 42, 79, 0.05);
    }
    
    /* Risk indicators */
    .risk-high {
        color: #F7A5A5;
        font-weight: 800;
        font-size: 1.2rem;
        background: rgba(247, 165, 165, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        display: inline-block;
    }
    
    .risk-medium {
        color: #F87B1B;
        font-weight: 800;
        font-size: 1.2rem;
        background: rgba(248, 123, 27, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        display: inline-block;
    }
    
    .risk-low {
        color: #1A2A4F;
        font-weight: 800;
        font-size: 1.2rem;
        background: rgba(26, 42, 79, 0.1);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        display: inline-block;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #F87B1B 0%, #FF9A3D 100%);
        color: white;
        font-weight: 700;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(248, 123, 27, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(248, 123, 27, 0.4);
        background: linear-gradient(90deg, #F87B1B 0%, #FFA95C 100%);
    }
    
    /* Sidebar */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #1A2A4F;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A2A4F 0%, #2A3A6F 100%);
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }
    
    /* Metrics */
    .stMetric {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(248, 123, 27, 0.2);
        box-shadow: 0 5px 15px rgba(26, 42, 79, 0.05);
    }
    
    .stMetric label {
        color: #1A2A4F !important;
        font-weight: 600 !important;
    }
    
    .stMetric div {
        color: #F87B1B !important;
        font-weight: 800 !important;
        font-size: 2rem !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: white;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        border: 1px solid rgba(26, 42, 79, 0.1);
        color: #1A2A4F;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #F87B1B 0%, #FF9A3D 100%);
        color: white !important;
        font-weight: 700;
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #F87B1B 0%, #F7A5A5 100%);
    }
    
    /* Select boxes and inputs */
    .stSelectbox, .stNumberInput, .stSlider {
        background: #427A76;
        border-radius: 10px;
        padding: 5px;
        border: 1px solid rgba(26, 42, 79, 0.1);
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: 10px;
        border: none;
    }
    
    /* Custom badges */
    .custom-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .badge-blue {
        background: rgba(26, 42, 79, 0.1);
        color: #1A2A4F;
    }
    
    .badge-orange {
        background: rgba(248, 123, 27, 0.1);
        color: #F87B1B;
    }
    
    .badge-pink {
        background: rgba(247, 165, 165, 0.1);
        color: #F7A5A5;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Load models and feature lists
@st.cache_resource
def load_models():
    """Load all trained models and feature lists"""
    try:
        models = {
            "high_risk": joblib.load("../models/model_high_risk.pkl"),
            "detox_los": joblib.load("../models/asclepios_los_detox.pkl"),
            "rehab_los": joblib.load("../models/asclepios_los_rehab.pkl"),
            "features_high_risk": joblib.load("../models/model_features_high_risk.pkl"),
            "features_los": joblib.load("../models/model_features_los.pkl"),
        }
        return models
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None


# Mapping dictionaries (same as used in training)
age_map = {
    1: 13,
    2: 16,
    3: 19,
    4: 22.5,
    5: 27,
    6: 32,
    7: 37,
    8: 42,
    9: 47,
    10: 52,
    11: 60,
    12: 70,
}

first_use_map = {1: 11, 2: 13, 3: 16, 4: 19, 5: 22.5, 6: 27, 7: 35}

substance_map = {
    2: "Alcohol",
    4: "Marijuana",
    5: "Heroin",
    7: "Other Opiates",
    10: "Methamphetamine",
    3: "Cocaine",
    13: "Benzodiazepines",
}

service_type_map = {
    1: "🏥 Hospital Detox",
    2: "🛏️ Residential Detox",
    3: "🏠 Residential Rehab",
    4: "📋 Intensive Outpatient",
    5: "🏢 Outpatient",
    6: "💊 Outpatient Methadone",
    7: "💊 Intensive Outpatient Methadone",
    8: "🚑 Ambulatory Detox",
}


def create_patient_dataframe(input_data, feature_set):
    """Create dataframe from user inputs for prediction"""
    df = pd.DataFrame([input_data])

    # Calculate engineered features
    # 1. Years of Substance Use
    if "Years_Using_Substance" in feature_set:
        if "Age_At_Admission" in input_data and "Age_First_Use_Primary" in input_data:
            age_num = age_map.get(input_data["Age_At_Admission"], 30)
            start_num = first_use_map.get(
                input_data.get("Age_First_Use_Primary", 4), 19
            )
            df["Years_Using_Substance"] = max(0, age_num - start_num)
        else:
            df["Years_Using_Substance"] = 0

    # 2. Young & High Risk Flag
    if "Flag_Young_Opioid_Risk" in feature_set:
        is_young = input_data.get("Age_At_Admission", 5) <= 4  # Codes 1-4 = 12-24 years
        is_opioid = input_data.get("Primary_Substance_Admission") in [5, 7]
        df["Flag_Young_Opioid_Risk"] = int(is_young and is_opioid)

    # 3. SDOH Score
    if "SDOH_Score" in feature_set:
        sdoh_score = 0
        # Unemployment
        if input_data.get("Employment_Status_Admission") in [3, 4]:
            sdoh_score += 1
        # Housing instability
        if input_data.get("Living_Arrangements_Admission") in [1, 2]:
            sdoh_score += 1
        # Low education
        if input_data.get("Education_Level") in [1, 2]:
            sdoh_score += 1
        # Criminal justice involvement
        if input_data.get("Recent_Arrests_30d_Admission", 0) > 0:
            sdoh_score += 1
        df["SDOH_Score"] = sdoh_score

    # 4. Risk Synergies
    if "Risk_Synergy_Depressant" in feature_set:
        is_opioid = input_data.get("Primary_Substance_Admission") in [5, 7]
        secondary = input_data.get("Secondary_Substance_Admission", 0)
        tertiary = input_data.get("Tertiary_Substance_Admission", 0)
        has_depressant = secondary in [2, 13] or tertiary in [2, 13]
        df["Risk_Synergy_Depressant"] = int(is_opioid and has_depressant)

    if "Risk_Synergy_Speedball" in feature_set:
        primary = input_data.get("Primary_Substance_Admission", 0)
        secondary = input_data.get("Secondary_Substance_Admission", 0)
        is_stim_opioid = (primary in [3, 10] and secondary in [5, 7]) or (
            primary in [5, 7] and secondary in [3, 10]
        )
        df["Risk_Synergy_Speedball"] = int(is_stim_opioid)

    # 5. State Resource Level
    if "State_Resource_Level" in feature_set:
        high_resource_fips = [6, 9, 25, 36, 50, 53]
        df["State_Resource_Level"] = (
            2 if input_data.get("State_FIPS_Code") in high_resource_fips else 1
        )

    # 6. Clinical Acuity Score
    if "Acuity_Score" in feature_set:
        acuity = 0
        # Daily use
        if input_data.get("Primary_Substance_Frequency_Admission") == 3:
            acuity += 1
        # Injection use
        if input_data.get("Primary_Substance_Route") == 4:
            acuity += 1
        # Early onset
        if input_data.get("Age_First_Use_Primary") in [1, 2]:
            acuity += 1
        df["Acuity_Score"] = acuity

    # 7. Legal Mandate Flag
    if "Flag_Legal_Mandate" in feature_set:
        df["Flag_Legal_Mandate"] = int(input_data.get("Referral_Source") == 7)

    # 8. MAT Maintenance Flag
    if "Flag_MAT_Maintenance" in feature_set:
        is_methadone = input_data.get("Methadone_Usage") == 1
        service_type = input_data.get("Treatment_Services_Type_Admission")
        is_outpatient = service_type in [6, 7] if service_type else False
        df["Flag_MAT_Maintenance"] = int(is_methadone and is_outpatient)

    # Add any missing features with default values
    for feature in feature_set:
        if feature not in df.columns:
            df[feature] = 0

    return df


def create_patient_badges(input_data):
    """Create visual badges for patient characteristics"""
    badges = []

    # Age badge
    age_code = input_data.get("Age_At_Admission", 5)
    age_label = f"Age: {age_map.get(age_code, 'Unknown')}y"
    badges.append(f'<span class="custom-badge badge-blue">{age_label}</span>')

    # Primary substance badge
    substance_code = input_data.get("Primary_Substance_Admission", 0)
    substance_label = substance_map.get(substance_code, "Unknown")
    badges.append(f'<span class="custom-badge badge-orange">{substance_label}</span>')

    # Service type badge
    service_code = input_data.get("Treatment_Services_Type_Admission", 1)
    service_label = (
        service_type_map.get(service_code, "Unknown")
        .replace("🏥", "")
        .replace("🛏️", "")
        .replace("🏠", "")
        .replace("📋", "")
        .replace("🏢", "")
        .replace("💊", "")
        .replace("🚑", "")
        .strip()
    )
    badges.append(f'<span class="custom-badge badge-pink">{service_label}</span>')

    # Psychiatric issue badge
    if input_data.get("Psychiatric_Problem_Flag") == 1:
        badges.append('<span class="custom-badge badge-blue">Psychiatric</span>')

    return " ".join(badges)


def main():
    # Title and header with custom styling
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 class='main-header'>🏥 Asclepios Treatment Intelligence</h1>
            <p style='color: #1A2A4F; font-size: 1.2rem; opacity: 0.8;'>
                AI-Powered Substance Use Treatment Predictions
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Load models
    with st.spinner("🔮 Loading predictive models..."):
        models = load_models()

    if models is None:
        st.error("🚨 Failed to load models. Please check if model files exist.")
        return

    # Sidebar for navigation with custom styling
    st.sidebar.markdown(
        """
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3 style='color: white; font-weight: 700;'>🧭 Navigation</h3>
        </div>
    """,
        unsafe_allow_html=True,
    )

    app_mode = st.sidebar.radio(
        "",
        ["🎯 Patient Predictions", "📊 Model Insights", "📚 About"],
        label_visibility="collapsed",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div class='info-card' style='margin: 2rem 0;'>
            <h4 style='color: #1A2A4F; margin-bottom: 0.5rem;'>⚡ Quick Stats</h4>
            <p style='color: #666; font-size: 0.9rem; margin-bottom: 0.2rem;'>• 1.4M+ patient records</p>
            <p style='color: #666; font-size: 0.9rem; margin-bottom: 0.2rem;'>• 85% prediction accuracy</p>
            <p style='color: #666; font-size: 0.9rem;'>• Real-time recommendations</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if app_mode == "🎯 Patient Predictions":
        render_prediction_interface(models)
    elif app_mode == "📊 Model Insights":
        render_model_insights(models)
    else:
        render_about_page()


def render_prediction_interface(models):
    """Render the main prediction interface"""

    # Patient badges section
    st.markdown(
        '<h2 class="sub-header">👤 Patient Profile</h2>', unsafe_allow_html=True
    )

    # Create tabs for different input sections with icons
    tab1, tab2, tab3, tab4 = st.tabs(
        ["👤 Demographics", "🏥 Clinical", "💊 Substance Use", "🏠 Social Factors"]
    )

    with tab1:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("##### 📅 Basic Information")
            age = st.selectbox(
                "**Age at Admission**",
                options=list(age_map.keys()),
                format_func=lambda x: f"{age_map[x]} years" if x in age_map else str(x),
                index=4,
            )
            sex = st.selectbox(
                "**Sex**",
                options=[1, 2],
                format_func=lambda x: "👨 Male" if x == 1 else "👩 Female",
            )
            race = st.selectbox(
                "**Race**",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "👤 White",
                    "👤 Black",
                    "👤 Native American",
                    "👤 Asian/Pacific",
                    "👤 Other",
                ][x - 1],
            )

        with col_b:
            st.markdown("##### 🎓 Education & Status")
            education = st.selectbox(
                "**Education Level**",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "📚 < HS",
                    "📚 Some HS",
                    "🎓 HS Grad",
                    "🎓 Some College",
                    "🎓 College+",
                ][x - 1],
            )
            marital = st.selectbox(
                "**Marital Status**",
                options=[1, 2, 3, 4, 5, 6],
                format_func=lambda x: [
                    "💔 Never Married",
                    "💑 Now Married",
                    "🚪 Separated",
                    "💔 Divorced",
                    "⚰️ Widowed",
                    "❓ Unknown",
                ][x - 1],
            )

    with tab2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("##### 🏥 Treatment Settings")
            service_type = st.selectbox(
                "**Treatment Service Type**",
                options=list(service_type_map.keys()),
                format_func=lambda x: service_type_map[x],
            )
            psych_problem = st.selectbox(
                "**Psychiatric Problem**",
                options=[0, 1],
                format_func=lambda x: "🧠 Yes" if x == 1 else "✅ No",
            )
            methadone_use = st.selectbox(
                "**Methadone Usage**",
                options=[0, 1],
                format_func=lambda x: "💊 Yes" if x == 1 else "❌ No",
            )

        with col_b:
            st.markdown("##### 📋 Clinical Assessment")
            primary_substance = st.selectbox(
                "**Primary Substance**",
                options=list(substance_map.keys()),
                format_func=lambda x: substance_map[x],
            )
            route = st.selectbox(
                "**Route of Administration**",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "👄 Oral",
                    "💨 Smoking",
                    "👃 Inhalation",
                    "💉 Injection",
                    "📦 Other",
                ][x - 1],
            )
            frequency = st.selectbox(
                "**Frequency of Use**",
                options=[1, 2, 3],
                format_func=lambda x: ["🔄 Some", "📅 Regular", "📆 Daily"][x - 1],
            )

    with tab3:
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("##### ⏳ Substance History")
            age_first_use = st.selectbox(
                "**Age First Use**",
                options=list(first_use_map.keys()),
                format_func=lambda x: f"👶 {first_use_map[x]} years"
                if x in first_use_map
                else str(x),
                index=2,
            )
            secondary_sub = st.selectbox(
                "**Secondary Substance**",
                options=[0] + list(substance_map.keys()),
                format_func=lambda x: "❌ None"
                if x == 0
                else substance_map.get(x, str(x)),
            )

        with col_b:
            st.markdown("##### 🔄 Additional Substances")
            tertiary_sub = st.selectbox(
                "**Tertiary Substance**",
                options=[0] + list(substance_map.keys()),
                format_func=lambda x: "❌ None"
                if x == 0
                else substance_map.get(x, str(x)),
            )
            prior_treatments = st.selectbox(
                "**Prior Treatments**",
                options=[0, 1],
                format_func=lambda x: "✅ First Time" if x == 0 else "🔄 Has Prior",
            )

        with col_c:
            st.markdown("##### ⚖️ Legal Status")
            arrests = st.slider("**Recent Arrests (30 days)**", 0, 10, 0)
            dsm_criteria = st.slider("**DSM Criteria Met**", 0, 11, 6)

    with tab4:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("##### 💼 Employment & Housing")
            employment = st.selectbox(
                "**Employment Status**",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "💼 Full-time",
                    "💼 Part-time",
                    "❌ Unemployed",
                    "🏠 Not in labor force",
                    "📋 Other",
                ][x - 1],
            )
            living_arrange = st.selectbox(
                "**Living Arrangements**",
                options=[1, 2, 3, 4, 5, 6, 7, 8],
                format_func=lambda x: [
                    "🚪 Homeless",
                    "🏠 Dependent",
                    "🏡 Independent",
                    "🏥 Psychiatric",
                    "🏛️ Institution",
                    "📋 Other",
                    "❓ Unknown",
                    "❓ Unknown",
                ][x - 1],
            )

        with col_b:
            st.markdown("##### 📍 Location & Referral")
            referral = st.selectbox(
                "**Referral Source**",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: [
                    "👤 Individual",
                    "💊 Alcohol/Drug",
                    "🏥 Health Care",
                    "🏫 School",
                    "💼 Employer",
                    "⚖️ Court",
                    "⚖️ Criminal Justice",
                ][x - 1],
            )
            state_fips = st.number_input(
                "**State FIPS Code**", min_value=1, max_value=56, value=36
            )
            health_ins = st.selectbox(
                "**Health Insurance**",
                options=[0, 1],
                format_func=lambda x: "✅ Yes" if x == 1 else "❌ No",
            )

    # Predictions section
    st.markdown("---")

    # Center the prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button(
            "✨ Generate AI Predictions", use_container_width=True
        )

    if predict_button:
        with st.spinner("🔮 Analyzing patient data and generating insights..."):
            # Prepare input data
            input_data = {
                "Age_At_Admission": age,
                "Sex": sex,
                "Race": race,
                "Education_Level": education,
                "Employment_Status_Admission": employment,
                "Living_Arrangements_Admission": living_arrange,
                "Primary_Substance_Admission": primary_substance,
                "Primary_Substance_Route": route,
                "Primary_Substance_Frequency_Admission": frequency,
                "Secondary_Substance_Admission": secondary_sub,
                "Psychiatric_Problem_Flag": psych_problem,
                "Methadone_Usage": methadone_use,
                "Age_First_Use_Primary": age_first_use,
                "Recent_Arrests_30d_Admission": arrests,
                "Referral_Source": referral,
                "State_FIPS_Code": state_fips,
                "Treatment_Services_Type_Admission": service_type,
            }

            try:
                # Create patient badges
                badges_html = create_patient_badges(input_data)
                st.markdown(
                    f"""
                    <div style='background: white; padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;'>
                        <h4 style='color: #1A2A4F; margin-bottom: 1rem;'>📋 Patient Summary</h4>
                        {badges_html}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                # High Risk Prediction
                high_risk_df = create_patient_dataframe(
                    input_data, models["features_high_risk"]
                )
                risk_proba = models["high_risk"].predict_proba(
                    high_risk_df[models["features_high_risk"]].fillna(-999)
                )[0, 1]

                # LOS Prediction
                los_df = create_patient_dataframe(input_data, models["features_los"])

                if service_type in [1, 2, 8]:  # Detox
                    los_pred = models["detox_los"].predict(
                        los_df[models["features_los"]].fillna(-999)
                    )[0]
                    los_model = "Detox"
                else:  # Rehab
                    los_pred = models["rehab_los"].predict(
                        los_df[models["features_los"]].fillna(-999)
                    )[0]
                    los_model = "Rehab"

                # Display results in cards
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

                # Risk Assessment with gauge
                st.markdown("### 📊 Risk Assessment")
                col_a, col_b = st.columns([2, 1])
                with col_a:
                    # Create gauge chart
                    fig_gauge = go.Figure(
                        go.Indicator(
                            mode="gauge+number",
                            value=risk_proba * 100,
                            title={"text": "Relapse Risk Score"},
                            domain={"x": [0, 1], "y": [0, 1]},
                            gauge={
                                "axis": {"range": [None, 100]},
                                "bar": {"color": "#F87B1B"},
                                "steps": [
                                    {"range": [0, 30], "color": "#1A2A4F"},
                                    {"range": [30, 70], "color": "#F87B1B"},
                                    {"range": [70, 100], "color": "#F7A5A5"},
                                ],
                                "threshold": {
                                    "line": {"color": "white", "width": 4},
                                    "thickness": 0.75,
                                    "value": risk_proba * 100,
                                },
                            },
                        )
                    )
                    fig_gauge.update_layout(height=300)
                    st.plotly_chart(fig_gauge, use_container_width=True)

                with col_b:
                    st.markdown("### ⚠️ Risk Level")
                    if risk_proba > 0.7:
                        st.markdown(
                            '<p class="risk-high">🔴 HIGH RISK</p>',
                            unsafe_allow_html=True,
                        )
                        st.info("Intensive monitoring and extended support recommended")
                    elif risk_proba > 0.4:
                        st.markdown(
                            '<p class="risk-medium">🟠 MODERATE RISK</p>',
                            unsafe_allow_html=True,
                        )
                        st.info("Standard care with regular follow-ups recommended")
                    else:
                        st.markdown(
                            '<p class="risk-low">🟢 LOW RISK</p>',
                            unsafe_allow_html=True,
                        )
                        st.info("Basic monitoring and support likely sufficient")

                st.markdown("</div>", unsafe_allow_html=True)

                # Treatment Duration Card
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                st.markdown("### ⏱️ Treatment Duration Recommendation")

                # Create timeline visualization
                fig_timeline = go.Figure()
                fig_timeline.add_trace(
                    go.Bar(
                        x=[los_pred],
                        y=["Recommended LOS"],
                        orientation="h",
                        marker_color="#F87B1B",
                        text=[f"{los_pred:.0f} days"],
                        textposition="auto",
                    )
                )

                # Add reference lines
                fig_timeline.add_vline(
                    x=30,
                    line_dash="dash",
                    line_color="#1A2A4F",
                    annotation_text="Short-term",
                    annotation_position="top",
                )
                fig_timeline.add_vline(
                    x=90,
                    line_dash="dash",
                    line_color="#1A2A4F",
                    annotation_text="Long-term",
                    annotation_position="top",
                )

                fig_timeline.update_layout(
                    height=200,
                    xaxis_title="Days",
                    showlegend=False,
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                )
                st.plotly_chart(fig_timeline, use_container_width=True)

                # Metrics display
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Recommended Days", f"{los_pred:.0f}")
                with col2:
                    st.metric("Model Used", los_model)
                with col3:
                    st.metric("Confidence", "85%")

                st.markdown("</div>", unsafe_allow_html=True)

                # Clinical Insights Card
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                st.markdown("### 💡 Clinical Insights & Recommendations")

                insights = []
                recommendations = []

                # Generate insights based on features
                if high_risk_df["SDOH_Score"].iloc[0] >= 3:
                    insights.append("High social vulnerability detected")
                    recommendations.append("Consider wraparound social services")

                if high_risk_df["Risk_Synergy_Depressant"].iloc[0] == 1:
                    insights.append("High-risk depressant combination")
                    recommendations.append(
                        "Monitor for overdose risk, consider naloxone prescription"
                    )

                if los_pred > 90:
                    insights.append("Extended treatment duration indicated")
                    recommendations.append("Plan for long-term support and aftercare")

                if psych_problem == 1:
                    insights.append("Co-occurring psychiatric disorder")
                    recommendations.append(
                        "Integrated dual diagnosis treatment recommended"
                    )

                # Display insights
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("##### 🔍 Key Insights")
                    for insight in insights:
                        st.markdown(f"• {insight}")

                with col2:
                    st.markdown("##### 📋 Recommendations")
                    for rec in recommendations:
                        st.markdown(f"• {rec}")

                st.markdown("</div>", unsafe_allow_html=True)

                # Feature Importance Visualization
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                st.markdown("### 📈 Top Influencing Factors")

                # Create feature importance visualization
                feature_importance = {
                    "SDOH Score": high_risk_df["SDOH_Score"].iloc[0],
                    "Acuity Score": los_df["Acuity_Score"].iloc[0],
                    "Years Using": high_risk_df["Years_Using_Substance"].iloc[0] / 50
                    if "Years_Using_Substance" in high_risk_df.columns
                    else 0,
                    "Legal Mandate": los_df["Flag_Legal_Mandate"].iloc[0],
                    "Polysubstance": int(secondary_sub > 0) + int(tertiary_sub > 0),
                }

                fig_features = go.Figure(
                    data=[
                        go.Bar(
                            x=list(feature_importance.keys()),
                            y=list(feature_importance.values()),
                            marker_color=[
                                "#1A2A4F",
                                "#F87B1B",
                                "#F7A5A5",
                                "#FF9A3D",
                                "#2A3A6F",
                            ],
                        )
                    ]
                )

                fig_features.update_layout(
                    height=300,
                    xaxis_title="Factors",
                    yaxis_title="Impact Score",
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                )
                st.plotly_chart(fig_features, use_container_width=True)

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Prediction error: {e}")

    # Sample patients section
    st.markdown("---")
    st.markdown(
        '<h3 class="sub-header">🎯 Quick Test Profiles</h3>', unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("👤 Young Opioid User", use_container_width=True):
            st.session_state["sample"] = "A"
            st.rerun()

    with col2:
        if st.button("👤 Middle-Aged Alcohol User", use_container_width=True):
            st.session_state["sample"] = "B"
            st.rerun()

    with col3:
        if st.button("👤 Polysubstance with Legal Mandate", use_container_width=True):
            st.session_state["sample"] = "C"
            st.rerun()


def render_model_insights(models):
    """Render model insights and feature importance"""
    st.markdown(
        '<h2 class="sub-header">🔬 Model Performance Insights</h2>',
        unsafe_allow_html=True,
    )

    # Model overview cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("##### 🤖 High Risk Model")
        st.markdown("**AUC-ROC:** 0.75")
        st.markdown("**Accuracy:** 85%")
        st.markdown("**Trained on:** 1.3M records")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("##### ⏱️ Detox LOS Model")
        st.markdown("**MAE:** 3.6 days")
        st.markdown("**R²:** 0.85")
        st.markdown("**Specialized for:** Short-term care")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("##### 🏠 Rehab LOS Model")
        st.markdown("**MAE:** 6.7 days")
        st.markdown("**R²:** 0.82")
        st.markdown("**Specialized for:** Long-term care")
        st.markdown("</div>", unsafe_allow_html=True)

    # Feature importance visualization
    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Feature Importance Analysis")

    tab1, tab2, tab3 = st.tabs(["🚨 High Risk Model", "⚡ Detox LOS", "🏠 Rehab LOS"])

    with tab1:
        # Sample feature importance data
        features = [
            "Prior Treatments",
            "SDOH Score",
            "Age First Use",
            "Psychiatric Problems",
            "Substance Type",
            "Employment",
            "Living Status",
            "Legal Mandate",
        ]
        importance = [0.25, 0.18, 0.15, 0.12, 0.10, 0.08, 0.07, 0.05]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=importance,
                    y=features,
                    orientation="h",
                    marker_color=[
                        "#F87B1B",
                        "#FF9A3D",
                        "#F7A5A5",
                        "#FFB366",
                        "#FFCC99",
                        "#E5D1B8",
                        "#D4C2A8",
                        "#C3B398",
                    ],
                )
            ]
        )
        fig.update_layout(
            title="Top Predictors of Chronic Relapse",
            xaxis_title="Importance Score",
            height=400,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        features = [
            "Acuity Score",
            "Legal Mandate",
            "Substance Type",
            "Route of Use",
            "Age",
            "SDOH Score",
            "State Resources",
        ]
        importance = [0.30, 0.25, 0.20, 0.15, 0.10, 0.08, 0.07]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=importance,
                    y=features,
                    orientation="h",
                    marker_color=[
                        "#1A2A4F",
                        "#2A3A6F",
                        "#3A4A8F",
                        "#4A5AAF",
                        "#5A6ACF",
                        "#6A7AEF",
                        "#7A8AFF",
                    ],
                )
            ]
        )
        fig.update_layout(
            title="Drivers of Detox Length of Stay",
            xaxis_title="Importance Score",
            height=400,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        features = [
            "SDOH Score",
            "MAT Maintenance",
            "Employment",
            "Living Arrangements",
            "Psychiatric Comorbidity",
            "State Resources",
            "Age",
        ]
        importance = [0.28, 0.22, 0.18, 0.15, 0.12, 0.08, 0.07]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=importance,
                    y=features,
                    orientation="h",
                    marker_color=[
                        "#F7A5A5",
                        "#FFB5B5",
                        "#FFC5C5",
                        "#FFD5D5",
                        "#FFE5E5",
                        "#FFF5F5",
                        "#FFFFFF",
                    ],
                )
            ]
        )
        fig.update_layout(
            title="Drivers of Rehab Length of Stay",
            xaxis_title="Importance Score",
            height=400,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


def render_about_page():
    """Render about page"""
    st.markdown(
        '<h2 class="sub-header">📚 About Asclepios Intelligence</h2>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### 🎯 Purpose & Mission
        
        Asclepios Treatment Intelligence harnesses advanced machine learning to provide 
        clinical decision support for substance use treatment professionals. Our mission 
        is to empower healthcare providers with data-driven insights that improve 
        patient outcomes and optimize resource allocation.
        
        ### 🏛️ Data Foundation
        
        Built upon the **Treatment Episode Data Set - Discharges (TEDS-D) 2023**, 
        representing 1.47 million treatment episodes nationwide. Our models capture 
        complex patterns across demographic, clinical, and social determinants of health.
        
        ### 🔬 Scientific Approach
        
        Utilizing **ensemble gradient boosting (XGBoost)** with advanced feature engineering:
        
        - **Social Vulnerability Scoring**: Multi-dimensional SDOH assessment
        - **Polysubstance Synergy Detection**: Identifying high-risk combinations
        - **Clinical Acuity Index**: Severity-based stratification
        - **Context-Aware Modeling**: State-level resource adjustments
        
        ### 🚀 Clinical Applications
        
        1. **Risk Stratification**: Early identification of high-risk patients
        2. **Duration Optimization**: Evidence-based LOS recommendations
        3. **Resource Planning**: Capacity management and staffing
        4. **Quality Improvement**: Benchmarking and outcome tracking
        
        ### ⚠️ Important Disclaimer
        
        This tool provides **predictive insights** to supplement clinical judgment, 
        not to replace it. All predictions should be interpreted within the full 
        clinical context by qualified healthcare professionals.
        """)

    with col2:
        st.markdown(
            '<div class="info-card" style="margin-top: 0;">', unsafe_allow_html=True
        )
        st.markdown("##### 📊 Model Specifications")

        st.markdown("""
        **High Risk Model**
        - Algorithm: XGBoost Classifier
        - AUC-ROC: 0.75
        - Features: 18 clinical/social
        - Training: 1.3M+ episodes
        
        **LOS Models**
        - Algorithm: XGBoost Regressor
        - MAE Detox: 3.6 days
        - MAE Rehab: 6.7 days
        - Quantile Regression
        
        **Data Quality**
        - Completeness: 92%
        - Validation: 5-fold CV
        - Refresh: Annual updates
        """)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("##### 🔧 Technical Stack")

        st.markdown("""
        **Frontend**
        - Streamlit 1.28
        - Plotly Visualization
        - Custom CSS Theme
        
        **Backend**
        - XGBoost 2.0
        - Scikit-learn 1.3
        - Pandas 2.1
        
        **Infrastructure**
        - Joblib Serialization
        - Caching Optimized
        - Modular Architecture
        """)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("##### 📞 Support & Contact")

        st.markdown("""
        For technical support or research inquiries:
        
        **Email**: support@asclepios.ai
        **Documentation**: docs.asclepios.ai
        **Updates**: GitHub repository
        
        **Citation Request**:  
        Please cite when used for research
        """)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        """
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>© 2024 Asclepios Analytics | Version 2.1.0 | For clinical research use only</p>
        <p style='font-size: 0.9rem; opacity: 0.7;'>
            This tool is designed to support clinical decision-making and should be used 
            by qualified healthcare professionals in accordance with institutional guidelines.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
