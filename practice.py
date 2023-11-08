### 각각 x축, y축 방향으로 8개 방향
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
dirX = [0, 1, 1, 1, 0, -1, -1, -1]

"""a[1][2]의 70를 기준으로 시계방향으로 회전해서 출력
"""

a = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]

for i in range(8):
    ny = 1 + dirY[i]  # ny ===> 0 0 1 2 2 2 1 0
    nx = 2 + dirX[i]  # nx ===> 2 3 3 3 2 1 1 1
    print(nx)
    if 0 <= ny < 4 and 0 <= nx < 4:
        print(a[ny][nx])

"""output
30
40
80
120
110
100
60
20
"""
