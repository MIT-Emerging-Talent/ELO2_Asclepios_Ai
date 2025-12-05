# models/train_model.py

import warnings

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


def train_and_save_model():
    """Train and save the prediction model"""
    print("🚀 Loading processed data...")

    # Load your processed data
    df = pd.read_csv("1_datasets/processed/teds_d_ml_ready.csv")

    # Define target variable (example: treatment completion)
    target_col = "completed_treatment"

    if target_col not in df.columns:
        # If not available, create a synthetic target for demonstration
        print("⚠️ Target column not found. Creating synthetic target...")
        df[target_col] = np.random.choice([0, 1], size=len(df), p=[0.4, 0.6])

    # Select features - adjust based on your actual columns
    feature_cols = [
        "AGE",
        "SEX",
        "EDUC",
        "EMPLOY",
        "NOPRIOR",
        "ARRESTS",
        "LOS",
        "DAYWAIT",
        "FRSTUSE1",
        "PSYPROB",
        "is_polysubstance",
        "is_injection_user",
        "is_homeless",
        "complexity_score",
    ]

    # Only use existing columns
    existing_features = [col for col in feature_cols if col in df.columns]
    print(f"✅ Using {len(existing_features)} features")

    X = df[existing_features]
    y = df[target_col]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"📊 Dataset: {len(df)} total, {len(X_train)} train, {len(X_test)} test")

    # Train Random Forest model
    print("🤖 Training Random Forest model...")
    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features="sqrt",
        random_state=42,
        class_weight="balanced",
    )

    rf_model.fit(X_train, y_train)

    # Predictions
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

    # Save model
    joblib.dump(rf_model, "models/trained_model.pkl")
    print("💾 Model saved as 'models/trained_model.pkl'")

    # Save feature list
    joblib.dump(existing_features, "models/feature_list.pkl")

    # Generate report
    report = classification_report(y_test, y_pred)
    print("\n📋 Classification Report:")
    print(report)

    return rf_model, existing_features, accuracy


if __name__ == "__main__":
    train_and_save_model()
