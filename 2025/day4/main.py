import numpy as np

def solve_part1():

    f = open('input.txt', 'r')

    list_matrix = []

    for line in f:
        list_line = []
        for c in line:
            if c == '.':
                list_line.append(0)
            if c == '@':
                list_line.append(1)

        list_matrix.append(list_line)
    
    matrix = np.array(list_matrix)

    matches = 0 

    # Create buffer around matrix to avoid errors
    matrix = np.c_[np.zeros(matrix.shape[0]), matrix, np.zeros(matrix.shape[0])]
    matrix = np.vstack([np.zeros(matrix.shape[1]), matrix, np.zeros(matrix.shape[1])])

    for y in range(1, matrix.shape[0]-1):
        for x in range(1, matrix.shape[1]-1):
            if matrix[y,x] != 0:
                count = 0
                if matrix[y-1,x-1] == 1:
                    count+=1
                if matrix[y-1,x] == 1:
                    count+=1
                if matrix[y-1,x+1] == 1:
                    count+=1
                if matrix[y,x-1] == 1:
                    count+=1
                if matrix[y,x+1] == 1:
                    count+=1
                if matrix[y+1,x-1] == 1:
                    count+=1
                if matrix[y+1,x] == 1:
                    count+=1
                if matrix[y+1,x+1] == 1:
                    count+=1
            
                if count < 4:
                    matches+=1
                    print("X:"+str(y))
                    print("Y:"+str(x))

    print(matches) 


def reduce_matrix(matrix):
    
    changes = 0
    to_change = []

    for y in range(1, matrix.shape[0]-1):
        for x in range(1, matrix.shape[1]-1):
            if matrix[y,x] != 0:
                count = 0
                if matrix[y-1,x-1] == 1:
                    count+=1
                if matrix[y-1,x] == 1:
                    count+=1
                if matrix[y-1,x+1] == 1:
                    count+=1
                if matrix[y,x-1] == 1:
                    count+=1
                if matrix[y,x+1] == 1:
                    count+=1
                if matrix[y+1,x-1] == 1:
                    count+=1
                if matrix[y+1,x] == 1:
                    count+=1
                if matrix[y+1,x+1] == 1:
                    count+=1
            
                if count < 4:
                    changes+=1
                    to_change.append((y,x))
                    print("X:"+str(y))
                    print("Y:"+str(x))
    
    for cc in to_change:
        matrix[cc[0], cc[1]] = 0   

    return matrix, changes


def solve_part2():
    
    f = open('input.txt', 'r')

    list_matrix = []

    for line in f:
        list_line = []
        for c in line:
            if c == '.':
                list_line.append(0)
            if c == '@':
                list_line.append(1)

        list_matrix.append(list_line)
    
    matrix = np.array(list_matrix)

    matches = 0 

    # Create buffer around matrix to avoid errors
    matrix = np.c_[np.zeros(matrix.shape[0]), matrix, np.zeros(matrix.shape[0])]
    matrix = np.vstack([np.zeros(matrix.shape[1]), matrix, np.zeros(matrix.shape[1])])
    
    while True:
        matrix, changes = reduce_matrix(matrix)
        matches += changes
        if changes == 0:
            break
        print(changes)
    print(matches)

if __name__ == '__main__':
    solve_part2()