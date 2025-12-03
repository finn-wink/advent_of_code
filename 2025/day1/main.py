import math

f = open('input.txt', 'r')

curr_num = 50
zeroes = 0

for line in f:
    line = line.strip()
    print(line)
    direction = line[0]
    distance  = int(line[1:])

    if direction == "L":
        new_num = curr_num - distance
    
    if direction == "R":
        new_num = curr_num + distance

    print("pre " + str(new_num))

    if curr_num != 0:
        if new_num < 0:
            zeroes += 1

    if new_num != 100:
        zeroes += math.floor(abs(new_num / 100))

    new_num = new_num % 100

    curr_num = new_num
    print(new_num)

    if new_num == 0:
        zeroes += 1

    print(zeroes)

# print(zeroes)