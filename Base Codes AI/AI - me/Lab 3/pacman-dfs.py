import collections


def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):

    result = dfs_iterative(r, c, pacman_r, pacman_c, food_r, food_c, grid)

    print len(result['visited'])
    for pos in result['visited']:
        print str(pos[0]) + ' ' + str(pos[1])

    path = reconstruct_path((food_r, food_c), result['came_from'])
    print len(path)-1
    for pos in path:
        print str(pos[0]) + ' ' + str(pos[1])


def dfs_iterative(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    fringe = collections.deque()
    came_from = {} 
    visited = []
    start = (pacman_r, pacman_c)
    fringe.append(start)
    came_from[start] = None

    while len(fringe) > 0:
        current = fringe.pop()
        visited.append(current)

        if is_goal(current, grid):
            return {'visited': visited, 'came_from': came_from}
        neighbours = get_neighbours(current, grid)
        for next in neighbours:
            if next not in came_from and next not in fringe:
                came_from[next] = current
                fringe.append(next)

def get_neighbours(pos, grid):
    (x, y) = pos
    neighbours = [(x-1, y  ),  # up
                  (x,   y-1),  # left
                  (x,   y+1),  # right
                  (x+1, y  )]  # down
    neighbours = filter(lambda x: is_wall(x, grid), neighbours)
    return neighbours


def is_wall(pos, grid):
    return grid[pos[0]][pos[1]] != '%'  # wall


def is_goal(pos, grid):
    return grid[pos[0]][pos[1]] == '.'  # food


def is_start(pos, grid):
    return grid[pos[0]][pos[1]] == 'P'  # pacman


def reconstruct_path(goal, came_from):
    current = goal
    path = [current]
    while not is_start(current, grid):
        current = came_from[current]
        path.append(current)
    return path[::-1]  # reverse




# input
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

