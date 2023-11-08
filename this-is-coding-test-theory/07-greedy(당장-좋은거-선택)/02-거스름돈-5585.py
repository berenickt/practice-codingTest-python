# 📚 https://www.acmicpc.net/problem/5585
"""
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 
언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 

타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램

input #1
380

output #1
4

Tip
최적의 해를 구하기 위해서는 가장 큰 화폐단위부터 돈을 거슬러주면 된다.

- //는 나눈 몫을 반환
- % 는 나눈 나머지를 반환
- / 는 나눈 나머지를 부동소수점 수를 반환
"""
T = int(input())
n = 1000 - T  # 타로가 지불할 돈(1 이상 1000미만의 정수)
# testcase #1 n ===> 620

# 큰 단위의 화폐부터 차례대로 확인하기
data = [500, 100, 50, 10, 5, 1]
coin_cnt = 0

# 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
for coin in data:
    coin_cnt = coin_cnt + n // coin
    n = n % coin

print(coin_cnt)
