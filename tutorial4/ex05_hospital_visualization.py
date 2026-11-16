import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tutorial4/hospital_original.csv', index_col=0)
df.index = list('ABCDEFGH')

df['TotalCost'] = df['DaysAdmitted'] * df['DailyCost']
df['RiskScore'] = (df['DaysAdmitted'] * 0.4) + (df['Age'] * 0.3) + (100 - df['Satisfaction'] * 10) * 0.3
df['RiskCategory'] = np.select([df['RiskScore'] > 60, df['RiskScore'] >= 40], ['High', 'Medium'], default='Low')
df['HighCost'] = np.where(df['TotalCost'] > 60000, 'Yes', 'No')
df['Readmitted'] = df['Readmitted'].map({0: 'No', 1: 'Yes'})

cost_per_city = df.groupby('City')['TotalCost'].sum()
fig, ax = plt.subplots()
bars = ax.bar(cost_per_city.index, cost_per_city.values, color='skyblue')
ax.set_xlabel('City')
ax.set_ylabel('Total Cost')
ax.set_title('Total Cost per City')
ax.bar_label(bars)
plt.savefig('tutorial4/matplotlib_q1_total_cost.png')
plt.close()

mean_val = df['Satisfaction'].mean()
median_val = df['Satisfaction'].median()
fig, ax = plt.subplots()
ax.hist(df['Satisfaction'], bins=5, color='orange', edgecolor='black')
ax.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
ax.axvline(median_val, color='blue', linestyle=':', label=f'Median: {median_val:.2f}')
ax.set_xlabel('Satisfaction')
ax.set_ylabel('Frequency')
ax.set_title('Satisfaction Distribution')
ax.legend()
plt.savefig('tutorial4/matplotlib_q2_satisfaction_hist.png')
plt.close()

fig, ax = plt.subplots()
colors = ['red' if x == 'Yes' else 'blue' for x in df['HighCost']]
ax.scatter(df['Satisfaction'], df['TotalCost'], c=colors)
ax.set_xlabel('Satisfaction')
ax.set_ylabel('TotalCost')
ax.set_title('Cost vs Satisfaction')
plt.savefig('tutorial4/matplotlib_q3_scatter.png')
plt.close()

fig, axes = plt.subplots(1, 3, sharey=True, figsize=(12, 4))
cities = ['Alger', 'Annaba', 'Oran']
for i, city in enumerate(cities):
    data = df[df['City'] == city].groupby('Department')['Satisfaction'].mean()
    axes[i].bar(data.index, data.values)
    axes[i].set_title(city)
    axes[i].set_ylim(0, 5)
fig.suptitle('Average Satisfaction per Department by City')
plt.tight_layout()
plt.savefig('tutorial4/matplotlib_q4_subplots_city.png')
plt.close()

plt.figure()
sns.barplot(data=df, x='City', y='TotalCost', hue='Department', estimator='mean')
plt.title('Average TotalCost by City')
plt.savefig('tutorial4/seaborn_q1_city_performance.png')
plt.close()

plt.figure()
sns.barplot(data=df, x='Department', y='DailyCost', hue='City')
plt.title('Average DailyCost by Department')
plt.savefig('tutorial4/seaborn_q2_barplot.png')
plt.close()

plt.figure()
sns.stripplot(data=df, x='Department', y='DailyCost', hue='City', jitter=True, dodge=True)
plt.title('DailyCost by Department (Stripplot)')
plt.savefig('tutorial4/seaborn_q2_stripplot.png')
plt.close()

plt.figure()
sns.boxplot(data=df, x='City', y='RiskScore')
plt.title('RiskScore Boxplot')
plt.savefig('tutorial4/seaborn_q3_boxplot.png')
plt.close()

plt.figure()
sns.violinplot(data=df, x='City', y='RiskScore')
plt.title('RiskScore Violinplot')
plt.savefig('tutorial4/seaborn_q3_violinplot.png')
plt.close()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.barplot(data=df, x='City', y='Satisfaction', estimator='mean', ax=axes[0, 0])
axes[0, 0].set_title('Average Satisfaction per City')

sns.boxplot(data=df, x='RiskCategory', y='RiskScore', ax=axes[0, 1])
axes[0, 1].set_title('RiskScore by RiskCategory')

sns.scatterplot(data=df, x='Age', y='RiskScore', hue='RiskCategory', ax=axes[1, 0])
axes[1, 0].set_title('Age vs RiskScore')

sns.countplot(data=df, x='City', hue='Readmitted', ax=axes[1, 1])
axes[1, 1].set_title('Readmissions per City')

fig.suptitle('Hospital Risk and Satisfaction Overview')
plt.tight_layout()
plt.savefig('tutorial4/seaborn_q4_combined_dashboard.png')
plt.close()
