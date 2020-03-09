text=['I like fishing','I eat fish','There are many fishes inpound', 'leaves and leaf']
#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
#print(df)
from textblob import Word
#Code for lemmatize
df['tweet'] = df['tweet'].apply(lambda x:" ".join([Word(word).lemmatize() for word in x.split()]) )
print(df)