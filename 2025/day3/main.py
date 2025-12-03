
def solve_part1():

    f = open('input.txt', 'r')

    joltage = 0

    for line in f:

        c_list = []

        for c in line:
            if c == "\n":
                continue
            c_list.append(int(c))
        
        # Search for largest number -> remember index -> search for largest right of that.
        largest_ind = 0
        largest_num = 0
        second_ind = 0
        second_num = 0

        for i, num in enumerate(c_list):
            if i == len(c_list) - 1:
                continue
            if num > largest_num:
                largest_num = num
                largest_ind = i

        # Slice the list to the highest num
        new_c_list = c_list[largest_ind+1:]

        for j, num1 in enumerate(new_c_list):
            if num1 > second_num:
                second_num = num1
                second_ind = i

        to_add_str = str(largest_num) + str(second_num)
        to_add = int(to_add_str)
        joltage += to_add

    print(joltage)

def solve_part2():
    return

if __name__ == '__main__':
    solve_part1()