#Importing data
import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
nltk.download('webtext')
wt_sentences = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')
print(len(wt_sentences))
print(len(wt_words))
frequency_dist = nltk.FreqDist(wt_words)

#sort
sorted_frequency_dist =sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)
print(sorted_frequency_dist)
# take word if frequency of it greater than 3
large_words = dict([(k,v) for k,v in frequency_dist.items() if
len(k)>3])
frequency_dist = nltk.FreqDist(large_words)
frequency_dist.plot(10,cumulative=False)




# #build wordcloud
# import WordCloud
# wcloud = WordCloud().generate_from_frequencies(frequency_dist)
# import matplotlib.pyplot as plt
# plt.imshow(wcloud, interpolation='bilinear')
# plt.axis("off")
# (-0.5, 399.5, 199.5, -0.5)
# plt.show()