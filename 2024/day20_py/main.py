import numpy as np
import heapq

def dijkstra(matrix, start, end):
    
    rows, cols = matrix.shape
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distances = np.full((rows, cols), np.inf)
    distances[start] = 0

    # Priority queue for Dijkstra's algorithm (distance, (row, col))
    pq = [(0, start)]
    
    # To reconstruct the path
    parent = {start: None}

    while pq:
        current_distance, current_position = heapq.heappop(pq)
        row, col = current_position

        if current_position == end:
            break

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_position = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row, new_col] == 0:
                
                # Implement check for the direction and add additional score if necessary
                new_distance = current_distance + 1

                if new_distance < distances[new_position]:
                    distances[new_position] = new_distance
                    heapq.heappush(pq, (new_distance, new_position))
                    parent[new_position] = current_position

    if distances[end] == np.inf:
        print("NO PATH")
        return None
    
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return path

def find_pass_through(arr):

    row_patterns = []
    col_patterns = []

    pattern_1 = [0, 1, 0]

    pattern_1_len = len(pattern_1)
    rows, cols = arr.shape

    for i in range(rows):
        for j in range(cols - pattern_1_len + 1):
            if np.array_equal(arr[i,j:j+pattern_1_len], pattern_1):
                row_patterns.append(((i),(j,j+pattern_1_len)))              

    for i in range(rows - pattern_1_len + 1):
        for j in range(cols):
            if np.array_equal(arr[i:i+pattern_1_len,j], pattern_1):
                col_patterns.append(((i,i+pattern_1_len),(j)))

    return row_patterns, col_patterns

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(1)
        if char == '\n':
            continue
        if char == '.':
            line_ls.append(0)
        if char == 'S':
            line_ls.append(2)
        if char == 'E':
            line_ls.append(3)
    if line_ls != []:
        arr_ls.append(line_ls)

arr = np.array(arr_ls)

start_loc = np.where(arr == 2)
end_loc = np.where(arr == 3) 
start = (start_loc[0][0], start_loc[1][0])
end = ((end_loc[0][0], end_loc[1][0]))
arr[start] = 0
arr[end] = 0

solution = dijkstra(arr, start, end)
FULL_PATH = len(solution)

row_patterns, col_patterns = find_pass_through(arr)

len_finds = {}

for f in row_patterns:
    
    row_arr = arr.copy()
    row_arr[f[0],f[1][0]:f[1][1]] = 0
    solution = dijkstra(row_arr, start, end)
    if FULL_PATH - len(solution) not in len_finds:
        len_finds[FULL_PATH - len(solution)] = 1
    else:
        len_finds[FULL_PATH - len(solution)] += 1
  
for f1 in col_patterns:
    
    row_arr = arr.copy()
    row_arr[f1[0][0]:f1[0][1],f1[1]] = 0
    solution = dijkstra(row_arr, start, end)
    if FULL_PATH - len(solution) not in len_finds:
        len_finds[FULL_PATH - len(solution)] = 1
    else:
        len_finds[FULL_PATH - len(solution)] += 1

print(len_finds)

count = 0

for k in len_finds.keys():
    if k > 99:
        count += len_finds[k]

print(count)

# re-run the check keeping all starting positions


# Check each possible position for the racer to be
# At that position, to the next position there can only be
# - Direct pattern of 