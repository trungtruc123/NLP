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