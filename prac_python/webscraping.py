import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)  # HTML을 받아온 것을 확인할 수 있다.

# select를 이용해서, li들을 불러오기
# class 명 앞에는 '.'을 붙여줍니다.
# class 명 내의 띄어쓰기(공백)은 '.'으로 바꾸어 써주세요.

movies = soup.select('.ipc-page-grid__item--span-2 > .ipc-metadata-list--base > li')
print(len(movies))
for movie in movies:
    # print(movie)

    # movie 안에 h3 가 있으면,
    # (조건을 만족하는 첫 번째 요소, 없으면 None을 반환한다.)
    title = movie.select_one('.ipc-title-link-wrapper > h3')  # 가장 위에 나오는 요소 반환
    released_year = movie.select_one('.cli-title-metadata-item:nth-child(1)')
    running_time = movie.select_one('.cli-title-metadata-item:nth-child(2)')
    pg_level = movie.select_one('.cli-title-metadata-item:nth-child(3)')
    # print(tag_element)
    if not title:
        continue
    # h3의 text를 찍어본다.
    print(title.text)
    print(released_year.text)
    print(running_time.text)
    print(pg_level.text)

""" ### 개발자 도구 Elements 탭에서 요소를 우클릭한 후 Copy > Copy selector를 해서 선택자를 얻을 수 있음
# 선택자를 사용하는 방법 (copy selector)
    soup.select('태그명')
    soup.select('.클래스명')
    soup.select('#아이디명')
    
# class 명 내의 띄어쓰기(공백)은 '.'으로 바꾸어 쓰거나, 조건이 겹치지 않는다면 띄어쓰기를 기준으로 class들을 분리하고 마지막 class만 써주세요.
    # 위의 단순한 3가지 형태만 쓸 경우 여러 요소가 선택될 수도 있습니다.
    # 예: soup.select('a')는 문서 내의 모든 <a></a> 요소를 찾습니다.
    # 이를 좀 더 구체화해서 아래처럼 어떤 경로를 거쳐 요소를 찾아야 되는지 명시할 수 있습니다. 
    soup.select('상위태그명 > 하위태그명 > 하위태그명')
    soup.select('상위태그명.클래스명 > 하위태그명.클래스명')
    
# 앞의 예에서처럼 여러 <li>를 가질 때 몇 번째 <li> 인지를
# 부모의 몇 번째 자식인지 명시해서 지정할 수도 있습니다. 
    soup.select('.클래스명:nth-child(자식의순서)')
    
# 태그와 속성값으로 찾는 방법
    soup.select('태그명[속성="값"]')
    
# 한 개만 가져오고 싶은 경우
    soup.select_one('위와 동일')
"""