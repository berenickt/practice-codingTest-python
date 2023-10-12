# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181880
"""
정수가 있을 때, 짝수라면 반으로 나누고, 
홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 

e.g. 10이 있다면 다음과 같은 과정으로 1이 됩니다.
10 / 2 = 5
(5 - 1) / 2 = 4
4 / 2 = 2
2 / 2 = 1
위와 같이 4번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 num_list가 주어질 때,
num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return

입력#1
[12, 4, 15, 1, 14]

출력#1
11
"""


def solution(num_list):
    answer = []
    # 1이 될 때까지 반복연산
    for n in num_list:
        repeat = 0
        num = n
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                repeat += 1
            else:
                num = (num - 1) // 2
                repeat += 1
        answer.append(repeat)
    return sum(answer)


print(solution([12, 4, 15, 1, 14]))
