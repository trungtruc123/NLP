# Import library
import re
import requests
#url you want to extract
url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
#function to extract
def get_book(url):
# Sends a http request to get the text from project
    raw = requests.get(url).text
# Discards the metadata from the beginning of the book( loai bo <html></html>...)
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
# Discards the metadata from the end of the book ( loai bo <html></html>...)
    stop = re.search(r"II", raw).start()
# Keeps the relevant text
    text = raw[start:stop]
    return text
# processing ( replace cac ky tu dac biet bang ' ')
def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()
#calling the above function
book = get_book(url)
processed_book = preprocess(book)
print(processed_book)
# Count number of times "the" is appeared in the book
print(len(re.findall(r'the', processed_book)))
#Replace "i" with "I"
processed_book = re.sub(r'\si\s', " I ", processed_book)
print(processed_book)
#find all occurance of text in the format "abc--xyz"
re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book)