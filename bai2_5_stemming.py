import pandas as pd
from nltk.stem import PorterStemmer
text=['I like fishing','I eat fish','There are many fishes in pound']

df = pd.DataFrame({'text':text})
# print(df) 
st = PorterStemmer()
df['text'][:5].apply(lambda x:" ".join([st.stem(word) for word in x.split()]))
