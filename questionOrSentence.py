import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import os

with open('classification.txt', 'r') as questions:
    questionsclassificaion = questions.read()
    with open('classificationsentences.txt', 'r') as sentences:
        sentenceclassification = sentences.read()
inputSentence = 1
while(inputSentence != 'exit'):
    print("Please enter a Sentence")
    inputSentence =  input()
    training = "Barak Obama Lives in the White House? This is Awesome!"

    mysentence_tokenizer = PunktSentenceTokenizer(training)
    Tagged = []
    tokenizedsentence = mysentence_tokenizer.tokenize(inputSentence)
    for i in tokenizedsentence:
        tokenwords = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(tokenwords)
        Tagged.append(tagged)
    trigramsfound = []
    for i in Tagged:
        templist = []
        for j in i:
            templist.append(j[1])

        trigram = ngrams(templist, 3)
        for k in trigram:
            trigramsfound.append(k)
    print(trigramsfound)

    print(questionsclassificaion)