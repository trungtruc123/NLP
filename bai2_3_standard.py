import re
lookup = { 'nlp':'nature learning proccessing','ur':'tran trung truc...','y':' year'}

input_text =' ur learn NLP y 2019......'
def text_std(input_text):
    words = input_text.split()
    new_word =[]
    for word in words:
        word = re.sub(r'[^\w\s]'," ",word)
        if word.lower() in lookup:
            word = lookup[word.lower()]
            new_word.append(word)
            new_text = "".join(new_word)
    return new_text
print(text_std(input_text))