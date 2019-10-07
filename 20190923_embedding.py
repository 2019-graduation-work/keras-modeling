#https://wikidocs.net/33793
#케라스의 Embedding 사용
#이진분류

sentence = [] #문장
category = [] #카테고리
#중복제거와 명사추출 필요.

#문장과 레이블 데이터를 만들었습니다.
from keras.preprocessing.text import Tokenizer
t = Tokenizer()
t.fit_on_texts(sentence)
vocab_size = len(t.word_index) + 1

print(vocab_size)

#케라스의 Tokenizer()를 사용하여 토큰화를 시켰습니다.
X_encoded = t.texts_to_sequences(sentence)
print(X_encoded)

#각 문장에 대해서 정수 인코딩을 수행합니다. # 최대길이가 너무 길면 수정 필요.
max_len=max(len(l) for l in X_encoded)
print(max_len)

#모든 문장을 패딩하여 길이 최대 길이로 만들어줍니다.
from keras.preprocessing.sequence import pad_sequences
predData = pad_sequences(X_encoded, maxlen=max_len, padding='post')
print(predData)

#train 데이터와 test 데이터로 나누어줍니다.
import numpy as np
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(predData, category, test_size=0.33, random_state=321) #3,4번째 인자 바꾸어주면됨


#출력층에 1개의 뉴런에 활성화 함수로는 시그모이드 함수를 사용하여 이진 분류를 수행합니다.
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(vocab_size, 4, input_length=max_len)) # 모든 임베딩 벡터는 4차원을 가지게됨.
model.add(Flatten()) # Dense의 입력으로 넣기위함임.
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

model.fit(X_train, Y_train, epochs=100, verbose=2)



#TEST
model.evaluate(X_test, Y_test, batch_size=32)
model.predict(X_test, batch_size=32)