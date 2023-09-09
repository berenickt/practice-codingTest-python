# 💡 N과 M (4) 📚 https://www.acmicpc.net/problem/15652
import sys
n, m = map(int, input().split())
cnt = [0]*(n+1)


def go(index, selected, n, m):
    if selected == m:
        for i in range(1, n+1):
            for j in range(cnt[i]):
                sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
        return
    if index > n:
        return
    for i in range(m-selected, 0, -1):
        cnt[index] = i
        go(index+1, selected+i, n, m)

    cnt[index] = 0
    go(index+1, selected, n, m)


go(1, 0, n, m)
