# calculate_component_scores.py

import pandas as pd

# -------------------------------
# Load Normalized Data
# -------------------------------
gps = pd.read_csv("normalized_CFC_GPS_Data.csv")
recovery = pd.read_csv("normalized_CFC_Recovery_Data.csv")

# -------------------------------
# Match Load Score (MLS)
# -------------------------------
# Uses: distance_norm, high_speed_norm, accel_norm, peak_speed_norm
gps['match_score'] = (
    0.3 * gps['distance_norm'] +
    0.25 * gps['high_speed_norm'] +
    0.25 * gps['accel_norm'] +
    0.2 * gps['peak_speed_norm']
)

print("\n✅ Match Load Score (First 5):")
print(gps[['date', 'match_score']].head())

# -------------------------------
# Recovery Score (RS) — Soft Averaging
# -------------------------------
# Uses: sleep_norm, subjective_norm, soreness_norm, emboss_norm
# Handles missing values by computing row-wise mean
recovery['recovery_score'] = recovery[
    ['sleep_norm', 'subjective_norm', 'soreness_norm', 'emboss_norm']
].mean(axis=1, skipna=True)

print("\n✅ Recovery Score (First 5):")
print(recovery[['sessionDate', 'recovery_score']].head())

# -------------------------------
# Save Output
# -------------------------------
gps[['date', 'match_score']].to_csv("match_score.csv", index=False)
recovery[['sessionDate', 'recovery_score']].to_csv("recovery_score.csv", index=False)
print("\n✅ Output Saved!")
