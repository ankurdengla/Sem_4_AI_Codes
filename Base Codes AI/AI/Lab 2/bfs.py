import copy
import time

start_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def swap_tile(original, new, board):

    new_board = copy.deepcopy(board)

    #print "new position before action", new_board

    x = new_board[new[0]][new[1]]
    new_board[original[0]][original[1]] = x
    new_board[new[0]][new[1]] = 0

    print "new position after action", new_board

    return new_board


def action(position, board):

    #print "applying", position, "to", board

    x = position[0]
    y = position[1]
    z = position[2]

    if z == None:
       return board
    elif z == 1:
       return swap_tile([x + 1, y], [x, y],board)
    elif z == 2:
       return swap_tile([x - 1, y], [x, y], board)
    elif z == 3:
       return swap_tile([x, y + 1], [x, y], board)
    elif z == 4:
       return swap_tile([x, y - 1], [x, y], board)


def next_states(current):

    	row = current[0]
	column = current[1]

	l = [((row - 1), column, 1), #Move Up
	      ((row + 1), column, 2), #Move Down
	      (row, (column - 1), 3), #Move Left
	      (row, (column + 1), 4)] #Move Right

	final = []

	for x in l:

	    tempx = x[0]
	    tempy = x[1]

	    if tempx > 2 or tempy > 2:
		continue
	    if tempx < 0 or tempy < 0:
		continue

	    final.append(x)

	return final

def is_goal(x):

	goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
	return (x == goal)

def find_zero(board): 
	for y,row in enumerate(board):
		for x,col in enumerate(row): 
			if board[y][x]==0: 
				return [y,x]

def BFS():

	global visited

	closed = []
	open = [start_state]   

	while len(open) > 0:

	    x = open.pop()

	    #print "pop", x

	    if is_goal(x):
		return x  

	    print "not goal"

	    if (x in closed) == False:

		#print "not visited"

		current = find_zero(x)
		moves = next_states(current)

		#print "legal moves", moves

		for move in moves:
		    y = action(move,x)
		    #print "successor state", y
		    open.append(y)

		closed.append(x)
		visited += 1

	return None

print start_state

print find_zero(start_state)

visited = 0

solution = BFS()

if solution: 
	print "Yes" 
	print solution 
else: 
	print "No"
	print visited, "nodes visited"
