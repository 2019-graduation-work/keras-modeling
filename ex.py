import numpy
#영어
from nltk.corpus import gutenberg   # Docs from project gutenberg.org
files_en = gutenberg.fileids()      # Get file ids
#doc_en = gutenberg.open('austen-emma.txt').read()
doc_en = "Three people were killed and three injured as an elevator fell at an apartment construction site in Sokcho, Gangwon Province, Wednesday morning, rescue workers and reports said. The three were riding in the elevator when it dropped 15 floors to the ground at 8:28 a.m. The fourth also in the elevator survived the fall and was transported to hospital. The remaining two ― foreign workers from Uzkekistan ― were on the ground and hit by debris when the elevator fell. They were also taken to hospital. All casualties were workers. It was not immediately known what caused one of the two elevators, installed outside the 30-story building, to fall. Police said that the workers were working to dissemble the elevators."

from nltk import regexp_tokenize
pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
tokens_en = regexp_tokenize(doc_en, pattern)

import nltk
en = nltk.Text(tokens_en)

print(len(en.tokens))       # returns number of tokens (document length)
print(len(set(en.tokens)))  # returns number of unique tokens
en.vocab()                  # returns frequency distribution

en.plot(50)     # Plot sorted frequency of top 50 tokens

#한국어
from konlpy.corpus import kobill    # Docs from pokr.kr/bill
files_ko = kobill.fileids()         # Get file ids
doc_ko = kobill.open('1809890.txt').read()

from konlpy.tag import Okt
okt= Okt()
tokens_ko = okt.morphs(doc_ko)

import nltk
ko = nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')   # For Pyt# hon 2, input `name` as u'유니코드'

print(len(ko.tokens))       # returns number of tokens (document length)
print(len(set(ko.tokens)))  # returns number of unique tokens
ko.vocab()                  # returns frequency distribution

ko.plot(50)     # Plot sorted frequency of top 50 tokens

