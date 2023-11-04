""" 인접행렬 vs 인접 리스트 
두 방식의 차이는 어떤점이 있을까?
메모리측면, 속도측면 에서 살펴보자.

메모리측면
- 인접 행렬(Adjacency Matrix) : 
    모든 관계를 저장하므로 노드 개수가 많을 수록 불필요한 메모리가 소요된다.
- 인접 리스트(Adjacency List)  : 
    연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.


속도측면
- 인접 행렬(Adjacency Matrix): 
    모든 경우의 수가 제시되어 있으므로 인접리스트보다 빠르다.
- 인접 리스트(Adjacency List): 
    인접행렬방식에 비해 정보를 얻는 속도가 느리다.
    인접리스트방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문이다.

DFS의 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
    방문처리(visited)란 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는것을 의미한다. 
    방문처리를 함으로써 각 노드를 한 번씩만 처리 할 수 있다.
"""

"""
깊이 우선 탐색 알고리즘인 DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단하다.
탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다.

실제로 스택을 쓰지 않고,
재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있다.
"""


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]  #

visited[v] = [False] * 9

dfs(graph, 1, visited)
# 👉🏽 1 2 7 6 8 3 4 5
