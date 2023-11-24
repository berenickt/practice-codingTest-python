"""
하나의 수열에는 다양한 수가 존재한다.
이러한 수는 크기에 상관없이 나열되어 있다.
이 수를 큰 수부터 작은 수의 순서로 정렬해야한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

cf.
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
둘째 줄부터 N + 1 번째 줄 까지 N개의 수가 입력된다. 
수의 범위는 1 이상 100,000 이하 자연수이다.

input #1
3
15
27
12

output #1
27 25 12
"""
# N 입력 받기
n = int(input())

# N개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 정렬 라이브러리를 이용하여 내림차순 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=" ")

"""Tip
가장 기본적인 정렬을 할 수 있는지 물어보는 문제
수의 개수 500개 이하로 매우적으며,
모든 수는 1이상 100,000 이하이므로 어떤 정렬 알고리즘을 사용해도 문제 해결 가능하다
"""
