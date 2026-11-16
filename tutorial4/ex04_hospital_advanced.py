import pandas as pd
import numpy as np

df = pd.read_csv('tutorial4/hospital_original.csv', index_col=0)
df.index = list('ABCDEFGH')

print(df.columns.tolist())

# Q1: TotalCost
# Q1: TotalCost
df['TotalCost'] = df['DaysAdmitted'] * df['DailyCost']
# Alt: df['TotalCost'] = df.eval('DaysAdmitted * DailyCost')
# Alt: df = df.assign(TotalCost=df['DaysAdmitted'] * df['DailyCost'])
# Alt: df['TotalCost'] = df.eval('DaysAdmitted * DailyCost')
# Alt: df = df.assign(TotalCost=df['DaysAdmitted'] * df['DailyCost'])

# Q2: AgeGroup
# Q2: AgeGroup
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 29, 50, 200], labels=['Young', 'Middle', 'Senior'])
# Alt: df['AgeGroup'] = np.select([df['Age'] <= 29, df['Age'] <= 50], ['Young', 'Middle'], default='Senior')
# Alt: df['AgeGroup'] = np.select([df['Age'] <= 29, df['Age'] <= 50], ['Young', 'Middle'], default='Senior')

# Q3: Rename and drop
# Q3: Rename and drop
df['Bonus'] = df['DailyCost'] * 0.10
df = df.rename(columns={'DailyCost': 'DailyFee'})
df = df.drop(columns=['Bonus'])
# Alt: del df['Bonus']; df.rename(columns={'DailyCost': 'DailyFee'}, inplace=True)
# Alt: del df['Bonus']; df.rename(columns={'DailyCost': 'DailyFee'}, inplace=True)

# Q4: HighCost
# Q4: HighCost
df['HighCost'] = df['TotalCost'].apply(lambda x: 'Yes' if x > 60000 else 'No')
# Alt: df['HighCost'] = np.where(df['TotalCost'] > 60000, 'Yes', 'No')
# Alt: df['HighCost'] = np.where(df['TotalCost'] > 60000, 'Yes', 'No')

# Q5: SatisfactionLevel
# Q5: SatisfactionLevel
df['SatisfactionLevel'] = df['Satisfaction'].apply(
    lambda x: 'Excellent' if x >= 8 else ('Average' if x >= 5 else 'Poor')
)
# Alt: df['SatisfactionLevel'] = np.select([df['Satisfaction'] >= 8, df['Satisfaction'] >= 5], ['Excellent', 'Average'], default='Poor')
# Alt: df['SatisfactionLevel'] = pd.cut(df['Satisfaction'], bins=[-np.inf, 4.99, 7.99, np.inf], labels=['Poor', 'Average', 'Excellent'])
# Alt: df['SatisfactionLevel'] = np.select([df['Satisfaction'] >= 8, df['Satisfaction'] >= 5], ['Excellent', 'Average'], default='Poor')
# Alt: df['SatisfactionLevel'] = pd.cut(df['Satisfaction'], bins=[-np.inf, 4.99, 7.99, np.inf], labels=['Poor', 'Average', 'Excellent'])

# Q6: CostRank
# Q6: CostRank
df['CostRank'] = df['TotalCost'].rank(ascending=False).astype(int)
# Alt: df['CostRank'] = df['TotalCost'].rank(ascending=False, method='dense').astype(int)
# Alt: df['CostRank'] = df['TotalCost'].rank(ascending=False, method='dense').astype(int)

# Q7: RiskScore
# Q7: RiskScore
df['RiskScore'] = (df['DaysAdmitted'] * 0.4) + (df['Age'] * 0.3) + (100 - df['Satisfaction'] * 10) * 0.3
# Alt: df['RiskScore'] = df.eval('(DaysAdmitted * 0.4) + (Age * 0.3) + (100 - Satisfaction * 10) * 0.3')
# Alt: df['RiskScore'] = df.eval('(DaysAdmitted * 0.4) + (Age * 0.3) + (100 - Satisfaction * 10) * 0.3')

# Q8: RiskCategory
# Q8: RiskCategory
df['RiskCategory'] = df['RiskScore'].apply(
    lambda x: 'High' if x > 60 else ('Medium' if x >= 40 else 'Low')
)
# Alt: df['RiskCategory'] = np.select([df['RiskScore'] > 60, df['RiskScore'] >= 40], ['High', 'Medium'], default='Low')
# Alt: df['RiskCategory'] = pd.cut(df['RiskScore'], bins=[-np.inf, 39.99, 60, np.inf], labels=['Low', 'Medium', 'High'])
# Alt: df['RiskCategory'] = np.select([df['RiskScore'] > 60, df['RiskScore'] >= 40], ['High', 'Medium'], default='Low')
# Alt: df['RiskCategory'] = pd.cut(df['RiskScore'], bins=[-np.inf, 39.99, 60, np.inf], labels=['Low', 'Medium', 'High'])

df = df.sort_values('RiskScore', ascending=False)
print(df)

# Q9: GroupBy aggregation
# Q9: GroupBy aggregation
city_summary = df.groupby('City').agg(
    avg_total_cost=('TotalCost', 'mean'),
    avg_satisfaction=('Satisfaction', 'mean'),
    readmission_rate=('Readmitted', 'mean')
)
# Alt: city_summary = df.groupby('City')[['TotalCost', 'Satisfaction', 'Readmitted']].mean()
# Alt: city_summary = df.groupby('City')[['TotalCost', 'Satisfaction', 'Readmitted']].mean()
print(city_summary)

# Q10: City with highest avg RiskScore
# Q10: City with highest avg RiskScore
print("City with highest avg RiskScore:", df.groupby('City')['RiskScore'].mean().idxmax())
# Alt: print("City with highest avg RiskScore:", df.groupby('City')['RiskScore'].mean().nlargest(1).index[0])
# Alt: print("City with highest avg RiskScore:", df.groupby('City')['RiskScore'].mean().nlargest(1).index[0])

# Q11: Fill missing values
# Q11: Fill missing values
df['Satisfaction'] = df['Satisfaction'].fillna(df['Satisfaction'].mean())
# Alt: df['Satisfaction'].fillna(df['Satisfaction'].mean(), inplace=True)
# Alt: df['Satisfaction'] = df['Satisfaction'].fillna(df.groupby('City')['Satisfaction'].transform('mean'))
# Alt: df['Satisfaction'].fillna(df['Satisfaction'].mean(), inplace=True)
# Alt: df['Satisfaction'] = df['Satisfaction'].fillna(df.groupby('City')['Satisfaction'].transform('mean'))

# Q12: Mapping values
# Q12: Mapping values
city_map = {'Alger': 'DZ-16', 'Annaba': 'DZ-23', 'Oran': 'DZ-31'}
df['City'] = df['City'].map(city_map)
# Alt: df['City'] = df['City'].replace(city_map)
# Alt: df['City'] = df['City'].replace(city_map)

df['Readmitted'] = df['Readmitted'].map({0: 'No', 1: 'Yes'})
# Alt: df['Readmitted'] = np.where(df['Readmitted'] == 1, 'Yes', 'No')
# Alt: df['Readmitted'] = np.where(df['Readmitted'] == 1, 'Yes', 'No')

# Q13: Pivot Table
# Q13: Pivot Table
pivot = df.pivot_table(values=['TotalCost', 'Satisfaction'], index='City', columns='Department', aggfunc='mean')
# Alt: pivot = df.groupby(['City', 'Department'])[['TotalCost', 'Satisfaction']].mean().unstack()
# Alt: pivot = df.groupby(['City', 'Department'])[['TotalCost', 'Satisfaction']].mean().unstack()
print(pivot)

df.to_csv('tutorial4/hospital_risk.csv')
city_summary.to_csv('tutorial4/city_summary.csv')
