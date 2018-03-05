import random

a = 5
b = 2

def calc(fl, visited, x, y, n, m):
	if (n == 1 and m == 1):
		if (fl[0][0] == 1):
			print('Sucked at', 0, 0)
			fl[0][0] = 0
			visited[0][0] = 1
		else :
			visited[0][0] = 1
			return
	# f = 1
	# for i in range(n):
	# 	for j in range(m):
	# 		if (visited[i][j] == 0):
	# 			f = 0
	# if (f == 1):
	# 	return
	# 	visited[x][y] = 1
	# if (x-1 >= 0 and fl[x-1][y] == 1):
	# 	print('Up from',x,y, ' to ', x-1, y)
	# 	calc(fl,visited,x-1,y,n,m)
	# elif (y+1 < m and fl[x-1])
	q = PriorityQueue()
	q.put()



n, m = input.split(' ')
n = int(n)
m = int(m)
fl = []
visited = []
for i in range(n):
	for j in range(m):
		x = random.randrange(2)
		fl[i].append(x)
		visited[i].append(0)
x = random.randrange(n)
y = random.randrange(m)
calc(fl,visited,x,y,n,m)