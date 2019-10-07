text="해당 이메일에서 네이버는 “지난달 12일부터 23일까지 두 번째 클라우드 데이터센터 건립을 희망하는 지자체 및 민간사업자 136곳으로부터 의향서를 받았다”라며 “이후 상세요건이 추가된 최종제안서를 요청했다”고 밝혔다. 네이버에 따르면 최초 의향서를 제출한 136곳 중 96개의 지자체 및 민간사업자가 최종 제안서를 보낸 것으로 확인됐다.(14일 14시 마감 기준) 네이버는 96개의 제안 부지에 대해 서류 심사 및 현장 실사 등을 거쳐 9월 말까지 우선협상부지 선정할 계획이라고 밝혔다. 이어 해당 지자체 및 사업자 분들과의 개별 협의를 거쳐 연내 최종 부지를 확정할 계획이라고 덧붙였다."

#.을기준으로 문장 토큰화
#from nltk.tokenize import sent_tokenize
#text=sent_tokenize(text)
#print(text)

#토큰화(전처리)
from konlpy.tag import Okt
okt=Okt()
#for i in text:
#   token=okt.nouns(i)

#print(token)
words=okt.nouns(text)
print(words)
#을,및,를 등을 불용단어사전을 만들어서 제외시켜야겠음
#print(okt.pos(text))

####################################################
#단어 빈도수 구하기
from collections import Counter
vocab=Counter() # 파이썬의 Counter 모듈을 이용하면 단어의 모든 빈도를 쉽게 계산할 수 있습니다.

for i in words:
    vocab[i] = vocab[i] + 1  # 각 단어의 빈도를 Count 합니다.

print(vocab)

#인덱싱(빈도수에 따라 부여해야하는데 제대로 안됌)
word_to_index={word : index+1 for index, word in enumerate(vocab)}
# 인덱스를 0이 아닌 1부터 부여.
print(word_to_index)
