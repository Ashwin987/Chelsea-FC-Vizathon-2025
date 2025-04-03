# Chelsea-FC-Vizathon-2025


# Chelsea FC Vizathon 2025 – Load Balance Efficiency Score (LBES)

**Author:** Ashwin Ramaseshan  
**Email:** ashwin.ramases@gmail.com  
**LinkedIn:** [Ashwin Ramaseshan](https://www.linkedin.com/in/ashwin-ramaseshan/)  
**GitHub:** [Chelsea-FC-Vizathon-2025](https://github.com/Ashwin987/Chelsea-FC-Vizathon-2025)

---

## 📌 Overview

This project was developed for the **Chelsea FC Performance Insights Vizathon 2025**. It introduces the **Load Balance Efficiency Score (LBES)** — a unified metric designed to monitor player performance, recovery, and training readiness. The system helps predict injury risk, detect imbalances, and guide performance staff through meaningful insights.

---

## 📁 Folder Structure

Chelsea-FC-Vizathon-2025/ │ ├── Charts/ # All Power BI visualizations (.pbix) and PNG exports ├── Datasets/ # Input data files used for analysis (e.g., CSVs) │ ├── calculate_component_scores.py ├── cluster_profiles.py ├── export_feature_importance.py ├── lbes.py ├── lbes_spike_detection.py ├── load_recommendations.py ├── normalization.py ├── time_to_recovery.py ├── ts_feature_engineering.py ├── ts_risk_model.py ├── training_score.py │ ├── README.md # You're here! ├── Chelsea_Vizathon_Final_Report.pdf # Final report for submission


---

## 🚀 How to Run the Code

Ensure you have **Python 3.8+** installed. Then:

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Ashwin987/Chelsea-FC-Vizathon-2025.git
   cd Chelsea-FC-Vizathon-2025

Install required packages
pip install -r requirements.txt

Run files in order (or as needed)

    normalization.py: Scales input features (0–100)

    calculate_component_scores.py: Computes match, training, and recovery scores

    lbes.py: Calculates LBES for each session

    lbes_spike_detection.py: Detects spikes/drops in LBES

    ts_feature_engineering.py: Generates rolling stats

    ts_risk_model.py: Predicts injury risk using Random Forest

    time_to_recovery.py: Calculates days to return to readiness

    📊 Visualizations

All charts and dashboards are included in the Charts/ folder:

    Training vs Recovery vs Match Load

    LBES Over Time

    Spike and Drop Detection

    Clustering Load Profiles

    Injury Risk Feature Importance

    Distribution of Player Risk Levels

These were created using Power BI and exported for inclusion in the final PDF.
📘 Final Report

See Chelsea_Vizathon_Final_Report.pdf for the complete write-up, graphs, and methodology.
❓Questions or Feedback?

Feel free to reach out:

    📧 ashwin.ramases@gmail.com

    💼 LinkedIn – Ashwin Ramaseshan

    💻 Project GitHub Repo