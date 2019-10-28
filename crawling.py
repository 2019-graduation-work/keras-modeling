import re
import json
import math
import datetime
import requests
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

#용택 여기따가 적으셈 니 api 키 값
naver_client_id = "rQkSsuIQnoQqDjsRZyfI"
naver_client_secret = "0wTocd4xsY"

path = "C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/"
# print(keyword)

keyword = ""

def naver_blog_crawling(search_blog_keyword, display_count, sort_type):
    search_result_blog_page_count = get_blog_search_result_pagination_count(search_blog_keyword, display_count)
    get_blog_post(search_blog_keyword, display_count, search_result_blog_page_count, sort_type)


def get_blog_search_result_pagination_count(search_blog_keyword, display_count):
    encode_search_keyword = urllib.parse.quote(search_blog_keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encode_search_keyword
    request = urllib.request.Request(url)

    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)

    response = urllib.request.urlopen(request)
    response_code = response.getcode()

    if response_code is 200:
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8'))

        if response_body_dict['total'] == 0:
            blog_pagination_count = 0
        else:
            blog_pagination_total_count = math.ceil(response_body_dict['total'] / int(display_count))
            # 블로그 글 1000개 넘으면 1000개만 수집하게 됨
            if blog_pagination_total_count >= 1000:
                # 밑에 카운트 개수가 포스트 1000개 넘을때 따올 포스팅 수임
                blog_pagination_count = 100 #?파씽할 블로그 수/10 (5000개할거니까 500)
            else:
                blog_pagination_count = blog_pagination_total_count

            print("키워드 " + search_blog_keyword + " 에 해당하는 포스팅 수 : " + str(response_body_dict['total']))
            print("키워드 " + search_blog_keyword + " 에 해당하는 블로그 페이지 수 : " + str(blog_pagination_total_count))
            print("키워드 " + search_blog_keyword + " 에 해당하는 블로그 처리할 수 있는 페이지 수 : " + str(blog_pagination_count))

        return blog_pagination_count

def get_blog_post(search_blog_keyword, display_count, search_result_blog_page_count, sort_type):
    iter1 = 0
    #?여기에 텍스트파일 경로 넣어주어야 함
    # file = open("C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/crawl_상하이 지하철.txt", "w", encoding='utf-8')
    file = open(path + b_name + ".txt", "w", encoding='utf-8')
    encode_search_blog_keyword = urllib.parse.quote(search_blog_keyword)

    for i in range(1, search_result_blog_page_count + 1):
        url = "https://openapi.naver.com/v1/search/blog?query=" + encode_search_blog_keyword + "&display=" + str(
            display_count) + "&start=" + str(i) + "&sort=" + sort_type

        request = urllib.request.Request(url)

        request.add_header("X-Naver-Client-Id", naver_client_id)
        request.add_header("X-Naver-Client-Secret", naver_client_secret)

        '''try:
            response = urllib.request.urlopen(request) #ERROR 1번
            response_code = response.getcode()
        except BaseException:
            response_code = 0;'''

        response = urllib.request.urlopen(request)  # ERROR 1번
        response_code = response.getcode()

        if response_code is 200:
            response_body = response.read()
            response_body_dict = json.loads(response_body.decode('utf-8'))


            for j in range(0, len(response_body_dict['items'])):
                try:
                    blog_post_url = response_body_dict['items'][j]['link'].replace("amp;", "")

                    get_blog_post_content_code = requests.get(blog_post_url)
                    get_blog_post_content_text = get_blog_post_content_code.text

                    get_blog_post_content_soup = BeautifulSoup(get_blog_post_content_text, 'lxml')

                    for link in get_blog_post_content_soup.select('iframe#mainFrame'):
                        real_blog_post_url = "http://blog.naver.com" + link.get('src')

                        get_real_blog_post_content_code = requests.get(real_blog_post_url)
                        get_real_blog_post_content_text = get_real_blog_post_content_code.text

                        get_real_blog_post_content_soup = BeautifulSoup(get_real_blog_post_content_text, 'lxml')
                        #print(get_real_blog_post_content_soup.find_all("div", 'class': "se-module se-module-text")

                        #블로그 본문내용
                        blog_post_full_contents = ''
                        for each_div in get_real_blog_post_content_soup.find_all('div', {'class': 'se-module se-module-text'}):
                            #print(each_div)
                            for each_p in each_div.find_all('p'):
                                blog_post_full_contents += each_p.get_text()

                        if len(blog_post_full_contents) == 0:
                            continue

                        remove_html_tag = re.compile('<.*?>')

                        blog_post_title = re.sub(remove_html_tag, '', response_body_dict['items'][j]['title'])
                        blog_post_description = re.sub(remove_html_tag, '',
                                                       response_body_dict['items'][j]['description'])
                        blog_post_postdate = datetime.datetime.strptime(response_body_dict['items'][j]['postdate'],
                                                                        "%Y%m%d").strftime("%y.%m.%d")
                        blog_post_blogger_name = response_body_dict['items'][j]['bloggername']

                        blog_post_full_contents = blog_post_full_contents.replace('\n', '')
                        blog_post_title = blog_post_title.replace('\n', '')

                        iter1 = iter1 + 1
                        #file.write("포스팅 URL : " + blog_post_url + '\n')
                        #file.write("포스팅 제목 : " + blog_post_title + '\n')
                        #file.write("포스팅 설명 : " + blog_post_description + '\n')
                        #file.write("포스팅 날짜 : " + blog_post_postdate + '\n')
                        #file.write("블로거 이름 : " + blog_post_blogger_name + '\n')
                        #file.write("포스팅 내용 : " + blog_post_full_contents + '\n\n\n\n')
                        file.write(blog_post_title + ' : '+blog_post_full_contents+ '\n')
                        print(iter1)
                        print("포스팅 제목 : " + blog_post_title + '\n')
                        print("포스팅 내용 : " + blog_post_full_contents + '\n')
                        print("******************************************")


                except:
                    j += 1

    file.close()

def removeDuplicate(b_name):
    content = []

    path = "C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/"

    f = open(path + b_name + ".txt", "r", encoding='utf-8')

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
    for i in range(1, len(content)):
        file.write(content[i])
    file.close()


if __name__ == '__main__':
    # print(keyword)
# 교통
#     "미국", "LA", "뉴욕", "워싱턴", "일본", "후쿠오카",
#     "대만", "타이페이", "독일", "프랑크푸르트", "베를린"
#     "쾰른", "뮌헨", "영국", "런던", "에든버러", "이탈리아", "로마"
#     "피렌체", "베니스", "플로렌스", "밀라노", "홍콩"
#                  "중국", "베이징", "상하이",
#                  "스페인", "바르셀로나", "마드리드", "마카오", "베트남",
#     "호치민", "다낭",
#                  "하노이", "스위스", "취리히", "제네바", "체코", "프라하", "부다페스트",
#                  "동유럽", "유럽", "오스트리아", "비엔나", "헝가리"

#   관광지
    #"미국", "LA", "뉴욕", "워싱턴", "일본", "후쿠오카",
         #      "대만", "타이페이","쾰른", "뮌헨", "영국", "런던", "에든버러",
    #"이탈리아", "로마"
            #    "피렌체", "베니스", "플로렌스", "밀라노", "홍콩"
            # "중국", "베이징", "상하이",
             #  "스페인",
#     "바르셀로나", "마드리드", "마카오", "베트남", "호치민", "다낭",
# "하노이", "스위스", "취리히", "제네바", "체코", "프라하", "부다페스트",
# "동유럽", "유럽", "오스트리아", "비엔나", "헝가리"
    locals = ["미국", "LA", "뉴욕", "워싱턴", "일본", "후쿠오카",
              "대만", "타이페이", "독일", "프랑크푸르트", "베를린",
              "쾰른", "뮌헨", "영국", "런던", "에든버러", "이탈리아",
              "로마", "피렌체", "베니스", "플로렌스", "밀라노", "홍콩",
              "중국", "베이징", "상하이", "스페인", "바르셀로나", "마드리드",
              "마카오", "베트남", "호치민", "다낭", "하노이", "스위스", "취리히",
              "제네바", "체코", "프라하", "부다페스트", "동유럽", "유럽", "오스트리아",
              "비엔나", "헝가리"]

    nation = ["미국", "일본", "대만", "태국", "독일"
              "유로", "달러", "스위스", "베트남", "태국",
              "필리핀"]

    # 맛집 서대문구부터
    # "도봉구", "은평구", "동대문구", "동작구", "금천구", "구로구", "종로구",
    # "강북구", "중랑구", "강남구", "강서구", "중구", "강동구", "광진구",
    # "마포구", "관악구", "성북구", "노원구", "송파구",
    seoul = [ "서대문구", "양천구",
             "영등포구", "용산구", "서초구", "성동구"]

    transport = ["기차", "지하철", "버스", "대중교통", "교통편"]
    place = ["관광지", "가볼만한 곳", "여행 코스"]
    exchange = ["환전", "환전 팁", "환전 정보"]
    food = ["음식점", "맛집", "존맛"]

    b_name = "crawl_"
    # keyword = b_name[6:]

    for loc in seoul:
        for trans in food:
            b_name += (loc + " " + trans)
            keyword = b_name[6:]
            naver_blog_crawling(keyword, 10, "sim") #?첫번째인자 검색하고싶은 검색 값
            removeDuplicate(b_name)
            b_name = "crawl_"

