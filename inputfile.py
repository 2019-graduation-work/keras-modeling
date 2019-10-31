sentence = [] #문장
category = [] #카테고리
vocab_size = 0
def read_file(file_name,index):
    import re
    from konlpy.tag import Okt
    global sentence,category
    f = open(file_name, "r", encoding='utf-8')
    list1 = []
    okt = Okt()
    for line in f:
        line = f.readline()  # 한 줄씩 읽음.
        line = re.sub('[^ㄱ-ㅣ가-힝0-9a-zA-Z\\s]', '', line)  # 특수문자제거를 위해 한글과 알파벳만 남기기.
        noun = okt.nouns(line)  # 명사추출
        stop_words = ['것', '수', '거', '곳', '저', '안', '제', '더', '때', '이', '진짜', '바로', '정말',
                      '여기', '개', '분', '정도', '그', '요', '중', '밤', '그', '요', '중', '위', '나', '내',
                      '가장', '게', '점', '좀', '또', '달', '말', '해', '은', '향', '번', '날', '아주', '완전', '꼭', '듯',
                      '그냥', '조금', '듯', '층', '사실', '도', '뭐', '살', '살짝', '걸', '쪽', '얼', '만', '꽤', '후']
        temp = [each_word for each_word in noun if each_word not in stop_words] #불용어 제거
        if temp:  # temp에 결과가 존재할 경우에만 (길이 0인거는 제외)
            list1.append(temp)
    f.close()
    sentence = sentence + list1
    cate = [index for k in range(len(list1))]
    category = category + cate

#파일 읽기
read_file("./text/merged_food_restaurant(4246).txt", 0)
read_file("C/Users/HYERIN/Downloads/merged_travel_place(5828).txt", 1)
read_file("C/Users/HYERIN/Downloads/merged_travel_transport(7017).txt", 2)
read_file("C/Users/HYERIN/Downloads/merged_travel_exchange(1324).txt", 3)

print(len(sentence),",",len(category))