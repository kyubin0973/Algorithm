# 프로그래머스 154540 무인도 여행 (Lv2)
#
# 문제: 지도에서 상하좌우로 연결된 땅(숫자 칸)을 하나의 섬으로 보고,
#       섬마다 숫자 합을 오름차순으로 반환. 섬이 없으면 [-1]
# 제한: 지도 크기 최대 100 x 100
#
# 판단: 연결된 영역 찾기 + 영역별 값 누적 -> BFS (DFS도 가능)
#       칸 10,000개를 각각 한 번씩만 방문 -> 충분히 빠름
#       재귀 DFS는 섬이 크면 재귀 한도(1000)를 넘을 수 있어 BFS 선택
#
# 시간 복잡도: O(R * C)

from collections import deque

def solution(maps):
    #R: 행의 개수(세로), C: 열의 개수(가로)
    R, C = len(maps), len(maps[0])
    #방문 여부 확인을 위해 행열의 크기만큼 미방문으로 채워놓기
    visited = [[False] * C for _ in range(R)]
    #섬마다 머물 수 있는 날짜의 합
    answer = []
    
    # (sr, sc)에서 시작해 연결된 땅을 모두 방문하고, 숫자의 합을 반환
    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        total = 0
        
        while q:
            #queue에서 먼저 넣은 칸에서부터 가까운 곳부터 퍼져나가기
            r, c = q.popleft()
            #머물 수 있는 날짜 숫자로 바꿔서 넣기
            total += int(maps[r][c])
            
            #상하좌우 확인
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                #잘못된 범위로 나가지 않게 하기
                if 0 <= nr < R and 0 <= nc < C:
                    #바다가 아니고 방문하지 않은 섬
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        #큐에 넣기 전 방문 표시
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
        return total
    
    #지도 전체를 확인
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(bfs(r, c))

    #섬이 하나도 없으면 -1, 있다면 오름차순 정렬
    return sorted(answer) if answer else [-1]
                