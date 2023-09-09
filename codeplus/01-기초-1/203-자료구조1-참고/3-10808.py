# 💡 알파벳 개수 📚 https://www.acmicpc.net/problem/10808
'''
알파벳 소문자로 이루어진 단어에서 각 알파벳이 몇 개인지 구하는 문제
'''
s = input()  # 입력으로 문자열을 받습니다.

# 알파벳 소문자의 개수를 세기 위해 루프를 돕니다.
for i in range(26):
    # 현재 알파벳 소문자를 chr 함수를 사용하여 구합니다.
    ch = chr(i+ord('a'))

    # 현재 알파벳 소문자의 개수를 문자열 내에서 세고 출력
    # end=' ' 옵션은 출력 시 줄바꿈을 방지하고 공백을 추가
    print(s.count(ch), end=' ')
