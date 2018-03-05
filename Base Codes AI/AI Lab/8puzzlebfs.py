import copy

class Node:
	def __init__(self, row, col, adj, n):
		self.row = row
		self.col = col
		self.adj = copy.deepcopy(adj)
		self.n = n
		#self.operation = operation
		self.par = None
	def isGoal(self):
		if (self.adj == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]):
			return True
		else:
			return False
	def get_val(self):
		num = 0
		for i in range (0,self.n):
			for j in range (0, self.n):
				num = num*10 + self.adj[i][j]
		return num
	def __eq__(self,other):
		return self.get_val() == other.get_val()
	def copy1(self):
		return copy.deepcopy(self)
	def __hash__(self):
		return hash(self.get_val())

def successor(state):
	children = []
	if (state.row > 0):
		other = state.copy1()
		temp = other.adj[other.row][other.col]
		other.adj[other.row][other.col] = other.adj[other.row-1][other.col]
		other.adj[other.row-1][other.col] = temp
		other.row = state.row - 1
		other.par = state
		#other.operation = "Up"
		children.append(other)

	if (state.row < state.n - 1):
		other = state.copy1()
		temp = other.adj[other.row][other.col]
		other.adj[other.row][other.col] = other.adj[other.row+1][other.col]
		other.adj[other.row+1][other.col] = temp
		other.row = state.row + 1
		other.par = state
		#other.operation = "Down"
		children.append(other)

	if (state.col > 0):
		other = state.copy1()
		temp = other.adj[other.row][other.col]
		other.adj[other.row][other.col] = other.adj[other.row][other.col-1]
		other.adj[other.row][other.col-1] = temp
		other.col = state.col - 1
		other.par = state
		#other.operation = "Left"
		children.append(other)

	if (state.col < state.n - 1):
		other = state.copy1()
		temp = other.adj[other.row][other.col]
		other.adj[other.row][other.col] = other.adj[other.row][other.col+1]
		other.adj[other.row][other.col+1] = temp
		other.col = state.col + 1
		other.par = state
		#other.operation = "Right"
		children.append(other)

	return children

def bfs():
	adj = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
	initial = Node(1,1,adj,3)
	display(initial.adj)
	if (initial.isGoal()):
		return initial
	frontier = list()
	explored = set()
	frontier.append(initial)
	explored.add(initial.get_val)
	while(frontier):
		state = frontier.pop(0)
		if (state.isGoal()):
			return state
		children = successor(state)
		for child in children:
			if (child.get_val() not in explored):
				frontier.append(child)
				explored.add(child.get_val)

	return None			

def display( state ):
	#if (operation)
	#	print (operation)
    print ("----------------")
    print ("| %i | %i | %i |" % (state[0][0], state[0][1], state[0][2]))
    print ("----------------")
    print ("| %i | %i | %i |" % (state[1][0], state[1][1], state[1][2]))
    print ("----------------")
    print ("| %i | %i | %i |" % (state[2][0], state[2][1], state[2][2]))
    print ("----------------")

def printsol(sol):
	path = []
	path.append(sol)
	parent = sol.parent
	while parent:
		path.append(parent)
		parent = parent.par

	for t in range(len(path)):
		state = path[len(path) - t - 1]
		display(state.adj)

def main():
	sol = bfs()
	if (sol):
		printsol(sol)

main()