# chart.py
# Email: 22f3002631@ds.study.iitm.ac.in
# Customer Analytics: Response Time Distribution by Support Channel
# Creates a Seaborn violinplot for support response times

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# Generate synthetic dataset
# ---------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Simulate response times (in minutes) for each support channel
data = []
for channel in channels:
    if channel == "Email":
        times = np.random.normal(loc=120, scale=30, size=200)  # slower
    elif channel == "Chat":
        times = np.random.normal(loc=15, scale=5, size=200)    # fastest
    elif channel == "Phone":
        times = np.random.normal(loc=45, scale=10, size=200)   # moderate
    else:  # Social Media
        times = np.random.normal(loc=60, scale=15, size=200)   # mid-slow
    # Ensure positive times
    times = np.clip(times, 1, None)
    for t in times:
        data.append({"Channel": channel, "ResponseTime": t})

df = pd.DataFrame(data)

# ---------------------------
# Visualization
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # ensures 512x512 pixels at dpi=64

ax = sns.violinplot(
    x="Channel", y="ResponseTime", data=df,
    palette="Set2", inner="quartile", cut=0
)

ax.set_title("Customer Support Response Times by Channel", fontsize=16, pad=20)
ax.set_xlabel("Support Channel", fontsize=14)
ax.set_ylabel("Response Time (minutes)", fontsize=14)

plt.tight_layout()

# ---------------------------
# Save chart as exactly 512x512 pixels
# ---------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
