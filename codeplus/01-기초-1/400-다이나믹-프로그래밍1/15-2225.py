# 💡 합분해 📚 https://www.acmicpc.net/problem/2225
mod = 1000000000
n, k = map(int, input().split())
d = [[0]*(n+1) for _ in range(k+1)]
d[0][0] = 1

for i in range(1, k+1):
    for j in range(0, n+1):
        for l in range(0, j+1):
            d[i][j] += d[i-1][j-l]
        d[i][j] %= mod

print(d[k][n])
