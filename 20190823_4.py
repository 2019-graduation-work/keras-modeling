#https://wikidocs.net/33793
#케라스의 Embedding 사용

#20190830 추가
f = open("C:/Users/HYERIN/PycharmProjects/untitled/crawl_blog_travel2.txt","r", encoding='utf-8')
content = []
title = []
y_train = []
sentences = []
for i in range(1,210):
    line = f.readline() #한 줄씩 읽음.
    if not line: break # 모두 읽으면 while문 종료.
    if i < 161:
        sentences.append(line)
        y_train.append(1)
    else:
        content.append(line)
        title.append(1)

f.close()
f2 = open("C:/Users/HYERIN/PycharmProjects/untitled/crawl_blog_travel2.txt","r", encoding='utf-8')
for i in range(1,210):
    line = f2.readline() #한 줄씩 읽음.
    if not line: break # 모두 읽으면 while문 종료.
    if i < 161:
        sentences.append(line)
        y_train.append(1)
    else:
        content.append(line)
        title.append(1)

f2.close()



#문장의 긍정, 부정을 판단하는 간단한 감성 분류 모델을 만들어보겠습니다.
#sentences = ['에너지 넘치는 여행의 중심엔 액티비티가 있죠! 특히 스포츠의 천국이라고 불리는 괌은 해양 스포츠와 다양한 액티비티를 즐기려는 여행객들에게 꾸준히 사랑받는 여행지랍니다!그래서 오늘은! 괌으로 떠나는 여행객들을 위해 괌 추천 액티비티 TOP 5를 소개합니다!괌 육해공에서 즐길 수 있는 액티비티같이 살펴 보실까요~?',
#             '정밀 진단을 통해서는 소득이나 저축, 재산 등을 입력해 좀 더 정확하고 개인적인 재무 진단을 받아볼 수 있습니다. ',
 #            '이번엔 신용 정보를 조회하고 관리해주는 서비스들을 추천해드리겠습니다. 신용등급은 떨어지는 건 한순간이지만 다시 올리려면 시간과 노력이 필요하기 때문에 지속적으로 관리를 해야 합니다.',
  #           '괌의 대자연을 온몸으로 느끼고 싶다면 오프로드 ATV 정글 투어호텔에서 벗어나 자연으로 떠나고 싶은 여행자라면 4륜 버기카를 타고 괌 정글을 탐험해보는 것을 추천!전문 드라이버가 운전하는 ATV 차량을 타고 오프로드를 온몸으로 느끼는 체험은 괌에서 특별한 추억이 될 거예요^^4. 괌 하늘을 자유롭게 날아 보고 싶다면 스카이다이빙이 정답',
   #          '오늘은 #코타키나발루여행 마지막 프롤로그를 가져왔어요~곱씹을수록 알차고 재밌게 놀다 왔구나를 느끼며~.~코타키나발루 3박5일의 마지막 날을 포스팅 합니당 !4일째 되는 날인데 비행기가 5일째되는날 새벽에 떠서 정말 하루종일 알참 ^^아침에 일어나니 보이는 #하얏트리젠시 뷰~.~ 크!',
    #         '재테크를 하다 보면 선택의 기로에 서는 순간들이 있습니다. 적금이 끝난 시점이나 보험이 만기 된 시점 등이 이에 해당하는데요. 이때 다른 상품을 선택한다면 어떤 상품을 선택해야 할지',
     #        '관광지 구경할라면 꼭 시내투어 신청하시길 ^^..진짜 관광지가 다 가깝긴 한데 떠죽어서 못다닐거 같음..프라이빗 투어에다가 투어시간도 유동적으로 할 수 있고영어 설명에 픽업, 드랍은 물론 선셋까지 볼 수 있어서 #코타키나발루시내투어 강추 ! 첫번째로 유명한 #블루모스크 를 가려고했는데 입장시간이 변경 되는 바람에중국사원 을 먼저가게 되었어요']
#y_train = [1, 0, 0, 1, 1, 0, 1]

#senten = ['코타키나발루 호텔에서의 석양','제태크란 무엇인가']
#y_test=[1, 0]

#문장과 레이블 데이터를 만들었습니다.
from keras.preprocessing.text import Tokenizer
t = Tokenizer()
t.fit_on_texts(sentences)
vocab_size = len(t.word_index) + 1

print(vocab_size)
t.fit_on_texts(content)
vocab_size = len(t.word_index) + 1
print(vocab_size)
#케라스의 Tokenizer()를 사용하여 토큰화를 시켰습니다.
X_encoded = t.texts_to_sequences(sentences)
print(X_encoded)

#각 문장에 대해서 정수 인코딩을 수행합니다.
max_len=max(len(l) for l in X_encoded)
print(max_len)
#모든 문장을 패딩하여 길이를 4로 만들어줍니다.
from keras.preprocessing.sequence import pad_sequences
X_train=pad_sequences(X_encoded, maxlen=max_len, padding='post')
print(X_train)

#출력층에 1개의 뉴런에 활성화 함수로는 시그모이드 함수를 사용하여 이진 분류를 수행합니다.
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(vocab_size, 4, input_length=max_len)) # 모든 임베딩 벡터는 4차원을 가지게됨.
model.add(Flatten()) # Dense의 입력으로 넣기위함임.
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

model.fit(X_train, y_train, epochs=100, verbose=2)

#TEST
#케라스의 Tokenizer()를 사용하여 토큰화를 시켰습니다.
Xt_encoded = t.texts_to_sequences(content)
print(Xt_encoded)
#각 문장에 대해서 정수 인코딩을 수행합니다.
max_l=max(len(l) for l in Xt_encoded)
print(max_l)
#모든 문장을 패딩하여 길이를 4로 만들어줍니다.
X_test=pad_sequences(Xt_encoded, maxlen=max_len, padding='post')
print(X_test)

model.evaluate(X_test, title, batch_size=32)
model.predict(X_test, batch_size=32)