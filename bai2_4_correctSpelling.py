from textblob import TextBlob
import pandas as pd

text=['Introduction to NLP','It is likely to be useful, topeople ','Machine learning is the new electrcity', 'R is goodlangauage','I like this book','I want more books like this']
#convert list to dataframe

df = pd.DataFrame({'tweet':text})

# sua loi chinh ta : electricity,language
df['tweet'].apply(lambda x: str(TextBlob(x).correct()))
print(df)
string =' I am tran trung truc'
print(string.split())
print(TextBlob(df['tweet'][3]).words)