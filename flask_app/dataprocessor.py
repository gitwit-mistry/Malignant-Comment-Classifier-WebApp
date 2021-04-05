from nltk.stem import PorterStemmer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import stopwords
import string

# creating function to clean data

def rm_punct_sw(x):
  res = [i.lower() for i in x if i not in string.punctuation and i not in ['"',"'",'•',"''",'``'] and i not in stopwords.words('english')]
  return res
def stemmer(x):
  res = [PorterStemmer().stem(i) for i in x]
  return res

  
def data_processor(val):
    #print('S0')
    # tokenize
    S1 = TreebankWordTokenizer().tokenize(val, convert_parentheses=True)
    #print('S1 done')
    # remove punctiaations and stopwords
    S2 = rm_punct_sw(S1)
    #print('S2 done')
    # stemmer
    S3 = stemmer(S2)
    #print('S3 done')
    # reforming the sentences
    S4 = " ".join(S3)
    return S4
