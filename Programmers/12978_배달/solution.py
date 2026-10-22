# 프로그래머스 12978 배달 (Lv2)
#
# 문제: 1번 마을에서 K 시간 이하로 배달 가능한 마을 수
# 제한: N <= 50, 도로 <= 2,000, 도로 시간 <= 10,000
#
# 판단: 도로마다 시간이 다름 -> BFS로는 최단 보장 X
#       한 출발점에서 모든 마을까지의 최단 시간 -> 다익스트라 (힙 사용)
#       같은 마을 쌍의 도로가 여러 개여도 인접 리스트에 다 넣으면 자동 처리
#
# 시간 복잡도: O(E log E), E = 도로 수

import heapq

def solution(N, road, K):
    # 마을 번호가 1부터 시작하므로, 그래프 리스트를 N+1 크기로 초기화
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        # 양방향 그래프이므로, 양쪽 모두 추가
        graph[a].append((b, c))
        graph[b].append((a, c))


    # dist[i]: 1번 마을에서 i번 마을까지 최단거리 (모르면 무한대)
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    # (시간, 마을) 순서로 넣어야 시간이 짧은 것부터 꺼내짐.
    heap = [(0, 1)]

    while heap:
        # 지금까지 알려진 시간이 가장 짧은 마을을 꺼냄
        current_dist, current_node = heapq.heappop(heap)

        # 이미 더 짧은 시간으로 처리된 마을이라면 낡은 정보이므로 무시
        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            # 현재 마을을 거쳐 이웃으로 가는 시간
            distance = current_dist + weight
            # 기존에 알던 시간보다 짧으면 갱신하고 힙에 추가
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    # 최단 시간이 K 이하인 마을 수 (0번 칸과 갈 수 없는 마을은 무한대라 생략됨)
    return len([d for d in dist if d <= K])