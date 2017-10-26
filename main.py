import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk import corpus
from nltk.corpus import brown

training = "Barak Obama Lives in the White House? Who else lives in the White House?"
mysentence = "Who is the owner of White House? Have you been to White House?"

#stop words:
stop_words = set(stopwords.words("english"))
words = word_tokenize(mysentence)
filtered_sentence = []
for i in words:
    if( i not in stop_words):
        filtered_sentence.append(i)
print(filtered_sentence)



#parts of speech tagging
mysentence_tokenizer = PunktSentenceTokenizer(training)
#tokenizing sentence, in this case there is only one sentence
tokenizedsentence = mysentence_tokenizer.tokenize(mysentence)
for i in tokenizedsentence:
    tokenwords = nltk.word_tokenize(i)
    #print(tokenwords)
    tagged = nltk.pos_tag(tokenwords)
    print(tagged)



brown_text = (nltk.Text(word for word in nltk.corpus.brown.words()))
print(brown_text.similar('ship'))
brown_train = brown.tagged_sents(categories='news')
print(brown_train)







