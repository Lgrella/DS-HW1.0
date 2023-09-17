'import pandas, matplotlib, and seaborn'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read in data
df = pd.read_csv("/workspaces/DS-HW1.0/diabetes.csv")

#make missing value counter
df2 = df[['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']]
dff = df.copy()
dff['MissingValues']=(df2 == 0).T.sum()

#plot missing value counter
sns.displot(dff['MissingValues'],kde=False,discrete = True)
plt.xlabel('Number of Missings Per Record')
plt.savefig('FreqDist_Missings2.png')

df_outcome1 = dff[dff['Outcome'] == 0]
df_outcome0 = dff[dff['Outcome'] == 1]

sns.displot(df_outcome1['MissingValues'],kde=False,discrete = True)
plt.xlabel('Number of Missings Per Record')
plt.savefig('FreqDist_Missings_Out1.png')

sns.displot(df_outcome0['MissingValues'],kde=False,discrete = True)
plt.xlabel('Number of Missings Per Record')
plt.savefig('FreqDist_Missings_Out0.png')