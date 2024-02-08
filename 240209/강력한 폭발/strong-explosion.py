import sys

# 계속 사용할거라서 bomb 함수 실행할때마다 계속 만드는 것보다 한번 만들어두고 계속 사용하는게 빠름
b1 = [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)]
b2 = [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)]
b3 = [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]

def bomb(x, y, num, explo):
    cnt = 0
    if num == 1:
        for (i, j) in b1:
            if 0 <= x+i < n and 0 <= y+j < n and not explo[x+i][y+j]:
                explo[x+i][y+j] = 1
                cnt += 1
    elif num == 2:
        for (i, j) in b2:
            if 0 <= x+i < n and 0 <= y+j < n and not explo[x+i][y+j]:
                explo[x+i][y+j] = 1
                cnt += 1
    elif num == 3:
        for (i, j) in b3:
            if 0 <= x+i < n and 0 <= y+j < n and not explo[x+i][y+j]:
                explo[x+i][y+j] = 1
                cnt += 1
    return cnt

# 변수로 지금 폭탄이 터져있는 상태의 맵 추가
def sol(N, bombCnt, now_explo):
    global maxCnt
    if N == bombN:
        if bombCnt > maxCnt:
            maxCnt = bombCnt
        return
    for i in range(1, 4):
        # tmp 는 이전단계에서 받아온 필드상태(아직 1, 2, 3 번을 추가로 터트리기 전 상태)
        # 1, 2, 3번 폭탄 터트릴 때, 터트릴 필드는 새로 만들어서 보내줘야함.
        # global의 exploded에서 계속 폭탄을 터트리는 방법으로 하려면, sol 함수 실행 후, 폭탄제거함수도 만들어서 실행해줘야함.
        tmp = [[now_explo[x][y] for y in range(n)] for x in range(n)]
        plus_score = bomb(bombs[N][0], bombs[N][1], i, tmp)
        sol(N+1, bombCnt + plus_score, tmp)

n = int(input())

bombs = []                   # 폭탄 위치 리스트
exploded = [[0]*n for _ in range(n)]    # 폭탄 터진 곳 표시 행렬
maxCnt = 0

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            bombs.append((i, j))
            exploded[i][j] = 1
bombN = len(bombs)           # 폭탄 개수

sol(0, bombN, exploded)
print(maxCnt)