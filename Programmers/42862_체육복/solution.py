# 프로그래머스 42862 체육복 (Lv1)
#
# 문제: 체육복을 도난당한 학생이 앞뒤 번호 학생에게 여벌을 빌릴 때,
#       수업을 들을 수 있는 학생의 최댓값 구하기
# 제한: 학생 수 n <= 30
#
# 판단: 번호가 작은 학생부터, 앞 번호에게 먼저 빌려주면 항상 최선 -> 그리디
#       (앞 번호에게 줄 수 있는데 뒤 번호에게 주면, 뒤쪽 학생이 빌릴 기회를 낭비함)
#
# 시간 복잡도: O(N log N) (정렬)

def solution(n, lost, reserve):
    # 여벌이 있는데 도난당한 학생은 자기 것을 입어야 하므로 양쪽에서 모두 제외
    set_lost = set(lost) - set(reserve)        # 실제로 빌려야 하는 학생
    set_reserve = set(reserve) - set(lost)     # 실제로 빌려줄 수 있는 학생

    # 번호가 작은 학생부터 빌려줄 상대를 찾는다
    for i in sorted(set_reserve):
        # 앞 번호 학생이 필요하면 먼저 빌려준다
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        # 앞 번호가 필요 없을 때만 뒤 번호 학생에게 빌려준다
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    # 전체 학생 수 - 끝까지 못 빌린 학생 수
    return n - len(set_lost)