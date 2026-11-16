import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    'City':         ['Alger', 'Annaba', 'Oran', 'Alger', 'Oran', 'Annaba', 'Alger', 'Oran'],
    'Department':   ['Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology'],
    'Age':          [45, 60, 30, 50, 40, 70, 35, 55],
    'DaysAdmitted': [5, 8, 3, 7, 4, 6, 2, 9],
    'DailyCost':    [200, 300, 150, 220, 280, 160, 210, 290],
    'Satisfaction': [4.5, 3.8, 4.2, 4.0, 4.1, 3.5, 4.7, 3.9],
    'Readmitted':   [0, 1, 0, 0, 1, 1, 0, 1],
}

df = pd.DataFrame(data)

df.to_csv('tutorial4/hospital_original.csv', index=True)

df.index = list('ABCDEFGH')
print(df)

print(df.loc['C':'F'])

print(df.iloc[1:4])

print(df.loc['B':'F', ['City', 'Department', 'DailyCost']])

filtered = df[(df['Age'] > 45) & (df['Satisfaction'] < 4)]
print(filtered[['City', 'Age', 'Satisfaction', 'Readmitted']])

df_neurology = df[df['Department'] == 'Neurology'][['City', 'Age', 'DaysAdmitted', 'DailyCost']].reset_index(drop=True)
df_neurology = df_neurology.set_index('City')
df_neurology = df_neurology.sort_values('DailyCost', ascending=False)
print(df_neurology)

print(df_neurology.groupby('City').size())

city_counts = df_neurology.groupby('City').size()
city_counts.plot(kind='bar')
plt.title("Patients per City (Neurology)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("tutorial4/neurology_city_bar.png")
plt.close()
