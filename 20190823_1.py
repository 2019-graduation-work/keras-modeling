#https://wikidocs.net/33793
#케라스 임베딩 층 예제
sentences = ['멋있어 최고야 짱이야 감탄이다', '헛소리 지껄이네', '닥쳐 자식아', '우와 대단하다', '우수한 성적', '형편없다', '최상의 퀄리티']
y_train = [1, 0, 0, 1, 1, 0, 1]
#문장과 레이블 데이터를 만들었습니다.
from keras.preprocessing.text import Tokenizer
t = Tokenizer()
t.fit_on_texts(sentences)
vocab_size = len(t.word_index) + 1

print(vocab_size)
#케라스의 Tokenizer()를 사용하여 토큰화를 시켰습니다.
X_encoded = t.texts_to_sequences(sentences)
print(X_encoded)
#각 문장에 대해서 정수 인코딩을 수행합니다.
max_len=max(len(l) for l in X_encoded)
print(max_len)
#문장 중에서 가장 길이가 긴 문장의 길이는 4입니다.
from keras.preprocessing.sequence import pad_sequences
X_train=pad_sequences(X_encoded, maxlen=max_len, padding='post')
print(X_train)
#모든 문장의 길이를 패딩하여 길이를 4로 만들어 주었습니다.
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(vocab_size, 4, input_length=max_len)) # 모든 임베딩 벡터는 4차원을 가지게됨.
model.add(Flatten()) # Dense의 입력으로 넣기위함임.
model.add(Dense(1, activation='sigmoid'))
#출력층에 1개의 뉴런에 활성화 함수로는 시그모이드 함수를 사용하여 이진 분류를 수행합니다.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(X_train, y_train, epochs=100, verbose=2)
