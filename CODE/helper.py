# -*- coding: utf-8 -*-

from gensim.test.utils import common_texts
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from gensim.models import Word2Vec
from nltk.corpus import treebank
import numpy as np

def tokenize(df):
  nltk.download('punkt')
  tokens=df.apply(nltk.word_tokenize)
  return tokens

"""Tags"""

def tags(df):
  nltk.download('averaged_perceptron_tagger')
  tokens=tokenize(df)
  tags=tokens.apply(nltk.pos_tag)
  return tags

"""Stemming"""

def Stemming(df):
  stemmed=pd.DataFrame()
  tokens=tokenize(df)
  stem=nltk.PorterStemmer()
  stemmed = tokens.apply(lambda x: [stem.stem(y) for y in x])
  return stemmed

def Lemmatizer(df):
  lemmatized=pd.DataFrame()
  nltk.download('wordnet')
  tokens=tokenize(df)
  lemma=nltk.stem.WordNetLemmatizer()
  lemmatized = tokens.apply(lambda x: [lemma.lemmatize(y) for y in x])
  return lemmatized

def remove_stopwords(df):
  nltk.download('stopwords')
  stopwords=set(nltk.corpus.stopwords.words('english'))
  tokens=tokenize(df)
  new_text=pd.DataFrame()
  new_text=tokens.apply(lambda x: ' '.join([word for word in x if word.lower() not in stopwords]))
  return new_text

def ngrams(df,n):
  ngrams=pd.DataFrame()
  tokens=tokenize(df)
  ngrams=tokens.apply(nltk.ngrams, args=(n,))
  return ngrams

def word2vec(df,sg):
  #!pip install gensim
  def doc_vector(model,doc):
    word_vec=[model.wv[word] for word in doc if word in model.wv]
    if not word_vec:
      return np.zeros(model.vector_size)
    doc_vec=np.mean(word_vec,axis=0)
    return doc_vec

  #tokens=tokenize(df)
  model=Word2Vec(df,vector_size=100, window=4,sg=sg,min_count=1)#sg=0 CBOW and 1 for Skipgram
  #doc_vector=df.apply(lambda x: doc_vector(model,x.split()))
  doc_vector=[doc_vector(model,token) for token in df]
  return doc_vector