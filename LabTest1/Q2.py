from queue import Queue
from copy import deepcopy

def Safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False   
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_queens(q, board, n):
    while not q.empty():
        cur_state = q.get()
        cur_board = cur_state[0]
        col = cur_state[1]
        #print (col)
        for i in range(n):
            if Safe(cur_board, i, col, n):
                cur_board[i][col] = 1
                q.put((deepcopy(cur_board), col+1))
                if col == n - 1:
                    return cur_board
                cur_board[i][col] = 0
    return False

def main():
    n = 4
    board = [[0] * n for i in range(n)]
    q = Queue()
    q.put(( board, 0))
    sol = n_queens(q, board, n)
    if not sol:
        print("No Solution")
    else:
        for x in sol:
            for y in x:
                print(y, end = ' ')
            print('\n')

if __name__== "__main__":
    main()