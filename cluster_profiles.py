# cluster_profiles.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# -------------------------------
# Load LBES Scores
# -------------------------------
df = pd.read_csv("FInalLbes.csv")

# -------------------------------
# Select Features for Clustering
# -------------------------------
features = df[['match_score', 'recovery_score', 'training_score']].copy()

# -------------------------------
# Normalize Using StandardScaler
# -------------------------------
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# -------------------------------
# Apply KMeans Clustering
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster_label'] = kmeans.fit_predict(scaled_features)

# -------------------------------
# Save to CSV for Power BI
# -------------------------------
df.to_csv("clustered_lbes.csv", index=False)
print("✅ Saved clustered_lbes.csv with cluster labels")

# -------------------------------
# 2D Scatter Plot (Match vs Recovery)
# -------------------------------
# Assign descriptive cluster names
cluster_labels = {
    0: "Cluster 0: Balanced Load",
    1: "Cluster 1: Low Match/Recovery Load",
    2: "Cluster 2: High Match Load, Low Recovery"
}

# Assign custom colors
cluster_colors = {
    0: "#F4D03F",  # yellow
    1: "#BB8FCE",  # purple
    2: "#48C9B0"   # teal
}

# Plot by cluster
plt.figure(figsize=(10, 7))
for label in df['cluster_label'].unique():
    subset = df[df['cluster_label'] == label]
    plt.scatter(
        subset['match_score'],
        subset['recovery_score'],
        c=cluster_colors[label],
        label=cluster_labels[label],
        s=60,
        edgecolors='black',
        alpha=0.8
    )

plt.xlabel("Match Score")
plt.ylabel("Recovery Score")
plt.title("Clustering Load Profiles (K=3)")
plt.legend(title="Clusters")
plt.grid(True)
plt.tight_layout()
plt.savefig("lbes_clusters_plot.png")
plt.show()
