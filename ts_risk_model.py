import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load time-series enriched dataset
# -------------------------------
df = pd.read_csv("ts_risk_data.csv")

# -------------------------------
# Define Features and Target
# -------------------------------
features = [
    'match_score', 'recovery_score', 'training_score',
    'match_score_prev', 'recovery_score_prev', 'training_score_prev',
    'LBES_3day_avg', 'LBES_5day_avg', 'recovery_3day_avg',
    'training_3day_std', 'LBES_change', 'recovery_slope'
]

X = df[features]
y = df['risk_label']

# -------------------------------
# Train/Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Train Random Forest Classifier
# -------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------------------
# Evaluate the Model
# -------------------------------
y_pred = model.predict(X_test)
print("\n✅ Classification Report:")
print(classification_report(y_test, y_pred))

# -------------------------------
# Confusion Matrix Visualization
# -------------------------------
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Safe', 'High Risk'], yticklabels=['Safe', 'High Risk'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Injury Risk Model - Confusion Matrix')
plt.tight_layout()
plt.savefig("risk_model_confusion_matrix.png")
plt.show()

# -------------------------------
# Feature Importance Plot
# -------------------------------
importances = model.feature_importances_
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
importance_df = importance_df.sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=importance_df, x='Importance', y='Feature')
plt.title('Feature Importance - Injury Risk Prediction')
plt.tight_layout()
plt.savefig("risk_model_feature_importance.png")
plt.show()

# -------------------------------
# Save Predictions for Power BI
# -------------------------------
df['risk_prediction'] = model.predict(X)
df['risk_prob'] = model.predict_proba(X)[:, 1]  # probability of being high risk
df.to_csv("ts_risk_predictions.csv", index=False)
print("\n📁 Saved predictions to ts_risk_predictions.csv")
