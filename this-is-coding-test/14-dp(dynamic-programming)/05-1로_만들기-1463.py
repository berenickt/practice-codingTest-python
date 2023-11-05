# 📚 https://www.acmicpc.net/problem/1463
"""
피보나치 수열 문제를 도식화했던 것처럼 문제를 풀기 전에 
함수가 호출되는 과정을 직접 그림으로 그려보면 이해하는데 도움이 된다.

점화식은 다음과 같다.
> a(i) = min(a(i-1), a(i-2), a(i-5)) + 1
> 점화식 끝에 1을 더해주는 이유는 함수의 호출 횟수를 구해야하기 때문이다.

실제 코드로 구현 할 때는 1을 빼는 연산을 제외하고는 
해당 수로 나누어떨어질 때 한해서만 점화식을 적용 할 수 있다.
두 수 중 단순히 더 작은수를 구할 때는 min() 함수를 이용하자.

이 문제를 풀때 사실 답안 예시를 보고도 이해가 되지않았다. 
그래서 다른 사람들은 어떻게 풀었는지 검색해봤는데,
빈 리스트(values)를 선언하고 거기에 추가하는 방식이다.
"""
# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
