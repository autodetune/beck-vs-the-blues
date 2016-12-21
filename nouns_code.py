from __future__ import print_function
import nltk
f = open(‘/path/to/file/file_name.txt')
file_name = f.read()
sentences = nltk.sent_tokenize(file_name)
from nltk.tag import StanfordPOSTagger
st = StanfordPOSTagger(‘/path/to/stanford-postagger/models/english-bidirectional-distsim.tagger’,’//path/to/stanford-postagger/stanford-postagger.jar')
st.tag(sentences)
file_tagged = st.tag(sentences)
nouns= []
for word, pos in file_tagged:
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
		nouns.append(word)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
no_stopnouns = [w for w in nouns if not w in stop_words]
no_stopnouns = []
for w in nouns:
	if w not in stop_words:
		no_stopnouns.append(w)
print(*no_stopnouns,sep='\n')