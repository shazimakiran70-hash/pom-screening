"""
hybrid_cat_predictor.py
HybridCatPredictor: Data-driven screening of visible-light POM hybrid photocatalysts
Author: Shazima Kiran
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# =======================
# Example Dataset (placeholder)
# =======================
# You can replace this CSV with your real features
example_data = {
    "id": ["POM1", "POM2", "POM3", "POM4", "POM5"],
    "bandgap_eV": [2.5, 3.1, 2.0, 3.5, 2.8],
    "CBM_eV": [-0.5, -0.6, -0.4, -0.7, -0.45],
    "VBM_eV": [2.0, 2.5, 1.6, 2.8, 2.35],
    "POM_LUMO_eV": [-0.6, -0.55, -0.5, -0.65, -0.6],
    "CO2_adsorption_eV": [-0.2, -0.3, -0.15, -0.35, -0.25],
    "stability_index": [0.8, 0.7, 0.85, 0.65, 0.78],
    "activity_score": [0.7, 0.6, 0.8, 0.5, 0.72]
}

df = pd.DataFrame(example_data)

# =======================
# Model Training
# =======================
X = df[["bandgap_eV", "CBM_eV", "VBM_eV", "POM_LUMO_eV", "CO2_adsorption_eV", "stability_index"]]
y = df["activity_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
print(f"Baseline Random Forest MSE: {mse:.4f}")

# =======================
# Prediction on new candidates
# =======================
# New candidate descriptors (example)
new_candidates = pd.DataFrame({
    "id": ["POM6", "POM7"],
    "bandgap_eV": [2.2, 3.0],
    "CBM_eV": [-0.45, -0.6],
    "VBM_eV": [1.75, 2.4],
    "POM_LUMO_eV": [-0.5, -0.55],
    "CO2_adsorption_eV": [-0.18, -0.28],
    "stability_index": [0.82, 0.7]
})

X_new = new_candidates[["bandgap_eV", "CBM_eV", "VBM_eV", "POM_LUMO_eV", "CO2_adsorption_eV", "stability_index"]]
new_candidates["predicted_activity"] = model.predict(X_new)

# Rank candidates
new_candidates_sorted = new_candidates.sort_values("predicted_activity", ascending=False)
print("\nPredicted and Ranked Candidates:")
print(new_candidates_sorted[["id", "predicted_activity"]])

# =======================
# Function Wrappers (for modularity)
# =======================
def train_model(X, y):
    """Train and return Random Forest model"""
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)
    return model

def predict_activity(model, df_features):
    """Predict activity score for new candidates"""
    return model.predict(df_features)
