'import pandas, matplotlib, and seaborn'
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from scipy.stats import chi2_contingency


#read in data
df = pd.read_csv("diabetes.csv")
ListVars = ['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']

#Question 1

def question_1_1():
    #Part 1 and 2: Histograms of Missingness Per Record

    #make missing value counter
    df2 = df[['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']]
    dff = df.copy()
    dff['MissingValues']=(df2 == 0).T.sum()

    df_outcome1 = dff[dff['Outcome'] == 0]
    df_outcome0 = dff[dff['Outcome'] == 1]

    def plot(df,filename):
        '''
        plot number of missings per record frequency distribution
        '''
        sns.displot(df['MissingValues'],kde=False,discrete = True)
        plt.xlabel('Number of Missings Per Record')
        plt.ylabel('Count of Records')
        plt.savefig(filename)

    plot(dff,"FreqDist_Missings2.png")
    plot(df_outcome1,"FreqDist_Missings_Out1.png")
    plot(df_outcome0,"FreqDist_Missings_Out0.png")

def question_1_3():
    #Part 3: Conditional Probability
    FinalOutput = [[0 for i in range(5)] for i in range(5)]
    print(FinalOutput)

    for indexa, vara in enumerate(ListVars):
        for indexb, varb in enumerate(ListVars):
            # P(A and B)
            p_a_and_b = len(df[(df[vara] == 0) & (df[varb] == 0)]) / len(df)

            # P(B)
            p_b = len(df[df[varb] == 0]) / len(df)

            # P(A|B)
            finalprob = p_a_and_b / p_b

            FinalOutput[indexa][indexb] = finalprob

    df_output = pd.DataFrame(FinalOutput, columns=ListVars, index = ListVars)



def question1_4 ():
    #Part 4

    #loop through each of the five variables and turn it into a boolean
    dff1_4 = df[['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']]
    dff1_4 = dff1_4.map(lambda x: 1 if x != 0 else 0)

    FinalOutput1_4 = [[0 for i in range(5)] for i in range(5)]
    for i in ListVars:
        for j in ListVars:
            contigency= pd.crosstab(df['Glucose'], df['BloodPressure'])
            print(contigency)

            #c, p, dof, expected = chi2_contingency(contigency)
            #print(p)

            #FinalOutput1_4[i][j] = p

    #df_output = pd.DataFrame(FinalOutput1_4, columns=ListVars, index = ListVars)


#question 2

def sample_population(N, n):
    ''' select into sample'''
    sample_size = 0
    for _ in range(N):
        inclusion_prob = n / N
        if random.random() <= inclusion_prob:
            sample_size += 1
    return sample_size

def simulate_sampling(N, n, num_simulations):
    '''simulate sampling at scale'''
    sample_sizes = []
    for _ in range(num_simulations):
        sample = sample_population(N, n)
        sample_sizes.append(sample)
    
    return sample_sizes

BIGN = 10000  # Population size
SMALLN = 100    # Desired sample size
SIMS = 100

sample_sizes_off = simulate_sampling(BIGN, SMALLN, SIMS)

sns.displot(sample_sizes_off,kde=False,discrete = True)
plt.xlabel('Number of Units in Sample')
plt.ylabel('Number of Samples')
plt.title('Distribution of Sample Sizes')
plt.savefig('test2.png')

print(sample_sizes_off)

#question 2