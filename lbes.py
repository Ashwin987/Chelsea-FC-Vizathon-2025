# calculate_lbes.py

import pandas as pd

# -------------------------------
# Load All Score Files
# -------------------------------
match = pd.read_csv("match_score.csv")
recovery = pd.read_csv("recovery_score.csv")
training = pd.read_csv("training_score.csv")

# -------------------------------
# Convert All Dates to datetime (DD/MM/YYYY support)
# -------------------------------
match['date'] = pd.to_datetime(match['date'], dayfirst=True, errors='coerce')
recovery['sessionDate'] = pd.to_datetime(recovery['sessionDate'], dayfirst=True, errors='coerce')
training['date'] = pd.to_datetime(training['date'], dayfirst=True, errors='coerce')

# Standardize recovery date column
recovery = recovery.rename(columns={'sessionDate': 'date'})

# Strip time — keep only date for merge
match['date'] = match['date'].dt.date
recovery['date'] = recovery['date'].dt.date
training['date'] = training['date'].dt.date

# -------------------------------
# Merge All 3 Score Tables
# -------------------------------
merged = match.merge(recovery, on='date', how='outer')
merged = merged.merge(training, on='date', how='outer')

# -------------------------------
# Drop Rows Missing Any Score
# -------------------------------
merged = merged.dropna(subset=['match_score', 'recovery_score', 'training_score'])

# -------------------------------
# Calculate Final LBES
# -------------------------------
merged['LBES'] = (
    0.35 * merged['recovery_score'] +
    0.35 * merged['training_score'] +
    0.30 * merged['match_score']
)

# -------------------------------
# Assign Risk Level
# -------------------------------
def classify_risk(score):
    if score >= 60:
        return "Optimal"
    elif score >= 55:
        return "Acceptable"
    elif score >= 50:
        return "Caution"
    else:
        return "High Risk"

merged['risk_level'] = merged['LBES'].apply(classify_risk)

# -------------------------------
# Final clean-up for Power BI
# -------------------------------
merged['risk_level'] = merged['risk_level'].astype(str).str.strip()

# Save cleaned version
merged.to_csv("final_lbesDonut.csv", index=False)
print("\n✅ Final LBES file cleaned and saved as 'final_lbes.csv' for Power BI.")

# Preview (optional)
print(merged[['date', 'match_score', 'recovery_score', 'training_score', 'LBES', 'risk_level']].head(10))
