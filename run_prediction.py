# run_prediction.py
# Reads sample_pom_dataset.csv, trains a baseline RandomForest on the small dataset,
# computes simple composite score (same formula used to generate predicted_results.csv),
# and writes predicted_results.csv. Works in plain Python with pandas and scikit-learn.

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("sample_pom_dataset.csv")

# Simple feature pipeline: one-hot encode categorical POM_type, Metal_Center, Host
cat_cols = ["POM_type", "Metal_Center", "Host"]
num_cols = ["bandgap_eV", "CBM_eV", "POM_LUMO_eV", "CO2_adsorption_eV", "stability_index"]

# Prepare X and a mock target (we'll compute composite_score as 'target' to train & reproduce)
def composite_score_row(row):
    # Same weights and formula used to generate example predictions
    vis = row["bandgap_eV"]
    alignment = -abs(row["CBM_eV"] - row["POM_LUMO_eV"])
    stability = row["stability_index"]
    ads = row["CO2_adsorption_eV"]
    vis_score = max(0, min(1, (3.2 - vis) / 2.0))
    align_score = max(0, min(1, (alignment + 2) / 2.0))
    stab_score = stability
    ads_score = max(0, min(1, (0.0 - ads)))
    final = 0.35 * vis_score + 0.30 * align_score + 0.20 * stab_score + 0.15 * ads_score
    return final

# Create a target column from composite score (this is just to show training; in real use you'd have measured activity)
df["activity_target"] = df.apply(composite_score_row, axis=1)

X = df[cat_cols + num_cols]
y = df["activity_target"]

# Build pipeline
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(sparse=False, handle_unknown="ignore"), cat_cols),
    ("num", "passthrough", num_cols)
])

pipeline = Pipeline([
    ("pre", preprocessor),
    ("rf", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Train model
pipeline.fit(X, y)

# Predict (we predict on the same rows just as a demo)
preds = pipeline.predict(X)
df_out = pd.DataFrame({
    "Compound": df["Compound"],
    "Predicted_Activity_Score": np.round(preds, 3)
})

# Save results
df_out.to_csv("predicted_results.csv", index=False)
print("Wrote predicted_results.csv")
print(df_out)
