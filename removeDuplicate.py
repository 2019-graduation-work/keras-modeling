#중복제거 파일 만들기
content = []

path = "C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/"
b_name = "merged_food_restaurant"

f = open(path + b_name + ".txt", "r", encoding='utf-8')
# for i in range(1, 10000):
#     line = f.readline() #한 줄씩 읽음.
#     content.append(line)
#     if not line: break # 모두 읽으면 while문 종료.


for line in f:
    content.append(line)

b_len = len(content)
print("before: " + str(b_len))

content = list(set(content))

f.close()

a_len = len(content)
print("after: " + str(a_len))

a_name = b_name + "(" + str(a_len) + ")"

file = open(path + a_name + ".txt", "w", encoding='utf-8')
for i in range(1,len(content)):
    file.write(content[i])
file.close()
