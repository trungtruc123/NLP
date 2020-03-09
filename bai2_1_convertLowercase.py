import pandas as pd
import re
text=['Tran Trung Truc...','23 tuoi','Tam thanh tam ki Quang nam']
# data frame
df = pd.DataFrame({'text':text})
print(df)
# lower(): convert 1 data frame to lowercase
df['text'] = df['text'].apply(lambda x: " ".join(x.lower()for x in x.split()))
print(df)
s= 'I .like . a book'
s1 = re.sub(r'[^\w\s]',"",s)
print(s1)
df['text']= df['text'].str.replace('[^\w\s]',"")
print (df)
import string
s2 = "I. like. This ngu!"
for c in string.punctuation:
 s2= s2.replace(c,"")
print(s2)