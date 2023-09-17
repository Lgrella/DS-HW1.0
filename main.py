'Pandas'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/workspaces/DS-HW1.0/diabetes.csv")

print(df.head())

df2 = df[['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']]
dff = df.copy()
dff['MissingValues']=(df2 == 0).T.sum()

print(dff.head())

fig, ax = plt.subplots(figsize=(12,4))

n, bins, patches = ax.hist(dff["MissingValues"], bins=4)
plt.savefig('FreqDist_Missings.png')
