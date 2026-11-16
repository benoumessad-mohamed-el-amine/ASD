"""
Exercise 05: Hospital Data Visualization — Matplotlib vs Seaborn
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set overall seaborn aesthetic
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# 0. Load Data & Prepare Required Columns
# ---------------------------------------------------------
df = pd.read_csv('tutorial4/hospital_original.csv', index_col=0)
df.index = list('ABCDEFGH')

# Compute TotalCost, RiskScore, RiskCategory, HighCost, and Readmitted
df['TotalCost'] = df['DaysAdmitted'] * df['DailyCost']
df['RiskScore'] = (df['DaysAdmitted'] * 0.4) + (df['Age'] * 0.3) + (100 - df['Satisfaction'] * 10) * 0.3
df['RiskCategory'] = np.select([df['RiskScore'] > 60, df['RiskScore'] >= 40], ['High', 'Medium'], default='Low')

# HighCost: In Ex04 text it was >60000; for realistic visualization we use >1500 (or flag both)
df['HighCost'] = np.where(df['TotalCost'] > 1500, 'Yes', 'No')

# Map Readmitted for clear categorical plots
df['Readmitted'] = df['Readmitted'].map({0: 'No', 1: 'Yes'})

print("Prepared DataFrame Preview:")
print(df[['City', 'Department', 'DailyCost', 'TotalCost', 'Satisfaction', 'RiskScore', 'RiskCategory', 'HighCost', 'Readmitted']])

# =========================================================
# MATPLOTLIB SECTION
# =========================================================

# ---------------------------------------------------------
# 1. Total Cost per City (Bar Chart)
# ---------------------------------------------------------
city_total_cost = df.groupby('City')['TotalCost'].sum()

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(city_total_cost.index, city_total_cost.values, color='skyblue', edgecolor='black')
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Total Cost ($)', fontsize=12)
ax.set_title('Total Cost per City', fontsize=14, fontweight='bold')
ax.bar_label(bars, fmt='%.0f', padding=3, fontsize=10)
# Alt: for b in bars: ax.text(b.get_x() + b.get_width()/2, b.get_height() + 50, f"{b.get_height():.0f}", ha='center')

plt.tight_layout()
plt.savefig('tutorial4/matplotlib_q1_total_cost.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 2. Satisfaction Distribution (Histogram)
# ---------------------------------------------------------
mean_sat = df['Satisfaction'].mean()
median_sat = df['Satisfaction'].median()

fig, ax = plt.subplots(figsize=(7, 5))
n, bins, patches = ax.hist(df['Satisfaction'], bins=5, color='orange', edgecolor='black', alpha=0.7)
ax.axvline(mean_sat, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_sat:.2f}')
ax.axvline(median_sat, color='blue', linestyle=':', linewidth=2, label=f'Median: {median_sat:.2f}')
ax.set_xlabel('Satisfaction Score', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.set_title('Satisfaction Score Distribution (bins=5)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig('tutorial4/matplotlib_q2_satisfaction_hist.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 3. Cost vs Satisfaction Scatter Plot
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
# Highlight HighCost == 'Yes' in red, and 'No' in navy
colors = np.where(df['HighCost'] == 'Yes', 'crimson', 'navy')
scatter = ax.scatter(df['Satisfaction'], df['TotalCost'], c=colors, s=100, edgecolors='black', alpha=0.85)

for i, txt in enumerate(df.index):
    ax.annotate(f"{txt} ({df.iloc[i]['HighCost']})", 
                (df.iloc[i]['Satisfaction'], df.iloc[i]['TotalCost']),
                textcoords="offset points", xytext=(5, 5), fontsize=9)

# Custom legend for HighCost
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='HighCost: Yes (> $1500)', markerfacecolor='crimson', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='HighCost: No (<= $1500)', markerfacecolor='navy', markersize=10)
]
ax.legend(handles=legend_elements, loc='upper left')

ax.set_xlabel('Satisfaction Score', fontsize=12)
ax.set_ylabel('Total Cost ($)', fontsize=12)
ax.set_title('Total Cost vs Satisfaction', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('tutorial4/matplotlib_q3_scatter.png', dpi=300)
plt.close()

# Discussion on Readability:
readability_discussion = (
    "Readability Discussion (Cost vs Satisfaction Scatter):\n"
    "- With only 8 patient points, data points are sparse, making trend detection difficult.\n"
    "- If the literal Ex04 threshold of >60,000 is used, no points are highlighted because max cost is $2,610.\n"
    "- Using a threshold of $1,500 successfully highlights high-cost patients (B, D, H), showing they correspond to lower satisfaction (3.8 - 4.0).\n"
    "- Point labels help identify individuals without cluttering due to small sample size."
)
print(readability_discussion)

# ---------------------------------------------------------
# 4. Subplots by City
# ---------------------------------------------------------
cities = ['Alger', 'Annaba', 'Oran']
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

dept_colors = {'Cardiology': '#4c72b0', 'Neurology': '#55a868', 'Orthopedics': '#c44e52'}

for ax, city in zip(axes, cities):
    city_data = df[df['City'] == city].groupby('Department')['Satisfaction'].mean()
    bar_colors = [dept_colors.get(d, 'gray') for d in city_data.index]
    bars = ax.bar(city_data.index, city_data.values, color=bar_colors, edgecolor='black')
    ax.set_title(f"City: {city}", fontsize=12, fontweight='bold')
    ax.set_xlabel('Department', fontsize=11)
    ax.set_ylim(0, 5.5)
    ax.bar_label(bars, fmt='%.2f', padding=3)

axes[0].set_ylabel('Average Satisfaction', fontsize=12)
fig.suptitle('Average Satisfaction per Department by City', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig('tutorial4/matplotlib_q4_subplots_city.png', dpi=300)
plt.close()


# =========================================================
# SEABORN SECTION
# =========================================================

# ---------------------------------------------------------
# 1. Compare City Performances
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=df, x='City', y='TotalCost', hue='Department', estimator='mean', errorbar=None, palette='Set2')
plt.title('Average TotalCost by City and Department', fontsize=14, fontweight='bold')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average TotalCost ($)', fontsize=12)
plt.legend(title='Department')
plt.tight_layout()
plt.savefig('tutorial4/seaborn_q1_city_performance.png', dpi=300)
plt.close()

seaborn_q1_interpretation = (
    "Seaborn Q1 Interpretation:\n"
    "- Alger only has patients in Cardiology, averaging ~$987 in total cost.\n"
    "- Annaba offers Neurology ($2,400) and Orthopedics ($960).\n"
    "- Oran has Neurology ($1,865 avg) and Orthopedics ($450).\n"
    "- Across all cities, Neurology incurs the highest average TotalCost, while Orthopedics has the lowest."
)
print(seaborn_q1_interpretation)

# ---------------------------------------------------------
# 2. Barplot vs. Stripplot
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Barplot (aggregates)
sns.barplot(data=df, x='Department', y='DailyCost', hue='City', estimator='mean', errorbar=None, ax=ax1, palette='tab10')
ax1.set_title('Average DailyCost (Barplot)', fontsize=13, fontweight='bold')
ax1.set_ylabel('Mean DailyCost ($)')

# Subplot 2: Stripplot (individual data points)
sns.stripplot(data=df, x='Department', y='DailyCost', hue='City', jitter=True, dodge=True, size=10, ax=ax2, palette='tab10')
ax2.set_title('Individual DailyCost (Stripplot with Jitter & Dodge)', fontsize=13, fontweight='bold')
ax2.set_ylabel('DailyCost ($)')

plt.tight_layout()
plt.savefig('tutorial4/seaborn_q2_barplot_vs_stripplot.png', dpi=300)
plt.close()

seaborn_q2_explanation = (
    "Seaborn Q2 Explanation (Barplot vs Stripplot):\n"
    "- Barplot shows aggregated summary statistics (mean) and obscures the underlying distribution and sample size.\n"
    "- Stripplot shows every individual observation, showing exact values and sample counts.\n"
    "- Role of jitter: Jitter introduces small random horizontal noise so overlapping points with identical values don't hide each other.\n"
    "- Role of dodge: Dodge separates the hue categories horizontally per department to avoid stacking."
)
print(seaborn_q2_explanation)

# ---------------------------------------------------------
# 3. Risk Distribution (Boxplot vs. Violinplot)
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=df, x='City', y='RiskScore', hue='City', legend=False, ax=ax1, palette='pastel')
ax1.set_title('RiskScore Distribution across Cities (Boxplot)', fontsize=13, fontweight='bold')
ax1.set_ylabel('RiskScore')

sns.violinplot(data=df, x='City', y='RiskScore', hue='City', legend=False, ax=ax2, palette='pastel', cut=0)
ax2.set_title('RiskScore Density across Cities (Violinplot)', fontsize=13, fontweight='bold')
ax2.set_ylabel('RiskScore')

plt.tight_layout()
plt.savefig('tutorial4/seaborn_q3_risk_distribution.png', dpi=300)
plt.close()

seaborn_q3_comparison = (
    "Seaborn Q3 Comparison (Boxplot vs Violinplot):\n"
    "- Boxplot displays the standard 5-number summary (min, Q1, median, Q3, max) and flags potential outliers.\n"
    "- Violinplot enhances this by showing the Kernel Density Estimation (KDE) curve, displaying distribution shape/density.\n"
    "- Note on small data: For small sample sizes (N=8 total, 2-3 per city), violin plot KDE can over-smooth or suggest continuous density where data is actually sparse."
)
print(seaborn_q3_comparison)

# ---------------------------------------------------------
# 4. Combined Dashboard
# ---------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Barplot of average satisfaction per city
sns.barplot(data=df, x='City', y='Satisfaction', hue='City', legend=False, estimator='mean', errorbar=None, ax=axes[0, 0], palette='Blues_d')
axes[0, 0].set_title('Average Satisfaction per City', fontweight='bold')
axes[0, 0].set_ylim(0, 5.5)

# Subplot 2: Boxplot of RiskScore by RiskCategory
sns.boxplot(data=df, x='RiskCategory', y='RiskScore', hue='RiskCategory', legend=False, ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('RiskScore by RiskCategory', fontweight='bold')

# Subplot 3: Scatterplot of Age versus RiskScore, colored by RiskCategory
sns.scatterplot(data=df, x='Age', y='RiskScore', hue='RiskCategory', s=120, ax=axes[1, 0], palette='Set1', edgecolor='black')
axes[1, 0].set_title('Age vs RiskScore (by RiskCategory)', fontweight='bold')

# Subplot 4: Countplot of readmissions (Yes/No) per city
sns.countplot(data=df, x='City', hue='Readmitted', ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Readmissions per City', fontweight='bold')

# Shared title
fig.suptitle('Hospital Risk and Satisfaction Overview', fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig('tutorial4/seaborn_q4_combined_dashboard.png', dpi=300)
plt.close()

print("All Exercise 05 plots have been generated and saved successfully.")
