
def solve_part1():

    f = open('input.txt', 'r')

    from_l = []
    to_l = []
    total_invalid = 0

    for line in f:
        str_splt = line.split(",")

    for pair in str_splt:
        pair_splt = pair.split("-")
        from_l.append(int(pair_splt[0]))
        to_l.append(int(pair_splt[1]))

    # Iterate over both lists to get the range
    for i, x in enumerate(from_l):
        start = x
        end = to_l[i]

        for r in range(start, end+1):
            r_str = str(r)
            mid = len(r_str) // 2

            if r_str[:mid] == r_str[mid:]:
                total_invalid += r
                print(r)

    print(total_invalid)

def solve_part2():

    f = open('input.txt', 'r')

    from_l = []
    to_l = []
    total_invalid = 0

    for line in f:
        str_splt = line.split(",")

    for pair in str_splt:
        pair_splt = pair.split("-")
        from_l.append(int(pair_splt[0]))
        to_l.append(int(pair_splt[1]))

    # Iterate over both lists to get the range
    for i, x in enumerate(from_l):
        start = x
        end = to_l[i]

        for r in range(start, end+1):
            r_str = str(r)
            max_char = len(r_str) // 2 

            # Create combination to check
            # If less than 1 skip
            if len(r_str) == 1:
                continue 
            
            # Iterate through the window size
            for w in range(1,max_char):
                matching = r_str[0:w]

                print("Matching " + matching)
            
                # Iterate over the string to see if it's a match, if not, move on
                for letter in r_str[1:]:
                    if matching == letter:
                        total_invalid += 1
                        print("Matched!")
                        print(matching + letter)


if __name__ == '__main__':
    solve_part2()