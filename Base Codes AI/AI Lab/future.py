def a_star( start, goal ):
	"""Perfoms an A* heuristic search"""
	# ATTEMPTED: does not work :(
	nodes = []
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		# We've run out of states - no solution.
		if len( nodes ) == 0: return None
		# Sort the nodes with custom compare function.
		nodes.sort( cmp )
		# take the node from the front of the queue
		node = nodes.pop(0)
		# if this node is the goal, return the moves it took to get here.
		print "Trying state", node.state, " and move: ", node.operator
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert( 0, temp.operator )
				if temp.depth <=1: break
				temp = temp.parent
			return moves
		#Expand the node and add all expansions to the end of the queue
		nodes.extend( expand_node( node, nodes ) )


		def bfs( start, goal ):
	"""Performs a breadth first search from the start state to the goal"""
	# A list (can act as a queue) for the nodes.
	nodes = []
	# Create the queue with the root node in it.
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		# We've run out of states, no solution.
		if len( nodes ) == 0: return None
		# take the node from the front of the queue
		node = nodes.pop(0)
		# Append the move we made to moves
		# if this node is the goal, return the moves it took to get here.
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth == 1: break
				temp = temp.parent
			return moves				
		# Expand the node and add all the expansions to the front of the stack
		nodes.extend( expand_node( node, nodes ) )

def h( state, goal ):
	"""Heuristic for the A* search. Returns an integer based on out of place tiles"""
	score = 0
	for i in range( len( state ) ):
		if state[i] != goal[i]:
			score = score + 1
	return score


			
def cmp( x, y ):
	# Compare function for A*. f(n) = g(n) + h(n). I use depth (number of moves) for g().
	return (x.depth + h( x.state, goal_state )) - (y.depth + h( x.state, goal_state ))
