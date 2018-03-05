M, N = 0, 0
GRAPH = None
STUDENTS = None
ADJACENT = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2)]
ADJACENT.remove((0, 0))
SEAT_MATRIX = None

class Student(object):
    '''STUDENT NODE'''
    def __init__(self, roll_no, friends):
        self.roll_no = roll_no
        self.friends = friends
        self.remaining_seats = [(row, column) for column in range(N) for row in range(M)]
        self.sitting = False
    
    def __repr__(self):
        return self.roll_no

def seat_exists(x, y):
    return x >= 0 and x < M and y >= 0 and y < N

def make_graph():
    global GRAPH
    GRAPH = {}
    for student in STUDENTS:
        GRAPH[student.roll_no] = []
        for other_student in STUDENTS:
            if other_student.roll_no not in student.friends:
                GRAPH[student.roll_no] += [other_student.roll_no]

def check_valid(student, seat):
    for dx, dy in ADJACENT:
        if seat_exists(seat[0] + dx, seat[1] + dy):
            if SEAT_MATRIX[seat[0]+dx][seat[1]+dy] is None:
                continue
            elif SEAT_MATRIX[seat[0] + dx][seat[1] + dy].roll_no in GRAPH[student.roll_no]:
                return False
    return True

def set_seat(student, seat):
    if seat in student.remaining_seats and check_valid(student, seat):
        SEAT_MATRIX[seat[0]][seat[1]] = student
        student.sitting = True
        for other_student in STUDENTS:
            if other_student.roll_no in GRAPH[student.roll_no]:
                other_student.remaining_seats.remove(seat)
        return True

def remove_seat(student, seat):
    SEAT_MATRIX[seat[0]][seat[1]] = None
    student.sitting = False
    for other_student in STUDENTS:
        if other_student.roll_no in GRAPH[student.roll_no]:
            other_student.remaining_seats.append(seat)

# DOESN'T WORK
def arc_consistency():
    for student in STUDENTS:
        for other_student in STUDENTS:
            if other_student.roll_no in GRAPH[student.roll_no]:
                pass


def backtrack(seat):
    STUDENTS.sort(key=lambda x: (len(x.remaining_seats), len(x.friends), x.roll_no))
    for student in STUDENTS:
        if not student.sitting and check_valid(student, seat):
            set_seat(student, seat)
            if seat == (M - 1, N - 1):
                return True
            if seat[1] == N - 1:
                possible = backtrack((seat[0] + 1, 0))
            else:
                possible = backtrack((seat[0], seat[1] + 1))
            if possible:
                return True
            remove_seat(student, seat)
    return False

def print_seating_arrangement():
    for row in range(M):
        for column in range(N):
            print(SEAT_MATRIX[row][column], end='\t')
        print()

def main():
    global STUDENTS, SEAT_MATRIX, M, N
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().strip().split())
        SEAT_MATRIX = [[None for _ in range(N)] for __ in range(M)]
        STUDENTS = []
        for _ in range(M * N):
            line = input().strip().split()
            STUDENTS.append(Student(line[0], set(line[2:])))
        make_graph()
        backtrack((0, 0))
        print_seating_arrangement()

if __name__ == '__main__':
    main()
