import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import os
with open('questions.txt','r') as questionsFile:
    questionscorpora = questionsFile.read()

training = "Barak Obama Lives in the White House? Who else lives in the White House?"

#print(questionscorpora)

mysentence_tokenizer = PunktSentenceTokenizer(training)
questionsTagged = []
tokenizedsentence = mysentence_tokenizer.tokenize(questionscorpora)
for i in tokenizedsentence:
    tokenwords = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(tokenwords)
    questionsTagged.append(tagged)
f = open('classification.txt', 'a')
#print(questionsTagged)
trigramsfound = []
for i in questionsTagged:
    templist=[]
    for j in i:
        templist.append(j[1])

    trigram = ngrams(templist,3)
    for k in trigram:
        trigramsfound.append(k)









tagfrequency = nltk.FreqDist(item for item in trigramsfound )
FrequencyQuestions = tagfrequency.most_common()
for item in FrequencyQuestions:
    f.write('{} {} {}'.format(item, 'q', '\n'))



f = open('classificationbigram.txt', 'a')
#print(questionsTagged)
bigramsfound = []
for i in questionsTagged:
    templist=[]
    for j in i:
        templist.append(j[1])

    bigram = ngrams(templist,2)
    for k in bigram:
        bigramsfound.append(k)


tagfrequency = nltk.FreqDist(item for item in bigramsfound )
FrequencyQuestions = tagfrequency.most_common()
for item in FrequencyQuestions:
    f.write('{} {} {}'.format(item, 'q', '\n'))

f.close()



















with open('statements.txt','r') as statementsFile:
    statementscorpora = statementsFile.read()

trainingstatement = "Barak Obama Lives in the White House. It's a very nice place!"

#print(questionscorpora)

mysentence_tokenizer = PunktSentenceTokenizer(trainingstatement)
statementsTagged = []
tokenizedsentence = mysentence_tokenizer.tokenize(statementscorpora)
for i in tokenizedsentence:
    tokenwords = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(tokenwords)
    statementsTagged.append(tagged)
f = open('classification.txt', 'a')
#print(questionsTagged)
trigramsfound = []
for i in statementsTagged:
    templist=[]
    for j in i:
        templist.append(j[1])

    trigram = ngrams(templist,3)
    for k in trigram:
        trigramsfound.append(k)




tagfrequency = nltk.FreqDist(item for item in trigramsfound )
FrequencyStatements = tagfrequency.most_common()
for item in FrequencyStatements:
    f.write('{} {} {}'.format(item, 's', '\n'))


for i in tokenizedsentence:
    tokenwords = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(tokenwords)
    statementsTagged.append(tagged)
f = open('classificationbigram.txt', 'a')
#print(questionsTagged)
bigramsfound = []
for i in statementsTagged:
    templist=[]
    for j in i:
        templist.append(j[1])

    trigram = ngrams(templist,2)
    for k in bigram:
        bigramsfound.append(k)









tagfrequency = nltk.FreqDist(item for item in bigramsfound )
FrequencyStatements = tagfrequency.most_common()
for item in FrequencyStatements:
    f.write('{} {} {}'.format(item, 's', '\n'))



f.close()











