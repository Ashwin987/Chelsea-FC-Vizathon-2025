# calculate_training_score.py

import pandas as pd

# -------------------------------
# Load Normalized Physical Data
# -------------------------------
physical = pd.read_csv("normalized_CFC_Physical_Data.csv")

# -------------------------------
# Convert Date Format with dayfirst
# -------------------------------
physical['testDate'] = pd.to_datetime(physical['testDate'], dayfirst=True)

# -------------------------------
# Group by testDate and Average
# -------------------------------
training_score = physical.groupby('testDate')['benchmarkPct_norm'].mean().reset_index()
training_score = training_score.rename(columns={
    'testDate': 'date',
    'benchmarkPct_norm': 'training_score'
})

# -------------------------------
# Preview Results
# -------------------------------
print("\n✅ Training Load Score (First 5):")
print(training_score.head())

# -------------------------------
# Save Output
# -------------------------------
training_score.to_csv("training_score.csv", index=False)
print("\n✅ Saved as training_score.csv")
