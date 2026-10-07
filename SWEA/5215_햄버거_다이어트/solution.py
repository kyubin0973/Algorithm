# SWEA 5215 햄버거 다이어트 (D3)
#
# 문제: 재료 N개(점수, 칼로리) 중 칼로리 합이 L 이하인 조합의 최대 점수
# 제한: N <= 20, L <= 10^4
#
# 판단: 재료마다 넣는다/안 넣는다, 개수 자유 -> 부분집합
#       2^20 = 약 100만 -> 완전 탐색 가능
# 가지치기: 칼로리 합이 L을 넘으면 더 내려가지 않는다
#
# 시간 복잡도: O(2^N)


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    #재료 수, 제한 칼로리 나눠서 N과 L에 저장.
    N, L = map(int, input().split())
    score = []
    cal = []

    #입력된 N에 대한 정보를 N만큼 반복하며 점수(s), 칼로리(c)로 나눠서 각각 score와 cal배열에 넣어주기
    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        cal.append(c)

    max_score = 0

    #재료 번호, 지금까지 넣기로 한 재료들의 합산 점수, 합산 칼로리를 받아서 계산하기
    def subset(idx, total_score, total_cal):
        global max_score

        #가지치기 : 합산 칼로리가 제한 칼로리를 초과 시
        if total_cal > L:
            return

        #모든 재료의 결정이 끝날 시 최고점수 갱신 후
        if idx == N:
            max_score = max(max_score, total_score)
            return

        #재료를 넣는 경우
        subset(idx + 1, total_score + score[idx], total_cal + cal[idx])

        #재료를 안넣는 경우
        subset(idx + 1, total_score, total_cal)

    subset(0, 0, 0)

    print(f"#{tc} {max_score}")