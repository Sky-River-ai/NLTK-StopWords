import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
#Taking on sentence to filter
Sentence = "this is a stop word example on NLTK stop words filteration."

stop_words = set(stopwords.words("english"))

#In sentence differentiating word_tokenize

word_token = word_tokenize(Sentence)
word_token

#Now filtering Sentence

Sentence_Filter = []

for words in word_token:
    if words not in stop_words:
        Sentence_Filter.append(words)

Sentence_Filter







