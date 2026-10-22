def rotate(key):
    M = len(key)
    result = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            result[j][M - 1 - i] = key[i][j]
    return result


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[i + M - 1][j + M - 1] != 1:
                return False
            return True


def solution(key, lock):
    M,N = len(key), len(lock)
    size = N + 2 * (M-1)
    board = [[0] * size for _ in range(size)]

    for i in range(N):
        for j in range(N):
            board[i + M - 1][j + M - 1] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(size - M + 1):
            for y in range(size - M + 1):    
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] += key[i][j]
                if check (board, M, N):
                    return True
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] -= key[i][j]
    return False
