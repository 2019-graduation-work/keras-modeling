text="A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

#문장 토큰화
from nltk.tokenize import sent_tokenize
text=sent_tokenize(text)
print(text)

#전처리
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
vocab=Counter() # 파이썬의 Counter 모듈을 이용하면 단어의 모든 빈도를 쉽게 계산할 수 있습니다.

sentences = []
stop_words = set(stopwords.words('english'))

for i in text:
    sentence=word_tokenize(i) # 단어 토큰화를 수행합니다.
    result = []

    for word in sentence:
        word=word.lower() # 모든 단어를 소문자화하여 단어의 개수를 줄입니다.
        if word not in stop_words: # 단어 토큰화 된 결과에 대해서 불용어를 제거합니다.
            if len(word) > 2: # 단어 길이가 2이하인 경우에 대하여 추가로 단어를 제거합니다.
                result.append(word)
                vocab[word]=vocab[word]+1 #각 단어의 빈도를 Count 합니다.
    sentences.append(result)
print(sentences)

print(vocab)

#빈도수 순 정렬
vocab_sorted=sorted(vocab.items(), key=lambda x:x[1], reverse=True)
print(vocab_sorted)

#빈도수 순으로 인덱스 부여
word_to_index={}
i=0
for (word, frequency) in vocab_sorted :
    if frequency > 1 : # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
        i=i+1
        word_to_index[word]=i
print(word_to_index)

#함수이용 인덱스 부여
word_to_index={word : index+1 for index, word in enumerate(vocab)}
# 인덱스를 0이 아닌 1부터 부여.
print(word_to_index)
#######################
text=[['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

vocab=sum(text, [])
print(vocab)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
vocab=Counter() # 파이썬의 Counter 모듈을 이용하면 단어의 모든 빈도를 쉽게 계산할 수 있습니다.
stop_words = set(stopwords.words('english'))
for word in sentence:
  word=word.lower() # 모든 단어를 소문자화하여 단어의 개수를 줄입니다.
  if word not in stop_words: # 단어 토큰화 된 결과에 대해서 불용어를 제거합니다.
    vocab[word]=vocab[word]+1 #각 단어의 빈도를 Count 합니다.
print(vocab)

word_to_index={word : index+1 for index, word in enumerate(vocab)}
# 인덱스를 0이 아닌 1부터 부여.
print(word_to_index)

################
#불용어
import nltk
from nltk.corpus import stopwords
stopwords.words('english')[:10]

from konlpy.tag import Okt
okt=Okt()
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

