def count_fruits(name):
    count = 0
    for fruit in fruits:
       if (fruit == name):
          count +=1
    return count

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# for i in range(len(fruits)):
#     if (fruits[i] == "사과"):
#         count += 1

print(count_fruits("사과"))

def find_age(target):
    for person in people:
       if (person['name'] == target):
          return person['age']
    return "해당하는 이름이 없습니다."

people = [{'name': 'bob', 'age': 20}, 
              {'name': 'carry', 'age': 38},
              {'name': 'john', 'age': 7},
              {'name': 'smith', 'age': 17},
              {'name': 'ben', 'age': 27}]

print(find_age("bob"))


"""
MongoDB는 데이터를 저장하고 관리할 수 있는 멋진 저장소예요! 데이터를 정리하기 위해 아래와 같은 구조를 사용해요


Database (데이터베이스): 데이터를 담는 가장 큰 상자예요.여러 개의 Collection(컬렉션)을 포함하고 있어요!
Collection (컬렉션): 데이터를 묶어두는 작은 상자들이에요. 각 컬렉션 안에는 여러 개의 Document(도큐먼트)가 있어요.
Document (도큐먼트): MongoDB에서 실제 정보를 담고 있는 데이터 덩어리예요. 우리가 필요한 내용은 모두 도큐먼트에 들어 있어요!

데이터베이스는 여러개의 컬렉션을 가지고 있고, 컬렉션은 여러개의 도큐먼트를 가지고 있어요!
우리가 실제로 사용하는 정보는 도큐먼트에요

Database (데이터베이스): 도서관 전체 (예: 과학 도서관, 미술 도서관)
Collection (컬렉션): 도서관의 섹션 (예: 과학 도서관 안의 물리학 섹션, 화학 섹션)
Document (도큐먼트): 섹션 안의 책 (실제로 읽을 수 있는 정보)

"""
