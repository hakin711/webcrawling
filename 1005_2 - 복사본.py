from konlpy.tag import Kkma, Twitter
from konlpy.utils import pprint
from collections import defaultdict, Counter

f = open('article_dong.txt')
data = f.read()
#print(data)

kkma = Kkma() #자연처 처리 라이브러리 Kkma
#pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에'))
#print('%s',data)
#pprint(kkma.nouns(data))
#print(kkma.nouns(data))

data_n = kkma.nouns(data) #list
#print(type(data_n))
#print(data_n[0])

'''
#dic_n = {} #명사의 사용 빈도를 기록할 dictionary

dic_n = defaultdict(int)

for i in data_n :
    #print(i)
    dic_n[i] += 1
pprint(dic_n)
'''

'''
#c = Counter(data) #명사만 분리 안됨
c = Counter(data_n)
print(c.most_common(50))
'''
t = Twitter() #'Twitter'객체를 생성
nn = t.nouns(data)
#'Twitter'객체의 'nouns'메소드를 이용해 'data'에서 명사만 분리/추출
#print(nn)
#print(type(nn)) #list


c = Counter(nn) 
print(c.most_common(10))
#'Counter'객체의 'most_common'메소드는 정수를 입력받아 객체 안의 명사 중,
#빈도수가 큰 명사부터 순서대로 입력받은 정수갯수만큼 저장되어 있는 객체를 반환
#print(type(c.most_common(10))) #list
#[('사드', 19), ('박', 15), ... ]


    
      
f.close()
