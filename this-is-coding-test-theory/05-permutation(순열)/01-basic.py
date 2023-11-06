"""
순열과 조합은 실제 코딩 테스트에서 필요한 경우가 많기 때문에, 
어떻게 사용할 수 있는지를 알고 있어야 한다.

사실 순열과 조합은 재귀 함수 혹은 반복문을 이용해서 직접 구현할 수 있지만,
실제 코딩테스트에서 이를 구현하는것은 매우 번거롭다.
다행히 파이썬3 버전 이상에서는 순열과 조합 기능을 제공하는 라이브러리를 
기본으로 제공하고 있기 때문에 걱정하지 말자

순열이나 조합을 호출해 나온 결과의 원소들은 리스트 형태가 아니기 때문에 
이를 손쉽게 다루기 위해서는 리스트로 바꿔줘야 한다.
마지막 결과에 list()를 붙여주자
"""

""" 순열(permutation)
- 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
- nPr으로 불림
- 순서가 의미있을 때 사용함
@see https://www.youtube.com/watch?v=1I6fAgEOPt4 --- 수학삼촌
"""
import itertools

data = [1, 2]

### 사용법 :  permutations(객체, r)
# 반복가능한 객체(리스트,튜플,문자열)안에서 r개를 선택
for i in itertools.permutations(data, 2):
    print(list(i), end=" ")

# 👉🏽 [1, 2] [2, 1]
