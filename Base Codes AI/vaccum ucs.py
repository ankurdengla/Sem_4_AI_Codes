import random
import heapq

pq = []
heapq.heapify(pq)

def findx(curr_pos):
    if (curr_pos == "00"):
        return 0
    if (curr_pos == "01"):
        return 0
    if (curr_pos == "10"):
        return 1
    if (curr_pos == "11"):
        return 1
def findy(curr_pos):
    if (curr_pos == "00"):
        return 0
    if (curr_pos == "01"):
        return 1
    if (curr_pos == "10"):
        return 0
    if (curr_pos == "11"):
        return 1

def rule(cstatus, x, y, c, n, m, visited):
    flag = 0
    while flag == 0:
        r = random.randrange(4)
        if (r == 0 and x - 1 >= 0):
            heapq.heappush(pq,(x-1, y, cstatus))
            flag = 1
        elif (r == 1 and x + 1 < n):
            heapq.heappush(pq,(x+1, y, cstatus))
            flag = 1
        elif (r == 2 and y - 1 >= 0):
            heapq.heappush(pq,(x, y-1, cstatus))
            flag = 1
        elif (r == 3 and y + 1 < m):
            heapq.heappush(pq,(x, y+1, cstatus))
            flag = 1
    return


def func(fl, x, y, c, n, m, visited):
    flag = 0
    heapq.heappush(pq, (x, y, fl))
    prevx = -1
    prevy = -1
    while pq:
        tup = heapq.heappop(pq)
        x = tup[0]
        y = tup[1]
        cstatus = tup[2]
        flag = 0
        for i in range(n):
            for j in range(m):
                if cstatus[i][j] == 1:
                    flag = 1
        if flag == 0:
            print(x, y)
            print(cstatus)
            return
        # tup = heapq.heappop(pq)
        # x = tup[0]
        # y = tup[1]
        # cstatus = tup[2]
        if (cstatus[x][y] == 1):
            cstatus[x][y] = 0
            print('S ')
        if (prevx != -1 and prevy != -1):
            if (prevx == x):
                if (prevy + 1 == y):
                    print('R ')
                elif (prevy - 1 == y) :
                    print('L ')
            elif (prevy == y):
                if (prevx + 1 == x):
                    print('D ')
                elif (prevx - 1 == x):
                    print('U ')

        if (x - 1 >= 0 and cstatus[x - 1][y] == 1):
            heapq.heappush(pq,(x-1, y, cstatus))
        elif (x + 1 < n and cstatus[x + 1][y] == 1):
            heapq.heappush(pq,(x+1, y, cstatus))
        elif (y - 1 >= 0 and cstatus[x][y - 1] == 1):
            heapq.heappush(pq,(x, y-1, cstatus))
        elif (y + 1 < m and cstatus[x][y + 1] == 1):
            heapq.heappush(pq,(x, y+1, cstatus))
        else:
            rule(cstatus, x, y, c, n, m, visited)
        prevx = x
        prevy = y


# n, m = input().split(' ')
# n = int(n)
# m = int(m)
curr_pos = input()
cstatu = []
for i in range(2):
    x = input().split(' ')
    l = [int(x[i]) for i in range(2)]
    cstatu.append(l)
visited = []
for i in range(2):
    visited.append([])
    for j in range(2):
        visited[i].append(0)
#print(cstatus)
x = findx(curr_pos)
y = findy(curr_pos)
c = 0
func(cstatu, x, y, c, 2, 2, visited)
#print(cstatu)