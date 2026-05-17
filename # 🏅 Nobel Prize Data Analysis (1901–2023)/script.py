# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Start coding here!

# this code loads the dataset and finds the most common gender and birth country among all winners
df = pd.read_csv('data/nobel.csv')
#sns.catplot(x='sex',data=df,kind='count')
plt.show()
top_gender = df['sex'].value_counts().idxmax()
top_country = df['birth_country'].value_counts().idxmax()
df.columns

# this code finds the decade where the proportion of US-born nobel prize winners was the highest

df['Flag'] = np.where(df['birth_country'] == 'United States of America',1,0)
df['decade'] = (df['year'] // 10) * 10
max_decade_usa = df.groupby('decade')['Flag'].mean().idxmax()

                     

# this code finds the decade and category combination with the highest proportion of female nobel prize winners


df['female_winner'] = np.where(df['sex'] == 'Female',1,0 )
female_winner = df.groupby(['decade','category'],as_index=False)['female_winner'].mean()
female_winner = female_winner.sort_values(by='female_winner', ascending=False)
max_female_dict = {female_winner['decade'].values[0]:female_winner['category'].values[0]}
max_female_dict

# this code finds the first woman to win a nobel prize and the category she won it in

women = df[df['sex'] == 'Female']

first_woman = women[['full_name', 'category', 'year']].sort_values('year').reset_index(drop=True).iloc[0, :]
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']
print(first_woman_category, first_woman_name)

# this code builds a list of all laureates who have won the nobel prize more than once

count = df.groupby('full_name',as_index=False)['full_name'].value_counts()
count2 = count.sort_values(by='count',ascending=False).reset_index(drop=True)
count3 = count[count['count'] >= 2]
repeat_list = count3['full_name'].tolist()
repeat_list

