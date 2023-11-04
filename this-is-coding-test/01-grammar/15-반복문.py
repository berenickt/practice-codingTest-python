"""while문
while문 은 조건문이 참일 때 한해서, 반복적으로 코드가 수행
"""
i = 1
result = 0

while i <= 9:
    result = result + i
    i = i + 1

# 👉🏽 45

"""for문
리스트를 사용하는 대표적인 for문의 구조는 다음과 같은데, 
in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용 될 수 있다.

for문에서 수를 차례대로 나열 할 때는 
range(이상, 미만)를 주로 사용
"""
"""💡 range() 함수
range(미만)            : range(10) = 0~9
range(이상, 미만)       : range(1, 11) = 1~10
range(이상, 미만, 간격)  : range(1, 20, 2) = 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
                      : range(20, 0, -2) = 20, 18, 16, 14, 12, 10, 8, 6, 4, 2
"""
result = 0

for i in range(1, 10):  # 1 ~ 9까지 더하기
    result = result + i

# 👉🏽 45

"""2중 반복문
조금 더 응용해서 2중 반복문을 사용 할 수 있는데,

중첩된 반목문은 플로이드 워셜 알고리즘, 
다이나믹 프로그래밍 등의 알고리즘 문제에서 매우 많이 사용
"""
# 구구단 알고리즘
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")

# 👉🏽 2단 ~ 9단까지의 곱셈
