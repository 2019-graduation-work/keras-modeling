from selenium import webdriver

driver = webdriver.Chrome('C:/Users/HYERIN/Downloads/chromedriver_win32/chromedriver')

#driver = webdriver.PhantomJS('C:/Users/HYERIN/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
keyword = '여행' #검색하고 싶은 것
print(url+keyword)
driver.get(url)

#블로그 클릭
driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[4]/a').click()

#하나하나 들어가기
driver.find_element_by_css_selector('#sp_blog_1 > dl > dt > a').click()



