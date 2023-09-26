# 💡 -2진수 📚 https://www.acmicpc.net/problem/2089
# 재귀 함수 go를 정의
def go(n):
    # 재귀 종료 조건: n이 0인 경우 함수를 종료
    if n == 0:
        return

    # n이 짝수인 경우
    if n % 2 == 0:
        # n을 음수로 나눈 후 다시 재귀 호출
        go(-(n // 2))
        # 0을 출력, end=""는 줄바꿈을 하지 않고 출력
        print(0, end="")

    # n이 홀수인 경우
    else:
        # n이 양수인 경우, n을 음수로 나눈 후 다시 재귀 호출
        if n > 0:
            go(-(n // 2))
        # n이 음수인 경우, (-n + 1)을 2로 나눈 후 다시 재귀 호출
        else:
            go((-n + 1) // 2)
        # 1을 출력, end=""는 줄바꿈을 하지 않고 출력
        print(1, end="")


# 정수 n을 입력받음
n = int(input())

# n이 0인 경우, 결과로 0을 출력
if n == 0:
    print(0)
# 그 외의 경우, go 함수를 호출하여 이진수를 생성하고 출력
else:
    go(n)
