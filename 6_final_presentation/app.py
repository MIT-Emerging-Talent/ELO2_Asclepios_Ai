# clinical_dashboard_fixed.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="TEDS Clinical Intelligence Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional healthcare appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        color: #1a5276;
        font-weight: 700;
        margin-bottom: 1rem;
        border-bottom: 3px solid #2e86ab;
        padding-bottom: 0.5rem;
    }
    .section-header {
        font-size: 1.6rem;
        color: #2e86ab;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-left: 1rem;
        border-left: 4px solid #2e86ab;
    }
    .metric-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2e86ab;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #ffc107;
    }
    .success-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #0dcaf0;
    }
    .clinical-insight {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #1976d2;
    }
</style>
""", unsafe_allow_html=True)

class ClinicalDashboard:
    def __init__(self):
        self.data = None
        self.engineered_features = [
            'age_group', 'sex', 'race', 'ethnicity', 'education_level', 'employment_status',
            'primary_substance', 'secondary_substance', 'has_mental_health_disorder', 
            'is_polysubstance', 'is_injection_user', 'is_homeless', 'is_veteran',
            'has_criminal_justice_involvement', 'complexity_score', 'completed_treatment',
            'los_category', 'discharge_reason'
        ]
        
    def load_data(self):
        """Load processed TEDS data"""
        try:
            self.data = pd.read_csv("1_datasets/processed/tedsd_ml_clean.csv")
            st.success(f"✅ Clinical data loaded: {self.data.shape[0]:,} patients, {self.data.shape[1]:,} variables")
            
            # Show data structure
            st.sidebar.info(f"📊 **Data Overview:** {self.data.shape[0]:,} patients, {self.data.shape[1]:,} variables")
            
            return True
        except FileNotFoundError:
            st.error("❌ Processed data not found. Please run the preprocessing pipeline first.")
            return False
    
    def get_available_engineered_features(self):
        """Get list of available engineered features"""
        return [col for col in self.engineered_features if col in self.data.columns]
    
    def create_patient_demographics(self, filtered_df):
        """Analyze patient demographics"""
        st.markdown('<p class="section-header">👥 Patient Demographics</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_patients = len(filtered_df)
            st.metric("Total Patients", f"{total_patients:,}")
        
        with col2:
            if 'AGE' in filtered_df.columns:
                avg_age = filtered_df['AGE'].mean()
                st.metric("Average Age", f"{avg_age:.1f} years")
        
        with col3:
            if 'sex' in filtered_df.columns:
                male_pct = (filtered_df['sex'] == 'Male').mean() * 100
                st.metric("Male Patients", f"{male_pct:.1f}%")
        
        with col4:
            if 'race' in filtered_df.columns:
                race_diversity = filtered_df['race'].nunique()
                st.metric("Race Categories", race_diversity)
        
        # Demographic visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            if 'age_group' in filtered_df.columns:
                age_counts = filtered_df['age_group'].value_counts().sort_index()
                fig = px.bar(x=age_counts.index, y=age_counts.values,
                            title='Age Group Distribution',
                            labels={'x': 'Age Group', 'y': 'Number of Patients'},
                            color_discrete_sequence=['#2e86ab'])
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
            elif 'AGE' in filtered_df.columns:
                fig = px.histogram(filtered_df, x='AGE', 
                                  title='Age Distribution',
                                  nbins=20, color_discrete_sequence=['#2e86ab'])
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'sex' in filtered_df.columns:
                gender_counts = filtered_df['sex'].value_counts()
                fig = px.pie(values=gender_counts.values, 
                            names=gender_counts.index,
                            title='Gender Distribution')
                st.plotly_chart(fig, use_container_width=True)
            elif 'SEX' in filtered_df.columns:
                gender_map = {1: 'Male', 2: 'Female'}
                gender_data = filtered_df['SEX'].map(gender_map).fillna('Unknown')
                fig = px.pie(values=gender_data.value_counts().values,
                            names=gender_data.value_counts().index,
                            title='Gender Distribution')
                st.plotly_chart(fig, use_container_width=True)
        
        # Additional demographics
        col1, col2 = st.columns(2)
        
        with col1:
            if 'race' in filtered_df.columns:
                race_counts = filtered_df['race'].value_counts().head(10)
                fig = px.bar(x=race_counts.values, y=race_counts.index,
                            title='Race Distribution (Top 10)',
                            orientation='h',
                            color_discrete_sequence=['#3498db'])
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'education_level' in filtered_df.columns:
                educ_counts = filtered_df['education_level'].value_counts()
                fig = px.pie(values=educ_counts.values, 
                            names=educ_counts.index,
                            title='Education Level Distribution')
                st.plotly_chart(fig, use_container_width=True)
    
    def create_substance_use_analysis(self, filtered_df):
        """Analyze substance use patterns"""
        st.markdown('<p class="section-header">💊 Substance Use Patterns</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Substance prevalence metrics
        with col1:
            if 'primary_substance' in filtered_df.columns:
                top_substance = filtered_df['primary_substance'].value_counts().index[0]
                st.metric("Most Common Substance", top_substance)
        
        with col2:
            if 'is_polysubstance' in filtered_df.columns:
                polysubstance_rate = filtered_df['is_polysubstance'].mean() * 100
                st.metric("Polysubstance Use", f"{polysubstance_rate:.1f}%")
        
        with col3:
            if 'is_injection_user' in filtered_df.columns:
                injection_rate = filtered_df['is_injection_user'].mean() * 100
                st.metric("Injection Drug Use", f"{injection_rate:.1f}%")
        
        with col4:
            if 'ALCFLG' in filtered_df.columns:
                alcohol_rate = filtered_df['ALCFLG'].mean() * 100
                st.metric("Alcohol Use", f"{alcohol_rate:.1f}%")
        
        # Substance visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            if 'primary_substance' in filtered_df.columns:
                substance_counts = filtered_df['primary_substance'].value_counts().head(10)
                fig = px.pie(values=substance_counts.values, 
                            names=substance_counts.index,
                            title='Top 10 Primary Substances')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Substance flags analysis
            substance_flags = ['ALCFLG', 'COKEFLG', 'MARFLG', 'HERFLG', 'METHFLG', 'OPSYNFLG']
            available_flags = [flag for flag in substance_flags if flag in filtered_df.columns]
            
            if available_flags:
                flag_prevalence = {}
                for flag in available_flags:
                    substance_name = flag.replace('FLG', '').title()
                    flag_prevalence[substance_name] = filtered_df[flag].mean() * 100
                
                prev_df = pd.DataFrame({
                    'Substance': list(flag_prevalence.keys()),
                    'Prevalence (%)': list(flag_prevalence.values())
                }).sort_values('Prevalence (%)', ascending=True)
                
                fig = px.bar(prev_df, y='Substance', x='Prevalence (%)',
                            title='Substance Use Prevalence by Type',
                            color='Prevalence (%)', 
                            color_continuous_scale='Reds')
                st.plotly_chart(fig, use_container_width=True)
        
        # Substance by demographics
        if 'primary_substance' in filtered_df.columns and 'age_group' in filtered_df.columns:
            st.subheader("Substance Use by Age Group")
            pivot_data = pd.crosstab(filtered_df['age_group'], filtered_df['primary_substance'], 
                                    normalize='index') * 100
            
            # Get top 5 substances
            top_substances = filtered_df['primary_substance'].value_counts().head(5).index
            pivot_top = pivot_data[top_substances]
            
            fig = px.imshow(pivot_top, aspect="auto",
                           title="Substance Prevalence by Age Group (%)",
                           color_continuous_scale="Blues")
            st.plotly_chart(fig, use_container_width=True)
    
    def create_clinical_complexity_analysis(self, filtered_df):
        """Analyze clinical complexity"""
        st.markdown('<p class="section-header">🏥 Clinical Complexity Analysis</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if 'complexity_score' in filtered_df.columns:
                avg_complexity = filtered_df['complexity_score'].mean()
                st.metric("Average Complexity", f"{avg_complexity:.2f}")
        
        with col2:
            if 'complexity_score' in filtered_df.columns:
                high_complexity = (filtered_df['complexity_score'] > 5).mean() * 100
                st.metric("High Complexity Patients", f"{high_complexity:.1f}%")
        
        with col3:
            if 'has_mental_health_disorder' in filtered_df.columns:
                mental_health_rate = filtered_df['has_mental_health_disorder'].mean() * 100
                st.metric("Mental Health Disorders", f"{mental_health_rate:.1f}%")
        
        with col4:
            if 'is_homeless' in filtered_df.columns:
                homelessness_rate = filtered_df['is_homeless'].mean() * 100
                st.metric("Homelessness", f"{homelessness_rate:.1f}%")
        
        # Complexity visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            if 'complexity_score' in filtered_df.columns:
                fig = px.histogram(filtered_df, x='complexity_score',
                                  title='Clinical Complexity Distribution',
                                  nbins=30, color_discrete_sequence=['#2e86ab'])
                fig.add_vline(x=filtered_df['complexity_score'].mean(), 
                             line_dash="dash", line_color="red",
                             annotation_text=f"Mean: {filtered_df['complexity_score'].mean():.2f}")
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Complexity drivers
            drivers = {}
            if 'has_mental_health_disorder' in filtered_df.columns:
                drivers['Mental Health'] = filtered_df['has_mental_health_disorder'].mean() * 100
            
            if 'is_polysubstance' in filtered_df.columns:
                drivers['Polysubstance Use'] = filtered_df['is_polysubstance'].mean() * 100
            
            if 'is_homeless' in filtered_df.columns:
                drivers['Homelessness'] = filtered_df['is_homeless'].mean() * 100
            
            if 'is_injection_user' in filtered_df.columns:
                drivers['Injection Drug Use'] = filtered_df['is_injection_user'].mean() * 100
            
            if 'has_criminal_justice_involvement' in filtered_df.columns:
                drivers['Criminal Justice'] = filtered_df['has_criminal_justice_involvement'].mean() * 100
            
            if drivers:
                driver_df = pd.DataFrame({
                    'Factor': list(drivers.keys()),
                    'Prevalence (%)': list(drivers.values())
                }).sort_values('Prevalence (%)', ascending=True)
                
                fig = px.bar(driver_df, y='Factor', x='Prevalence (%)',
                            title='Complexity Driver Prevalence',
                            color='Prevalence (%)',
                            color_continuous_scale='Blues')
                st.plotly_chart(fig, use_container_width=True)
        
        # Complexity by demographics
        if 'complexity_score' in filtered_df.columns and 'age_group' in filtered_df.columns:
            st.subheader("Complexity Score by Age Group")
            complexity_by_age = filtered_df.groupby('age_group')['complexity_score'].mean().sort_index()
            
            fig = px.bar(x=complexity_by_age.index, y=complexity_by_age.values,
                        title='Average Complexity Score by Age Group',
                        labels={'x': 'Age Group', 'y': 'Average Complexity Score'},
                        color_discrete_sequence=['#e74c3c'])
            st.plotly_chart(fig, use_container_width=True)
    
    def create_treatment_outcome_analysis(self, filtered_df):
        """Analyze treatment outcomes - FIXED VERSION without trendline"""
        st.markdown('<p class="section-header">📊 Treatment Outcomes & Effectiveness</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if 'completed_treatment' in filtered_df.columns:
                completion_rate = filtered_df['completed_treatment'].mean() * 100
                st.metric("Treatment Completion", f"{completion_rate:.1f}%")
        
        with col2:
            if 'LOS' in filtered_df.columns:
                avg_los = filtered_df['LOS'].mean()
                st.metric("Average Length of Stay", f"{avg_los:.1f} days")
        
        with col3:
            if 'NOPRIOR' in filtered_df.columns:
                readmission_risk = (filtered_df['NOPRIOR'] > 1).mean() * 100
                st.metric("Readmission Risk", f"{readmission_risk:.1f}%")
        
        with col4:
            if 'DAYWAIT' in filtered_df.columns:
                avg_wait = filtered_df['DAYWAIT'].mean()
                st.metric("Average Wait Time", f"{avg_wait:.1f} days")
        
        # Treatment outcome visualizations - FIXED: No trendline
        col1, col2 = st.columns(2)
        
        with col1:
            if 'LOS' in filtered_df.columns:
                fig = px.box(filtered_df, y='LOS', 
                            title='Length of Stay Distribution')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'completed_treatment' in filtered_df.columns and 'complexity_score' in filtered_df.columns:
                # Create bins for complexity score to show relationship
                filtered_df['complexity_bin'] = pd.cut(filtered_df['complexity_score'], bins=10)
                completion_by_complexity = filtered_df.groupby('complexity_bin')['completed_treatment'].mean().reset_index()
                completion_by_complexity['complexity_mid'] = completion_by_complexity['complexity_bin'].apply(lambda x: x.mid)
                
                fig = px.scatter(completion_by_complexity, x='complexity_mid', y='completed_treatment',
                               title='Treatment Completion vs Patient Complexity',
                               labels={'complexity_mid': 'Complexity Score (Binned)', 
                                      'completed_treatment': 'Completion Rate'})
                st.plotly_chart(fig, use_container_width=True)
        
        # Service type analysis
        if 'service_type' in filtered_df.columns:
            st.subheader("Treatment Outcomes by Service Type")
            
            outcome_by_service = filtered_df.groupby('service_type').agg({
                'completed_treatment': 'mean',
                'complexity_score': 'mean',
                'LOS': 'mean'
            }).round(3)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Completion Rate', 
                                x=outcome_by_service.index,
                                y=outcome_by_service['completed_treatment']*100,
                                marker_color='#27ae60'))
            fig.add_trace(go.Scatter(name='Complexity Score', 
                                   x=outcome_by_service.index,
                                   y=outcome_by_service['complexity_score']*20,  # Scale for visibility
                                   mode='lines+markers',
                                   line=dict(color='#e74c3c', width=3),
                                   yaxis='y2'))
            
            fig.update_layout(
                title='Treatment Outcomes by Service Type',
                xaxis_title='Service Type',
                yaxis=dict(title='Completion Rate (%)'),
                yaxis2=dict(title='Complexity Score', overlaying='y', side='right'),
                showlegend=True
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def create_high_risk_identification(self, filtered_df):
        """Identify high-risk patients"""
        st.markdown('<p class="section-header">🎯 High-Risk Patient Identification</p>', unsafe_allow_html=True)
        
        if 'complexity_score' not in filtered_df.columns:
            st.warning("Complexity score not available for risk assessment")
            return
        
        # Define risk categories
        risk_thresholds = {
            'Very High Risk': filtered_df['complexity_score'].quantile(0.8),
            'High Risk': filtered_df['complexity_score'].quantile(0.6),
            'Moderate Risk': filtered_df['complexity_score'].quantile(0.4)
        }
        
        risk_counts = {
            'Very High Risk': (filtered_df['complexity_score'] >= risk_thresholds['Very High Risk']).sum(),
            'High Risk': ((filtered_df['complexity_score'] >= risk_thresholds['High Risk']) & 
                         (filtered_df['complexity_score'] < risk_thresholds['Very High Risk'])).sum(),
            'Moderate Risk': ((filtered_df['complexity_score'] >= risk_thresholds['Moderate Risk']) & 
                             (filtered_df['complexity_score'] < risk_thresholds['High Risk'])).sum(),
            'Low Risk': (filtered_df['complexity_score'] < risk_thresholds['Moderate Risk']).sum()
        }
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Very High Risk", f"{risk_counts['Very High Risk']:,}", 
                     f"{(risk_counts['Very High Risk']/len(filtered_df))*100:.1f}%")
        with col2:
            st.metric("High Risk", f"{risk_counts['High Risk']:,}", 
                     f"{(risk_counts['High Risk']/len(filtered_df))*100:.1f}%")
        with col3:
            st.metric("Moderate Risk", f"{risk_counts['Moderate Risk']:,}", 
                     f"{(risk_counts['Moderate Risk']/len(filtered_df))*100:.1f}%")
        with col4:
            st.metric("Low Risk", f"{risk_counts['Low Risk']:,}", 
                     f"{(risk_counts['Low Risk']/len(filtered_df))*100:.1f}%")
        
        # High-risk patient profile
        high_risk_df = filtered_df[filtered_df['complexity_score'] >= risk_thresholds['High Risk']]
        
        if len(high_risk_df) > 0:
            st.subheader("High-Risk Patient Profile")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Demographic Characteristics:**")
                if 'age_group' in high_risk_df.columns:
                    common_age = high_risk_df['age_group'].mode()[0]
                    st.write(f"- Most common age group: {common_age}")
                
                if 'sex' in high_risk_df.columns:
                    gender_dist = high_risk_df['sex'].value_counts(normalize=True).head(2)
                    for gender, pct in gender_dist.items():
                        st.write(f"- {gender}: {pct*100:.1f}%")
            
            with col2:
                st.write("**Clinical Characteristics:**")
                if 'has_mental_health_disorder' in high_risk_df.columns:
                    mental_health_pct = high_risk_df['has_mental_health_disorder'].mean() * 100
                    st.write(f"- Mental health disorders: {mental_health_pct:.1f}%")
                
                if 'is_polysubstance' in high_risk_df.columns:
                    polysubstance_pct = high_risk_df['is_polysubstance'].mean() * 100
                    st.write(f"- Polysubstance use: {polysubstance_pct:.1f}%")
                
                if 'is_homeless' in high_risk_df.columns:
                    homeless_pct = high_risk_df['is_homeless'].mean() * 100
                    st.write(f"- Homelessness: {homeless_pct:.1f}%")
    
    def create_clinical_recommendations(self, filtered_df):
        """Generate clinical recommendations"""
        st.markdown('<p class="section-header">💡 Clinical Recommendations & Insights</p>', unsafe_allow_html=True)
        
        # Calculate key metrics
        total_patients = len(filtered_df)
        
        complexity_avg = filtered_df['complexity_score'].mean() if 'complexity_score' in filtered_df.columns else 0
        mental_health_rate = filtered_df['has_mental_health_disorder'].mean() * 100 if 'has_mental_health_disorder' in filtered_df.columns else 0
        polysubstance_rate = filtered_df['is_polysubstance'].mean() * 100 if 'is_polysubstance' in filtered_df.columns else 0
        completion_rate = filtered_df['completed_treatment'].mean() * 100 if 'completed_treatment' in filtered_df.columns else 0
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="clinical-insight">
            <h4>🎯 Targeted Intervention Priorities</h4>
            <ul>
            <li><strong>Integrated Mental Health Services:</strong> {mental_health_rate:.1f}% of patients have co-occurring disorders</li>
            <li><strong>Polysubstance Treatment Protocols:</strong> {polysubstance_rate:.1f}% use multiple substances</li>
            <li><strong>High-Complexity Care Teams:</strong> Average complexity score of {complexity_avg:.1f}</li>
            <li><strong>Continuity of Care Programs:</strong> Treatment completion rate of {completion_rate:.1f}%</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="clinical-insight">
            <h4>🏥 Service Optimization</h4>
            <ul>
            <li>Consider expanding intensive outpatient services for moderate complexity patients</li>
            <li>Develop specialized tracks for opioid and stimulant use disorders</li>
            <li>Implement stepped care approaches based on complexity scores</li>
            <li>Enhance discharge planning for patients with high readmission risk</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="clinical-insight">
            <h4>📊 Quality Improvement Focus</h4>
            <ul>
            <li>Monitor length of stay variations across complexity levels</li>
            <li>Track outcomes for patients with mental health comorbidities</li>
            <li>Evaluate effectiveness of different service types for specific substance groups</li>
            <li>Develop early warning systems for treatment non-completion</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="clinical-insight">
            <h4>🔬 Clinical Research Opportunities</h4>
            <ul>
            <li>Study factors associated with successful treatment completion</li>
            <li>Investigate optimal treatment duration for different complexity levels</li>
            <li>Explore personalized medicine approaches based on patient profiles</li>
            <li>Evaluate cost-effectiveness of different intervention strategies</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

def main():
    # Initialize dashboard
    dashboard = ClinicalDashboard()
    
    # Header
    st.markdown('<p class="main-header">🏥 TEDS Clinical Intelligence Dashboard</p>', unsafe_allow_html=True)
    st.markdown("**Data-Driven Insights for Substance Use Treatment Optimization**")
    
    # Load data
    if not dashboard.load_data():
        st.stop()
    
    # Show available features
    available_features = dashboard.get_available_engineered_features()
    st.sidebar.markdown("### 🎯 Available Clinical Features")
    st.sidebar.write(f"**Engineered Features:** {len(available_features)}")
    for feature in available_features:
        st.sidebar.write(f"• {feature}")
    
    # Sidebar filters
    st.sidebar.header("🔍 Clinical Filters")
    
    # Age group filter
    if 'age_group' in dashboard.data.columns:
        age_groups = sorted(dashboard.data['age_group'].unique())
        selected_ages = st.sidebar.multiselect(
            "Age Groups",
            options=age_groups,
            default=age_groups
        )
    else:
        selected_ages = []
    
    # Gender filter
    if 'sex' in dashboard.data.columns:
        genders = sorted(dashboard.data['sex'].unique())
        selected_genders = st.sidebar.multiselect(
            "Gender",
            options=genders,
            default=genders
        )
    else:
        selected_genders = []
    
    # Complexity score filter
    if 'complexity_score' in dashboard.data.columns:
        min_complexity, max_complexity = st.sidebar.slider(
            "Complexity Score Range",
            min_value=float(dashboard.data['complexity_score'].min()),
            max_value=float(dashboard.data['complexity_score'].max()),
            value=(0.0, float(dashboard.data['complexity_score'].max()))
        )
    else:
        min_complexity, max_complexity = (0, 1)
    
    # Primary substance filter
    if 'primary_substance' in dashboard.data.columns:
        substances = sorted(dashboard.data['primary_substance'].unique())
        selected_substances = st.sidebar.multiselect(
            "Primary Substances",
            options=substances,
            default=substances
        )
    else:
        selected_substances = []
    
    # Apply filters
    filtered_data = dashboard.data.copy()
    
    if selected_ages:
        filtered_data = filtered_data[filtered_data['age_group'].isin(selected_ages)]
    
    if selected_genders:
        filtered_data = filtered_data[filtered_data['sex'].isin(selected_genders)]
    
    if 'complexity_score' in dashboard.data.columns:
        filtered_data = filtered_data[
            (filtered_data['complexity_score'] >= min_complexity) & 
            (filtered_data['complexity_score'] <= max_complexity)
        ]
    
    if selected_substances:
        filtered_data = filtered_data[filtered_data['primary_substance'].isin(selected_substances)]
    
    # Key metrics header
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_patients = len(filtered_data)
        st.metric("Total Patients", f"{total_patients:,}")
    
    with col2:
        if 'complexity_score' in filtered_data.columns:
            avg_complexity = filtered_data['complexity_score'].mean()
            st.metric("Avg Complexity", f"{avg_complexity:.2f}")
        else:
            st.metric("Patients Analyzed", f"{total_patients:,}")
    
    with col3:
        if 'completed_treatment' in filtered_data.columns:
            completion_rate = filtered_data['completed_treatment'].mean() * 100
            st.metric("Completion Rate", f"{completion_rate:.1f}%")
        else:
            st.metric("Data Variables", f"{len(dashboard.data.columns):,}")
    
    with col4:
        if 'has_mental_health_disorder' in filtered_data.columns:
            mental_health_rate = filtered_data['has_mental_health_disorder'].mean() * 100
            st.metric("Mental Health", f"{mental_health_rate:.1f}%")
        else:
            substance_flags = [col for col in dashboard.data.columns if 'FLG' in col]
            st.metric("Substance Types", len(substance_flags))
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Overview", "👥 Demographics", "💊 Substances", "🏥 Clinical", "📊 Treatment", "💡 Insights"
    ])
    
    with tab1:
        st.markdown("""
        <div class="success-box">
        <h4>Welcome to the Clinical Intelligence Dashboard</h4>
        <p>This dashboard provides data-driven insights to support clinical decision-making, 
        resource allocation, and treatment optimization for substance use disorders.</p>
        <p><strong>Key Features Available:</strong></p>
        <ul>
        <li>Patient demographic analysis and profiling</li>
        <li>Substance use patterns and prevalence</li>
        <li>Clinical complexity assessment and risk stratification</li>
        <li>Treatment outcome analysis and effectiveness</li>
        <li>High-risk patient identification</li>
        <li>Evidence-based clinical recommendations</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### 📊 Dataset Overview")
            st.write(f"- **Total Patients:** {len(filtered_data):,}")
            st.write(f"- **Available Variables:** {len(dashboard.data.columns):,}")
            st.write(f"- **Engineered Features:** {len(available_features)}")
            st.write(f"- **Data Quality:** {((1 - dashboard.data.isnull().mean().mean()) * 100):.1f}% complete")
        
        with col2:
            st.write("### 🔍 Available Analyses")
            analyses = [
                "Patient Demographics & Profiles",
                "Substance Use Patterns & Trends", 
                "Clinical Complexity Assessment",
                "Treatment Outcome Analysis",
                "Risk Stratification & Identification",
                "Clinical Recommendations & Insights"
            ]
            for analysis in analyses:
                st.write(f"- {analysis}")
    
    with tab2:
        dashboard.create_patient_demographics(filtered_data)
    
    with tab3:
        dashboard.create_substance_use_analysis(filtered_data)
    
    with tab4:
        dashboard.create_clinical_complexity_analysis(filtered_data)
    
    with tab5:
        dashboard.create_treatment_outcome_analysis(filtered_data)
    
    with tab6:
        dashboard.create_high_risk_identification(filtered_data)
        dashboard.create_clinical_recommendations(filtered_data)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
    <p><strong>Clinical Intelligence Dashboard</strong> | TEDS-D 2023 Data | For Clinical Use Only</p>
    <p>Use these insights to inform treatment planning, resource allocation, and quality improvement initiatives.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    