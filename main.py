'Pandas'
import pandas as pd
import matplotlib as plt

df = pd.read_csv("/workspaces/DS-HW1.0/diabetes.csv")

print(df.head())

df2 = df[['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']]
dff = df.copy()
dff['MissingValues']=(df2 == 0).T.sum()

print(dff.head())

plt.hist(dff)
plt.show()
