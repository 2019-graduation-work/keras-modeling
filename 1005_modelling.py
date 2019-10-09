#https://wikidocs.net/33793
#케라스의 Embedding 사용
#이진분류
sentence = [] #문장
category = [] #카테고리

f = open("C:/Users/HYERIN/PycharmProjects/untitled/text/desrt(1006).txt","r", encoding='utf-8')
list1 = []
for i in range(1,10000):
    line = f.readline() #한 줄씩 읽음.
    list1.append(line)
    if not line: break # 모두 읽으면 while문 종료.

f.close()

import re
from konlpy.tag import Okt
okt=Okt()
list2=[]
a=0;
for n in list1:
    a=a+1
    print(a)
    #n = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', n)
    n = re.sub('[^ㄱ-ㅣ가-힝0-9a-zA-Z\\s]', '', n) #특수문자제거를 위해 한글과 알파벳만 남기기.
    temp = okt.nouns(n) #명사추출
    list2.append(temp)

#불용어제거 -> 추가해야함
stop_words = ['것', '수', '거', '곳', '저', '안', '제', '더', '때', '이', '진짜', '바로', '정말',
            '여기', '개', '분', '정도', '그', '요', '중', '밤', '그', '요', '중', '위', '나', '내',
            '가장', '게', '점', '좀', '또', '달', '말', '해', '은', '향', '번', '날', '아주', '완전', '꼭', '듯',
            '그냥', '조금', '듯', '층', '사실', '도', '뭐', '살', '살짝', '걸', '쪽', '얼', '만', '꽤', '후']
list3=[]
for word in list2:
    temp = [each_word for each_word in word if each_word not in stop_words]
    if temp: # temp에 결과가 존재할 경우에만
        list3.append(temp)

'''
#아래의 코드는 불용어를 찾기위해 빈도수대로 출력한것
words = [element for array in list3 for element in array]
words_count={}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_words = sorted([(k,v) for k,v in words_count.items()], key=lambda word_count: -word_count[1])
count = [w[0] for w in sorted_words]
print(count) #빈도수대로 단어 나열한 리스트
'''

sentence = sentence + list3
cate = [1 for i in range(len(list3))]
category = category + cate
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
min_len=min(len(l) for l in X_encoded)
print(max_len)
print(min_len)

max_len = 500 #?
#모든 문장을 패딩하여 길이 최대 길이로 만들어줍니다.
from keras.preprocessing.sequence import pad_sequences
predData = pad_sequences(X_encoded, maxlen=max_len, padding='post')
print(predData)

#train 데이터와 test 데이터로 나누어줍니다.
import numpy as np
from sklearn.model_selection import train_test_split
X_train, X_test, train_labels, test_labels = train_test_split(predData, category, test_size=0.33, random_state=321) #3,4번째 인자 바꾸어주면됨
from keras.utils.np_utils import to_categorical
Y_train = to_categorical(train_labels) # 라벨데이터 원 핫 인코딩(0-9사이의값(?))
Y_test = to_categorical(test_labels)

#MODEL
from keras.models import Sequential
from keras.layers import Dense
# 2. 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=1, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(X_train, Y_train, epochs=10, batch_size=100, verbose=2) #epochs 반복횟수, batch_size 한번에 보는 데이터 횟수
#https://snowdeer.github.io/machine-learning/2018/01/11/keras-model-fit-options/

# 5. 학습과정 확인하기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.set_ylim([0.0, 3.0])
acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))

#TEST
model.evaluate(X_test, Y_test, batch_size=32)
model.predict(X_test, batch_size=32)


