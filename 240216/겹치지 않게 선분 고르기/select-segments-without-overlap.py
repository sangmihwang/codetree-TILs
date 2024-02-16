import sys
input = sys.stdin.readline

def sol(i, s, e):
    global cnt, maxCnt
    if i == n:
        if cnt > maxCnt:
            maxCnt = cnt
        return
    newS, newE = lines[i][0], lines[i][1]
    if newS > e:
        cnt += 1
        sol(i+1, newS, newE)
        cnt -= 1
        sol(i+1, s, e)


n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
lines.sort()
i = 0
cnt, maxCnt = 0, 0
sol(0, -1, 0)
print(maxCnt)