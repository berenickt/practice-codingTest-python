# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42891
"""
평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어졌고 고민 끝에 카카오 TV 라이브 방송을 하기로 마음먹었습니다.
그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 다음과 같이 독특한 방식을 생각해냈습니다.
1. 회전판에 먹어야 할 N개의 음식이 있습니다.
2. 각 음식에는 1부터 N까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요됩니다.

무지는 다음과 같은 방법으로 음식을 섭취합니다.
- 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
- 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
- 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
    - 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말합니다.
- 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정합니다.

무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었습니다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 합니다.

각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times,
네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때,
몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하세요.

cf. 만약 더 섭취해야 할 음식이 없다면 -1을 반환

input #1
food_times : [3, 1, 2]
k          : 5

output #1
1

입출력 예 설명 #1
0~1초 동안에 1번 음식을 섭취한다. 남은 시간은 [2,1,2] 이다.
1~2초 동안 2번 음식을 섭취한다. 남은 시간은 [2,0,2] 이다.
2~3초 동안 3번 음식을 섭취한다. 남은 시간은 [2,0,1] 이다.
3~4초 동안 1번 음식을 섭취한다. 남은 시간은 [1,0,1] 이다.
4~5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은 [1,0,0] 이다.
5초에서 네트워크 장애가 발생했다. 1번 음식을 섭취해야 할 때 중단되었으므로, 
장애 복구 후에 1번 음식부터 다시 먹기 시작하면 된다

Tip
시간이 적게 걸리는 음식부터 확인해서 제거하는 Greedy로 해결 가능
1. 모든 음식을 우선순위 큐(최소 힙)에 삽입
2. 시간이 가장 적게 걸리는 음식부터 순서대로 탐색
3. [이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]과 K의 시간을 비교하며 제거를 진행
"""

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 먹는 시간이 작은 음식부터 제거해야하므로 우선순위 큐를 사용
    q = []

    # (음식 시간, 음식 번호)의 튜플 형태로 우선순위 큐에 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
        # 👉 q ===> [(1, 2), (3, 1), (2, 3 )

    cur_sum = 0  # 먹기 위해 사용한 시간
    prev = 0  # 직전에 다 먹은 음식 시간
    remain_fo = len(food_times)  # 남은 음식의 개수

    # [이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]이 K보다 커지면, 반복문 종료
    # 현재 음식을 섭취하기 위한 시간은, `남은 음식 개수 * (현재 음식 섭취 시간 - 이전 음식 섭취 시간)`
    while cur_sum + (remain_fo * (q[0][0] - prev)) <= k:
        # 현재 음식을 우선순위 큐에서 제거하며, 현재 음식의 섭취 시간을 저장
        now_food = heapq.heappop(q)[0]  # testcase#1 ==> 1, 2

        # 현재 음식을 모두 섭취하기 위해 걸리는 시간을, 음식 섭취에 소요한 전체 시간에 추가
        cur_sum += (now_food - prev) * remain_fo
        remain_fo -= 1  # 다 먹은 음식 제외
        prev = now_food  # 이전 음식 섭취 시간을 현재 음식 섭취 시간으로 변경

    # 우선순위큐의 남아있는 요소들을 음식 번호를 기준으로 오름차순 정렬
    result = sorted(q, key=lambda x: x[1])
    # 👉 result ===> [(3, 1)]

    # (K 발생까지 남은 시간 % 남은 음식 개수), 배열의 idx는 0부터 시작하므로 나머지 값을 idx로 사용
    return result[(k - cur_sum) % remain_fo][1]


print(solution([3, 1, 2], 5))
