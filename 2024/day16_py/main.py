import numpy as np
import copy
import heapq

def find_direction(current, new):

    direction_diff = tuple(np.subtract(new, current)) 
    # print(direction_diff)
    # Determine direction
    if direction_diff == (0,1):
        return 2 # Right
    if direction_diff == (0,-1):
        return 3 # Left
    if direction_diff == (1,0):
        return 1 # Down
    if direction_diff == (-1,0):
        return 0 # Up


def dijkstra(matrix, start, end):
    
    rows, cols = matrix.shape
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    direc = 2

    distances = np.full((rows, cols), np.inf)
    distances[start] = 0

    # Priority queue for Dijkstra's algorithm (distance, (row, col))
    pq = [(0, start, direc)]
    
    # To reconstruct the path
    parent = {start: None}

    while pq:
        current_distance, current_position, current_direction = heapq.heappop(pq)
        row, col = current_position

        if current_position == end:
            break

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_position = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row, new_col] == 0:
                
                # Implement check for the direction and add additional score if necessary
                n_direc = find_direction(current_position, new_position)
                if n_direc == current_direction:
                    new_distance = current_distance + 1
                else:
                    new_distance = current_distance + 1001

                if new_distance < distances[new_position]:
                    distances[new_position] = new_distance
                    heapq.heappush(pq, (new_distance, new_position, n_direc))
                    parent[new_position] = current_position

    if distances[end] == np.inf:
        print("NO PATH")
        return None
    
    print(current_distance)

    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return path

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(1)
        if char == '.':
            line_ls.append(0)
        if char == 'E':
            line_ls.append(0)
        if char == 'S':
            line_ls.append(0)
    if line_ls != []:
        arr_ls.append(line_ls)

arr = np.array(arr_ls)
# start1 = np.where(arr == 2)
# end1 = np.where(arr== 1)

# start = (start1[0][0], start1[1][0])
# end = (end1[0][0], end1[1][0]) 
start = (139,1)
end = (1,139)
print(arr.shape)
shortest_path = dijkstra(arr, start, end)

print(shortest_path)