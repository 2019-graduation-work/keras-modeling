#중복제거 파일 만들기
content = []

f = open("C:/Users/HYERIN/PycharmProjects/untitled/text/crawl_blog_food_3_존맛(3300).txt","r", encoding='utf-8')
for i in range(1,10000):
    line = f.readline() #한 줄씩 읽음.
    content.append(line)
    if not line: break # 모두 읽으면 while문 종료.

f.close()

len("before : ", content)
content = list(set(content))
len("after : ",content)

file = open("C:/Users/HYERIN/PycharmProjects/untitled/text/food.txt","w", encoding='utf-8')
for i in range(1,len(content)):
    file.write(content[i])
file.close()