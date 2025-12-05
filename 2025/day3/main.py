
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
    
    f = open('input.txt', 'r')

    joltage = 0
    indx_range = [11,10,9,8,7,6,5,4,3,2,1,0]
    highest_joltage = []

    for line in f:
        c_list = []

        for c in line:
            if c == "\n":
                continue
            c_list.append(int(c))
        
        highest_j = []

        for i in indx_range:
            highest = c_list[i]
            highest_ind = i
            curr_indx = i+1

            while curr_indx+1 < len(c_list):
                if c_list[curr_indx+1] > highest:
                    highest = c_list[curr_indx+1]
                    highest_ind = curr_indx+1
                curr_indx+=1
            highest_j.append(highest)
            c_list.pop(highest_ind)
        
        highest_joltage.append(highest_j)
    
    print(highest_joltage)
        
    # Select the first 12 as the "highest numbers"
    # Search from the 12th if the next is higher, if so, take it
    # if not look at the next one

if __name__ == '__main__':
    solve_part2()