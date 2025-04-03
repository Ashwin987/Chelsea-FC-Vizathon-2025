import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("ts_risk_data.csv")

# Drop non-numeric columns like 'date' and 'risk_level' if they exist
df = df.drop(columns=[col for col in ['date', 'risk_level'] if col in df.columns])

# Ensure only numeric columns are used for X
X = df.drop(columns=['risk_label'])
X = X.select_dtypes(include='number')  # Drop any remaining non-numeric columns just in case

# Target variable
y = df['risk_label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save feature importances
importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values(by='importance', ascending=False)

importance_df.to_csv("feature_importance_updated.csv", index=False)
print("✅ Feature importance saved as 'feature_importance_updated.csv'")
