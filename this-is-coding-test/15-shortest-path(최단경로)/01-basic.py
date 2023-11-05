"""최단경로
말 그대로 가장 짧은 경로를 찾는 알고리즘이다.
그래서 길 찾기 문제로 자주 출제되기도 한다.
최단 경로 알고리즘 유형에는 다양한 종류가 있는데, 
상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.

예를 들어, 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우,
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우등의 다양한 사례가 존재한다.

코딩테스트에서는 최단 경로를 모두 출력하는 문제보다는 
단순히 최단 거리를 출력하도록 요구하는 문제가 많이 출제된다점을 알아두자.

보통 많이 사용하는 최단거리 알고리즘은 
다익스트라 최단 경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘 정도이나 
다익스트라 최단 경로 알고리즘, 플로이드 워셜정도만 배워보자.
"""

"""📍 dijkstra_path(linear_path_ver.)
다익스트라는 그래프에서 여러 개의 노드가 있을 때, 
특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
실제로 GPS 소프트웨어의 기본 알고리즘으로 채택되곤한다.

알고리즘의 원리는 다음과 같다.
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3, 4번을 반복한다.

다익스트라의 특징은 각 노드에 대한 현재까지의 최단거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다.

다익스트라를 구현하는 방법
1. 구현하기 쉽지만 느리게 동작하는 코드 (O(V^2))
2. 구현하기 조금 까다롭지만 빠르게 동작하는 코드 O(ElogV)

코딩테스트 시험을 준비할때는 2번을 정확히 이해하고 구현해야한다.

관련 강의는 하단을 참고하자.
개인적으로는 1번이 이해가 더 잘됐다.
1. 나동빈 강의 1 (2018) - https://www.youtube.com/watch?v=611B-9zk2o4
1. 나동빈 강의 2 (2020) - https://www.youtube.com/watch?v=acqm9mM1P6o&t=1259s

코드를 보면 알겠지만,
def get_smaller_node에서 사용된 for문과 def dijkstra(start)에서 
사용된 for문이 겹쳐 다익스트라 선형탐색의 시간복잡도는 (O(V^2))이다.

그래서, 전체 노드의 개수가 5,000개 이하라면 일반적인 코드로 해결 할 수 있으나, 
노드의 개수가 10,000개 이상이라면 문제를 풀기 어렵다.
그럴때는 다음시간에 배울 개선된 다익스트라 알고리즘을 이용하자.
"""
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""

import sys

n, m = int, input().split()
input = sys.stdin.readline
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = INF * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_small_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_small_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
# 👉🏽 0 2 3 1 2 4
