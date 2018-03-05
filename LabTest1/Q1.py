class Graph():
     
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]
 
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                print (v,i,colour[i])
                return False
        return True
     

    def graphColourUtil(self, m, colour, v):
        if m == 0:
            return False
        
        if v == self.V:
            return True
 
        for c in range(1, m+1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v+1) == True:
                    return True
                #colour[v] = 0
        return False
 
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            print ("No solution exists")
            return False
 
        print ("Solution Exists: Following are the assigned colours:")
        for c in colour:
            print (c, end = ' '),
        return True
 
def main():
    v = int(input())
    g  = Graph(v)
    # grid = [[0 for column in range(v)]\
    #                         for row in range(v)]

    grid = []

    for i in range (v):
        grid.append(list(map(int,input().strip().split())))
        # for j in range (v):
            # grid[i][j] = int(input())

    #for i in range (v):
        #for j in range (v):
            #grid[i][j] = int(grid[i][j])

    g.graph = grid

    # for i in range (v):
    #     print (grid[i]) 

    m = int(input())
    g.graphColouring(m)
    print(' ')

if __name__ == "__main__":
    main()
 
