# 📚 https://www.acmicpc.net/problem/6603
"""
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 
49가지 수 중 k(k>6)개의 수를 골라 
집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 
이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. 
([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때,
수를 고르는 모든 방법을 구하는 프로그램

input #1
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""
import itertools

while True:
    k, *s = map(int, input().split())
    s.sort()
    if k == 0:
        break
    for result in itertools.combinations(s, 6):
        print(" ".join(map(str, result)))
    print()
