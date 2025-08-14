import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# 아래 uri를 복사해둔 uri로 수정하기
uri = "mongodb+srv://parkmisonme777:I2k7z6cLWTUw8AQ8@myjunglecluster.kxpq58a.mongodb.net/?retryWrites=true&w=majority&appName=MyJungleCluster&tlsAllowInvalidCertificates=true"
client = MongoClient(uri, 27017)  # MongoDB는 27017 포트로 돌아갑니다.
db = client.jungle 
    
# 코딩 시작
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')
    
# # select를 이용해서, li들을 불러오기
# movies = soup.select('.ipc-page-grid__item--span-2 > .ipc-metadata-list--base > li')
# for movie in movies:
#     tag_element = movie.select_one('.ipc-title-link-wrapper > h3')
#     if not tag_element:
#         continue

#     title = tag_element.text.split(". ", 1)[1]
#     if (title == "포레스트 검프"):
#         released_year = movie.select_one('.cli-title-metadata-item:nth-child(1)').text
#         released_year = int(released_year)
#         print(released_year)

target_movie = db.movies.find_one({'title':'포레스트 검프'})
target_year = target_movie['released_year']

# for movie in len(db.movies):
#     same = db.movies.find_one({'released_year':target_year})
#     print(same['title'])
    
movies = list(db.movies.find({'released_year':target_year}))
for movie in movies:
    print(movie['title'])

target_movie = db.movies.update_one({'title':'매트릭스'}, {'$set' : {'released_year':1998}})
print(db.movies.find_one({'title':'매트릭스'},{'_id':False}))