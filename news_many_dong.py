#http://yoonpunk.tistory.com/6
# 각페이지 기사 링크(15개/페이지당)에서 기사본문 가져오기

def article(l) :
    src = urlopen(l)
    soup = BeautifulSoup(src,'lxml')
    res = soup.find_all('div',{'class':'article_txt'})
    article_text=res[0].text
    #print(res[0].text)
    t=article_text.find('function')
    #print(article_text[0:t])
    f = open('article_dong.txt','a+')
    f.write('================================================\n')
    f.write(soup.title.text)
    f.write(article_text[0:t])
    f.write('\n')
    f.close()

def page(u) :
    src = urlopen(u)
    soup = BeautifulSoup(src,'lxml')
    res = soup.find_all('p',{'class':'tit'})
    f = open('article_link.txt','w')
    
    for i in range(15) :
        #print(res[i].a.text,res[i].a['href'])
        f.write(res[i].a['href'])
        f.write('\n')
        article(res[i].a['href'])
    f.close()
    

import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen, quote
# 'quote'는 'urlopen'에서 인자로 사용되는 URL주소(이하 타겟 주소)에 한글(UTF_8)이 포함되었을 때,
# 이를 아스키(ASCII)형식으로 바꿔주기 위한 함수

url_1 = 'http://news.donga.com/search?p='
url_key = '&query='
url_2 = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'

url=url_1+'1'+url_key+quote('사드')+url_2  
#URL주소에는 'ASCII' 표현 방식 이외의 문자표기법은 사용될 수 없기 때문에 '
#한글,'UTF-8' 방식의 문자를 'ASCII' 방식으로 변환해야하기 위해 'quute'메소드를 사용


f = open('page_link.txt','w')

for i in range(1,11) : #10개 페이지
    i=1+15*(i-1)
    url = url_1 + str(i) +url_key+quote('사드')+url_2
    
    f.write(url)
    f.write('\n')
    #print(url)  #페이지
    page(url)

f.close()
