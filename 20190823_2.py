#https://wikidocs.net/22660
#Word2Vec 모델 만드는 방법
f = open('C:/Users/HYERIN/PycharmProjects/untitled/wiki_data.txt', encoding="utf8")
#다섯줄출력
i=0
while True:
    line = f.readline()
    if line != '\n':
        i=i+1
        print("%d번째 줄 :"%i + line)
    if i==5:
        break
f.close()

########################333
from konlpy.tag import Okt
okt=Okt()
fread = open('C:/Users/HYERIN/PycharmProjects/untitled/wiki_data.txt', encoding="utf8")
# 파일을 다시 처음부터 읽음.
n=0
result = []

while True:
    line = fread.readline() #한 줄씩 읽음.
    if not line: break # 모두 읽으면 while문 종료.
    n=n+1
    if n%5000==0: # 5,000의 배수로 While문이 실행될 때마다 몇 번째 While문 실행인지 출력.
        print("%d번째 While문."%n)
    tokenlist = okt.pos(line, stem=True, norm=True) # 단어 토큰화
    temp=[]
    for word in tokenlist:
        if word[1] in ["Noun"]: # 명사일 때만
            temp.append((word[0])) # 해당 단어를 저장함

    if temp: # 만약 이번에 읽은 데이터에 명사가 존재할 경우에만
      result.append(temp) # 결과에 저장
fread.close()
#약 240만여개의 줄(line)이 명사 토큰화가 되어 저장되어 있는 상태입니다. 이제 이를 Word2Vec으로 학습시킵니다.
from gensim.models import Word2Vec
model = Word2Vec(result, size=100, window=5, min_count=5, workers=4, sg=0)
#학습을 다했다면 이제 임의의 입력 단어로부터 유사한 단어들을 구해봅시다.
