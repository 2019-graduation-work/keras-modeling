import re
import json
import math
import datetime
import requests
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

#용택 여기따가 적으셈 니 api 키 값
naver_client_id = "rQkSsuIQnoQqDjsRZyfI"
naver_client_secret = "0wTocd4xsY"


def naver_blog_crawling(search_blog_keyword, display_count, sort_type):
    search_result_blog_page_count = get_blog_search_result_pagination_count(search_blog_keyword, display_count)
    get_blog_post(search_blog_keyword, display_count, search_result_blog_page_count, sort_type)


def get_blog_search_result_pagination_count(search_blog_keyword, display_count):
    encode_search_keyword = urllib.parse.quote(search_blog_keyword)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = "https://openapi.naver.com/v1/search/blog?query="+encode_search_keyword
    request = urllib.request.Request(url,headers=header)

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
            if blog_pagination_total_count >= 10000:
                # 밑에 카운트 개수가 포스트 1000개 넘을때 따올 포스팅 수임
                blog_pagination_count = 200*5 #?파씽할 블로그 수/10 (5000개할거니까 500)
            else:
                blog_pagination_count = blog_pagination_total_count

            print("키워드 " + search_blog_keyword + " 에 해당하는 포스팅 수 : " + str(response_body_dict['total']))
            print("키워드 " + search_blog_keyword + " 에 해당하는 블로그 페이지 수 : " + str(blog_pagination_total_count))
            print("키워드 " + search_blog_keyword + " 에 해당하는 블로그 처리할 수 있는 페이지 수 : " + str(blog_pagination_count))

        return blog_pagination_count

def get_blog_post(search_blog_keyword, display_count, search_result_blog_page_count, sort_type):
    iter1 = 0
    #?여기에 텍스트파일 경로 넣어주어야 함
    file = open("C:/Users/HYERIN/PycharmProjects/untitled/crawl_blog_trafic_2.txt","w", encoding='utf-8')
    encode_search_blog_keyword = urllib.parse.quote(search_blog_keyword)

    for i in range(1, search_result_blog_page_count + 1):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url = "https://openapi.naver.com/v1/search/blog?query=" + encode_search_blog_keyword + "&display=" + str(
            display_count) + "&start=" + str(i) + "&sort=" + sort_type
        #url = "https://openapi.naver.com/v1/search/blog?query="%urllib.parse.quote(encode_search_blog_keyword)%urllib.parse.quote("&display=")\
        #      %urllib.parse.quote(str(display_count))%urllib.parse.quote("&start=")%urllib.parse.quote(str(i))%urllib.parse.quote("&sort=")%urllib.parse.quote(sort_type)

        request = urllib.request.Request(url,headers = header)

        request.add_header("X-Naver-Client-Id", naver_client_id)
        request.add_header("X-Naver-Client-Secret", naver_client_secret)

        '''try:
            response = urllib.request.urlopen(request) #ERROR 1번
            response_code = response.getcode()
        except BaseException:
            response_code = 0;'''
        try:
            response = urllib.request.urlopen(request)  # ERROR 1번
            response_code = response.getcode()
        except HTTPError as e:
            print(e)
            response_code = 0;
        except URLError as e:
            print(url)
            response_code = 0;

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

                except:
                    j += 1

    file.close()

if __name__ == '__main__':
    naver_blog_crawling("기초 화장품 후기", 1, "sim") #?첫번째인자 검색하고싶은 검색 값