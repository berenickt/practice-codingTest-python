# 💡 알파벳 찾기 @https://www.acmicpc.net/problem/10809
s = input() # 입력으로 문자열을 받습니다.

# 알파벳 소문자의 존재 여부를 찾기 위해 루프를 돕니다.
for i in range(26):
  # 현재 알파벳 소문자를 chr 함수를 사용하여 구합니다.
  ch = chr(i+ord('a'))

  # 현재 알파벳 소문자가 문자열 내에서 처음으로 등장하는 위치를 찾고 출력
  # 존재하지 않으면 -1을 출력합니다. end=' ' 옵션은 출력 시 줄바꿈을 방지하고 공백을 추가
  print(s.find(ch), end= ' ')