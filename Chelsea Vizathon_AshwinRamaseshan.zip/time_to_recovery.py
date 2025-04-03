# load_recommendations.py

import pandas as pd

# -------------------------------
# Load Final LBES Dataset
# -------------------------------
df = pd.read_csv("FInalLbes.csv")

# -------------------------------
# Use Top 10% LBES for "Optimal" Periods
# -------------------------------
top_10_threshold = df['LBES'].quantile(0.9)
ideal_data = df[df['LBES'] >= top_10_threshold]

if ideal_data.empty:
    print("⚠️ No rows found in top 10% — fallback to entire dataset.")
    ideal_data = df

# -------------------------------
# Calculate Mean of Load Variables
# -------------------------------
load_columns = ['match_score', 'training_score', 'recovery_score']
recommendations = ideal_data[load_columns].mean().reset_index()
recommendations.columns = ['load_type', 'ideal_value']

# -------------------------------
# Save Recommendations
# -------------------------------
recommendations.to_csv("load_recommendations.csv", index=False)
print("\n✅ Personalized Load Recommendations (based on Top 10% LBES):\n")
print(recommendations)
