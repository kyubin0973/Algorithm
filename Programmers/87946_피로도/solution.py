# 프로그래머스 87946 피로도 (Lv2)
#
# 문제: 피로도 k로 던전을 최대 몇 개 돌 수 있는가 (던전마다 [최소 필요 피로도, 소모 피로도])
# 제한: 던전 최대 8개
#
# 판단: 도는 순서에 따라 결과가 달라짐 -> 순열
#       8! = 40,320 -> 완전 탐색 가능
#
# 시간 복잡도: O(N! * N)

from itertools import permutations

def solution(k, dungeons):
    # 지금까지 확인한 순서들 중 가장 많이 돈 던전 수
    answer = 0

    # 던전을 도는 모든 순서를 하나씩 시도
    for path in permutations(dungeons, len(dungeons)):
        cnt = 0   # 이 순서로 돈 던전 수
        tmp = k   # 이 순서에서의 남은 피로도 (순서마다 k로 초기화)

        # 정해진 순서대로 던전을 방문
        for need, spend in path:
            # 남은 피로도가 최소 필요 피로도 이상이어야 입장 가능
            if tmp >= need:
                tmp -= spend
                cnt += 1
            # 입장 못 하는 던전은 건너뛰고 다음 던전으로 진행

        # 이 순서의 결과로 최댓값 갱신
        answer = max(answer, cnt)

    return answer