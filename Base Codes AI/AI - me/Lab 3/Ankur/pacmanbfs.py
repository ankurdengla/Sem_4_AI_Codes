from copy import deepcopy
visited ={}

def isvalid(grid,x,y,m,n):
    return True if x >=0 and y >= 0 and x < m and y < n and grid[x][y] != '%' else False

def bfs( grid, pac_x, pac_y, f_x, f_y, rows, columns ):
    
    nodes = []
    expl = []
    global visited
   # visited = {}

    nodes.append( [create_node( pac_x, pac_y ), []] )

    while True:
        
        if len(nodes) == 0:
            return None

        node, path = nodes.pop()
        curr = deepcopy(path)
        curr.append(node)
        visited[(node.x,node.y)] = 1
        
        expl.append(node)

        if node.x == f_x and node.y == f_y:
            return expl,curr
        else:
            
            expanded_nodes = expand_node(grid,node, nodes, rows, columns)
            nodes = [[node, curr] for node in expanded_nodes] + nodes
                

def expand_node(grid,node,nodes,m,n):
    expanded_nodes = []
    global visited

    node1 = create_node(node.x+1,node.y)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n) :
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x,node.y+1)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n) :
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x,node.y-1)
    
    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n):
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x-1,node.y)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n):
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    return expanded_nodes

def create_node( x, y):
    	return Node( x, y)            

class Node:
    def __init__( self, x, y):
        self.x = x
        self.y = y

def main():
    pac_x, pac_y = map(int,input().strip().split())
    f_x, f_y = map(int,input().strip().split())
    rows, columns = map(int,input().strip().split())

    grid = []

    for i in range(rows):
        grid.append(list(input().strip()))

    expl,curr = bfs(grid,pac_x,pac_y,f_x,f_y,rows,columns)
    
    print (len(expl))
    for node in expl:
        print(node.x,node.y)

    
    print (len(curr)-1)
    for node in curr:
        print(node.x,node.y)

if __name__ == "__main__":
	main()
