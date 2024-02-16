import sys
input = sys.stdin.readline

def sol(i):
    global cnt, maxCnt, newS, newE
    if i == n:
        if cnt > maxCnt:
            maxCnt = cnt
        return
    newS, newE = lines[i][0], lines[i][1]
    if overlapNone(selected, newS, newE):
        cnt += 1
        selected.append([newS, newE])
        sol(i+1)
        selected.pop()
        cnt -= 1
        sol(i+1)
    else:
        sol(i+1)

def overlapNone(selected, i, j):
    flag = True
    for line in selected:
        if not (i < j < line[0] < line [1] or line[0] < line[1] < i < j):
            flag = False            # 하나라도 겹치는게 나오면 False
    return flag

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
lines.sort()
i = 0
cnt, maxCnt = 0, 0
selected = []
sol(0)
print(maxCnt)