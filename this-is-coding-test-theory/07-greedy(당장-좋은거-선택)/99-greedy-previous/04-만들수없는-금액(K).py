"""
동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 
최솟값을 구하는 프로그램을 작성하세요.

e.g.1, N = 5 이고, 
각 동전이 각각 3원, 2원, 1원, 1원, 9원짜리(화폐 단위) 동전이라고 가정합시다.
이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.

e.g.2, N = 3 이고, 
각 동전이 각각 3원, 5원, 7원짜리(화폐 단위) 동전이라고 가정합시다.
이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 1원입니다.

cf. 
첫째 줄에는 동전의 개수를 나타내는 양의 정수 N
둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 
        각 자연수는 공백으로 구분
        각 화폐 단위는 1,000,000 이하의 자연수

input #1
5
3 2 1 1 9

output #1 만들 수 없는 양의 정수 금액 중 최솟값
8

Tip
1. 화폐 단위를 기준으로 오름차순 정렬
2. 이후 1부터 차례대로 특정 금액(target)을 만들 수 있는지 확인
3. 만들 수 있는 target 금액이면, target값 증가시켜 업데이트
4. 만들 수 없는 값이 나오면, 그 값을 정답으로 출력
"""
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < coin:
        break
    target += coin

# 만들 수 없는 금액 출력
print(target)
