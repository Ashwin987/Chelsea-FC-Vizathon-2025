import pandas as pd

# -------------------------------
# Load Final LBES Dataset
# -------------------------------
df = pd.read_csv("FInalLbes.csv")

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

# Sort by date
df = df.sort_values('date').reset_index(drop=True)

# -------------------------------
# Calculate % Change in LBES
# -------------------------------
df['lbes_pct_change'] = df['LBES'].pct_change() * 100

# -------------------------------
# Flag Spikes or Drops
# -------------------------------
def flag_change(pct):
    if pd.isna(pct):
        return "No Data"
    elif pct > 20:
        return "🔺 Spike"
    elif pct < -20:
        return "🔻 Drop"
    else:
        return "Normal"

df['change_flag'] = df['lbes_pct_change'].apply(flag_change)

# -------------------------------
# Save Output for Power BI or Report
# -------------------------------
df.to_csv("lbes_spike_alerts.csv", index=False)
print("\n✅ Saved LBES spike alerts to 'lbes_spike_alerts.csv'.")

# Optional: Preview results
print(df[['date', 'LBES', 'lbes_pct_change', 'change_flag']].head(10))
