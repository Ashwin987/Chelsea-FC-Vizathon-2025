import pandas as pd

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("FInalLbes.csv")
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df = df.sort_values('date')

# -------------------------------
# Create Lag Features
# -------------------------------
df['match_score_prev'] = df['match_score'].shift(1)
df['recovery_score_prev'] = df['recovery_score'].shift(1)
df['training_score_prev'] = df['training_score'].shift(1)

# -------------------------------
# Rolling Averages (Windows: 3 & 5)
# -------------------------------
df['LBES_3day_avg'] = df['LBES'].rolling(window=3).mean()
df['LBES_5day_avg'] = df['LBES'].rolling(window=5).mean()

df['recovery_3day_avg'] = df['recovery_score'].rolling(window=3).mean()
df['training_3day_std'] = df['training_score'].rolling(window=3).std()

# -------------------------------
# Score Slopes (Change Over Time)
# -------------------------------
df['LBES_change'] = df['LBES'] - df['LBES'].shift(1)
df['recovery_slope'] = df['recovery_score'] - df['recovery_score'].shift(2)

# -------------------------------
# Binary Risk Label
# -------------------------------
df['risk_label'] = (df['LBES'] < 50).astype(int)

# -------------------------------
# Drop Rows with NaNs (from rolling windows)
# -------------------------------
df = df.dropna()

# -------------------------------
# Save Output
# -------------------------------
df.to_csv("ts_risk_data.csv", index=False)
print("✅ Time-series features saved to ts_risk_data.csv")
