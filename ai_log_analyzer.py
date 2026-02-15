import json
import pandas as pd
from collections import Counter

LOG_FILE = "sample_alerts.json"

print("=== AI SOC Log Analyzer Started ===")

# Load Wazuh alerts
with open(LOG_FILE, "r") as f:
    alerts = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(alerts)

print("\nTotal Alerts:", len(df))

# Extract rule descriptions
if "rule" in df.columns:
    df["rule_description"] = df["rule"].apply(lambda x: x.get("description") if isinstance(x, dict) else "Unknown")

# Count alert types
alert_counts = Counter(df["rule_description"])

print("\nTop Detected Alerts:")
for alert, count in alert_counts.most_common(5):
    print(f"{alert}: {count}")

# Detect brute force behavior
brute_force_alerts = df[df["rule_description"].str.contains("SSH", case=False, na=False)]

if len(brute_force_alerts) > 5:
    print("\n⚠️ Potential Brute Force Attack Detected!")
    print("Total SSH-related alerts:", len(brute_force_alerts))
else:
    print("\n✅ No brute force attack detected")

# Save analysis report
report = {
    "total_alerts": len(df),
    "top_alerts": alert_counts.most_common(5),
    "ssh_alerts": len(brute_force_alerts)
}

with open("ai_analysis_report.json", "w") as f:
    json.dump
