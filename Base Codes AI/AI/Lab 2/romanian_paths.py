
GRAPH = {\
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},\
            'Zerind': {'Arad': 75, 'Oradea': 71},\
            'Oradea': {'Zerind': 71, 'Sibiu': 151},\
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Faragas': 99, 'Rimnicu': 80},\
            'Timisoara': {'Arad': 118, 'Lugoj': 111},\
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},\
            'Mehadia': {'Lugoj': 70, 'Dobreta': 75},\
            'Dobreta': {'Mehadia': 75, 'Craiova': 120},\
            'Craiova': {'Dobreta': 120, 'Rimnicu': 146, 'Pitesti': 138},\
            'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},\
            'Faragas': {'Sibiu': 99, 'Bucharest': 211},\
            'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},\
            'Bucharest': {'Faragas': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
            'Giurgiu': {'Bucharest': 90},\
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},\
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},\
            'Eforie': {'Hirsova': 86},\
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},\
            'Iasi': {'Vaslui': 92, 'Neamt': 87},\
            'Neamt': {'Iasi': 87}\
        }

def dfs_paths(s, dest, path=None):
    if path is None:
        path = [s]
    if s == dest:
        yield path
    for next_node in set(GRAPH[s].keys()) - set(path):
        yield from dfs_paths(next_node, dest, path + [next_node])

def main():
    print('Source', end=' ')
    source = input().strip()
    print('Destination', end=' ')
    goal = input().strip()
   
    paths = dfs_paths(source, goal)
    for path in paths:
        print(' -> '.join(city for city in path))

if __name__ == '__main__':
    main()
