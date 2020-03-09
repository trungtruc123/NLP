import docx
from docx import Document

#Creating a word file object
#doc = open("file.docx","rb")
#creating word reader object
document = docx.Document('‪E:/TailieuNLP/fileWord.docx')
# create an empty string and call this document. This document variable store each paragraph in the Word document.We then create a for loop that goes through each paragraph in the Word document and appends the paragraph.

String =""
for para in document.paragraphs:
    String +=para.text
print(String)