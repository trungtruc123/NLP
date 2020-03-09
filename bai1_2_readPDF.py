import PyPDF2
from PyPDF2 import PdfFileReader
#Creating a pdf file object
#pdf = open("‪E:/TailieuNLP/deep_learning_for_nlp.pdf","rb")
#creating pdf reader object
pdf_reader = PyPDF2.PdfFileReader('E:/TailieuNLP/deep_learning_for_nlp.pdf')

#checking number of pages in a pdf file
print(pdf_reader.numPages)
#creating a page object
page = pdf_reader.getPage(2)
#finally extracting text from the page
print(page.extractText())
#closing the pdf file
#pdf.close()