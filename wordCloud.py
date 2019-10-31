from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt



title_list = []

def get_titles():
    f = open("C:/Users/HYERIN/PycharmProjects/untitled/text/merged_travel_place(5827).txt", "r", encoding='utf-8')

    for i in range(1, 210):
        line = f.readline()  # 한 줄씩 읽음.
        if not line: break  # 모두 읽으면 while문 종료.
        title_list.append(line)

    f.close()
    print(title_list)


def make_wordcloud(word_count):
    okt = Okt()

    sentences_tag = []
    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-' * 30)

    print(sentences_tag)
    print('\n' * 3)

    noun_adj_list = []
    # 명사만 구분하여 이스트에 넣기
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun']:
                if word not in ['것', '수', '거', '곳', '저', '안', '제', '더', '때', '이', '진짜', '바로', '정말',
            '여기', '개', '분', '정도', '그', '요', '중', '밤', '그', '요', '중', '위', '나', '내',
            '가장', '게', '점', '좀', '또', '달', '말', '해', '은', '향', '번', '날', '아주', '완전', '꼭', '듯',
            '그냥', '조금', '듯', '층', '사실', '도', '뭐', '살', '살짝', '걸', '쪽', '얼', '만', '꽤', '후']:
                    noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print(tags)

    # wordCloud생성
    # 한글꺠지는 문제 해결하기위해 font_path 지정
    wc = WordCloud(font_path='./NanumSquare.ttf', background_color='white', width=800, height=600)
    print(dict(tags))
    cloud = wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


if __name__ == '__main__':
    #
    get_titles()

    # 단어 30개까지 wordcloud로 출력
    make_wordcloud(100)

