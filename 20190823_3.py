from konlpy.tag import Okt
okt=Okt()
fread = open('C:/Users/HYERIN/Downloads/trip_test.txt', encoding="utf8")
# 파일을 다시 처음부터 읽음.
n=0
result = []

while True:
    line = fread.readline() #한 줄씩 읽음.
    if not line: break # 모두 읽으면 while문 종료.
    n=n+1
    if n%50==0: # 5,0의 배수로 While문이 실행될 때마다 몇 번째 While문 실행인지 출력.
        print("%d번째 While문."%n)
    tokenlist = okt.pos(line, stem=True, norm=True) # 단어 토큰화
    temp=[]
    for word in tokenlist:
        if word[1] in ["Noun"]: # 명사일 때만
            temp.append((word[0])) # 해당 단어를 저장함

    if temp: # 만약 이번에 읽은 데이터에 명사가 존재할 경우에만
      result.append(temp) # 결과에 저장
fread.close()


from gensim.models import Word2Vec

embedding_model = Word2Vec(result, size=100, window=2, min_count=5, workers=4, sg=1) #min_count를 데어터가 많으면 높여야함
embedding_model.wv.save_word2vec_format('word2vec.txt', binary=False)
print(embedding_model.most_similar(positive=["여행"], topn=10))

word_vectors = embedding_model.wv
vocabs = word_vectors.vocab.keys()
word_vector_list = [word_vectors[v] for v in vocabs]
print(embedding_model.wv.vocab)
print(embedding_model.wv["시간"])
word = "시간"
embedding_model.wv.vocab