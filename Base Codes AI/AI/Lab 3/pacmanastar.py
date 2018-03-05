from copy import deepcopy
import sys
from functools import cmp_to_key

visited ={}
f_x = 0
f_y = 0

def calccost(node):
    global f_x
    global f_y
    return node.cost + abs(f_x-node.x)+ abs(f_y-node.y)

def compare( x, y ):
    node1, l1 = x
    node2, l2 = y
    return (node1.cost + calccost(node1)) - (node2.cost + calccost(node2))

def isvalid(grid,x,y,m,n):
    return True if x >=0 and y >= 0 and x < m and y < n and grid[x][y] != '%' else False

def dfs( grid, pac_x, pac_y, rows, columns ):
    global f_x
    global f_y
    
    nodes = []
    expl = []
    global visited
   # visited = {}

    nodes.append( [create_node( pac_x, pac_y, 1 ), []] )

    while True:
        
        if len(nodes) == 0:
            return None

        node, path = nodes.pop(0)
        curr = deepcopy(path)
        curr.append(node)
        visited[(node.x,node.y)] = 1
        
        expl.append(node)

        if node.x == f_x and node.y == f_y:
            return expl,curr
        else:
            expanded_nodes = expand_node(grid,node, nodes, rows, columns)
            nodes = [[node, curr] for node in expanded_nodes] + nodes
            sorted(nodes,key=cmp_to_key(compare))
                

def expand_node(grid,node,nodes,m,n):
    global f_x
    global f_y    
    expanded_nodes = []
    global visited

    node1 = create_node(node.x+1,node.y,node.cost+1)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n) :
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x,node.y+1,node.cost+1)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n) :
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x,node.y-1,node.cost+1)
    
    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n):
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    node1 = create_node(node.x-1,node.y,node.cost+1)

    if (node1.x,node1.y) not in visited and isvalid(grid,node1.x,node1.y,m,n):
        expanded_nodes.append(node1)
        visited[(node1.x,node1.y)] = 1

    return expanded_nodes

def create_node( x, y, cost):
    	return Node( x, y, cost)            

class Node:
    def __init__( self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

def main():
    global f_x
    global f_y
    pac_x, pac_y = map(int,input().strip().split())
    f_x, f_y = map(int,input().strip().split())
    rows, columns = map(int,input().strip().split())

    grid = []

    for i in range(rows):
        grid.append(list(input().strip()))

    expl,curr = dfs(grid,pac_x,pac_y,rows,columns)
    
    #print (len(expl))
    #for node in expl:
        #print(node.x,node.y)

    print (len(curr)-1)
    for node in curr:
        print(node.x,node.y)

if __name__ == "__main__":
	main()
