# normalization.py

import pandas as pd

# ----------------------------------------
# Load Datasets
# ----------------------------------------
gps = pd.read_csv("CFC GPS Data.csv", encoding='ISO-8859-1')
recovery_long = pd.read_csv("CFC Recovery status Data.csv", encoding='ISO-8859-1')
physical = pd.read_csv("CFC Physical Capability Data_.csv", encoding='ISO-8859-1')

# ----------------------------------------
# Normalize Function
# ----------------------------------------
def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min()) * 100

# ----------------------------------------
# GPS Normalization
# ----------------------------------------
gps['high_speed_total'] = gps['distance_over_21'] + gps['distance_over_24'] + gps['distance_over_27']
gps['accel_total'] = gps['accel_decel_over_2_5'] + gps['accel_decel_over_3_5'] + gps['accel_decel_over_4_5']

gps['distance_norm'] = min_max_normalize(gps['distance'])
gps['high_speed_norm'] = min_max_normalize(gps['high_speed_total'])
gps['accel_norm'] = min_max_normalize(gps['accel_total'])
gps['peak_speed_norm'] = min_max_normalize(gps['peak_speed'])

print("\n✅ GPS Normalized Columns:")
print(gps[['date', 'distance_norm', 'high_speed_norm', 'accel_norm', 'peak_speed_norm']].head())

# ----------------------------------------
# Pivot Recovery Data (Wide Format)
# ----------------------------------------
recovery_pivot = recovery_long.pivot(index='sessionDate', columns='metric', values='value').reset_index()
recovery_pivot.columns.name = None

recovery = recovery_pivot.rename(columns={
    'sleep_baseline_composite': 'sleep',
    'subjective_baseline_composite': 'subjective',
    'soreness_baseline_composite': 'soreness',
    'emboss_baseline_score': 'emboss'
})

# Normalize Recovery
recovery['sleep_norm'] = min_max_normalize(recovery['sleep'])
recovery['subjective_norm'] = min_max_normalize(recovery['subjective'])
recovery['soreness_norm'] = min_max_normalize(recovery['soreness'])
recovery['emboss_norm'] = min_max_normalize(recovery['emboss'])

print("\n✅ Recovery Normalized Columns:")
print(recovery[['sessionDate', 'sleep_norm', 'subjective_norm', 'soreness_norm', 'emboss_norm']].head())

# ----------------------------------------
# Normalize Physical Capability Data
# ----------------------------------------

# Rename testDate column
physical = physical.rename(columns={"ï»¿testDate": "testDate"})

# Drop rows with missing benchmark percentages
physical = physical.dropna(subset=["benchmarkPct"])

# Normalize the benchmark percentages
physical["benchmarkPct_norm"] = min_max_normalize(physical["benchmarkPct"])

# Optional: filter to focus on meaningful movements
relevant_movements = ["jump", "agility", "upper body"]
physical_filtered = physical[physical["movement"].isin(relevant_movements)]

print("\n✅ Physical Capability Normalized Data:")
print(physical_filtered[["testDate", "movement", "quality", "benchmarkPct", "benchmarkPct_norm"]].head())

# ----------------------------------------
# Save Outputs
# ----------------------------------------
gps.to_csv("normalized_CFC_GPS_Data.csv", index=False)
recovery.to_csv("normalized_CFC_Recovery_Data.csv", index=False)
physical_filtered.to_csv("normalized_CFC_Physical_Data.csv", index=False)
