# 💡 2×n 타일링 2 📚 https://www.acmicpc.net/problem/9095
d = [0]*11
d[0] = 1

for i in range(1, 11):
    if i-1 >= 0:
        d[i] += d[i-1]
    if i-2 >= 0:
        d[i] += d[i-2]
    if i-3 >= 0:
        d[i] += d[i-3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(d[n])
