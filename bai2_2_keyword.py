import pandas as pd
import nltk
#nltk.download()
from nltk.corpus import stopwords
text=['This is introduction to NLP','It is likely to be useful,to people ','Machine learning is the new electrcity',
'There would be less hype around AI and more action goingforward','python is the best tool!','R is good langauage','I likethis book','I want more books like this']

# covert data frame
df = pd.DataFrame({'text':text})
print(df)
#remove stop words
stop = stopwords.words('english')
df['text'] =df['text'].apply(lambda x:" ".join(x for x in x.split() if x not in stop))
print(df)