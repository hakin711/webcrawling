#메일 주소 없는 경우
from bs4 import BeautifulSoup
from urllib.request import urlopen, quote

def article(title, url) :
    src = urlopen(url)
    soup = BeautifulSoup(src,'lxml')

    res = soup.find_all('div',{'class':'article-text'})

    article_text = res[0].text
    t=article_text.find('@hani.co.kr')
    
    #print(article_text[0:t+11])
    f = open('article_text.txt','a')
    f.write('---------------------------------\n')
    f.write(url)
    f.write(title)
    
    if t < 0 :
        f.write(article_text)
    else :
        f.write(article_text[0:t+11])
        
    f.write('\n')
    f.close()


url_1 = 'http://search.hani.co.kr/Search?command=query&keyword='
url_2 = '&media=news&sort=s&period=month&datefrom=20160823&dateto=20161006&pageseq='

keyword=input('뉴스 검색어 ')
page_n=int(input('검색 기사수 '))

for i in range(page_n//10) :
    p_url=url_1+quote(keyword)+url_2+str(i)
    p_src = urlopen(p_url)
    p_soup = BeautifulSoup(p_src,'lxml')
    p_res=p_soup.find_all('ul',{'class':'search-result-list'})
    article_link=p_res[0].find_all('dt')
    
    for j in range(0,20,2) :
        a_title=article_link[j].a.text
        a_url=article_link[j].a['href']
        article(a_title,a_url)
