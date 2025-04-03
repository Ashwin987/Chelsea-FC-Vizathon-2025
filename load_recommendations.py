# load_recommendations.py

import pandas as pd

# -------------------------------------
# Load Final LBES Data
# -------------------------------------
df = pd.read_csv("FInalLbes.csv")

# -------------------------------------
# Filter for Optimal Performance (LBES >= 70)
# -------------------------------------
optimal_df = df[df['LBES'] >= 70]

# -------------------------------------
# Calculate Ideal Averages
# -------------------------------------
ideal_match = optimal_df['match_score'].mean()
ideal_training = optimal_df['training_score'].mean()
ideal_recovery = optimal_df['recovery_score'].mean()

# -------------------------------------
# Store Results
# -------------------------------------
recommendations = pd.DataFrame({
    'load_type': ['match_score', 'training_score', 'recovery_score'],
    'ideal_value': [ideal_match, ideal_training, ideal_recovery]
})

# Save to Excel for Power BI
recommendations.to_excel("personalized_load_recommendations.xlsx", index=False)

# Preview
print("\n✅ Personalized Load Recommendations (based on LBES ≥ 70):\n")
print(recommendations)
