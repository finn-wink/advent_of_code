import numpy as np

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

def window_checker(string, window):
    return

def solve_part2():

    f = open('input.txt', 'r')

    from_l = []
    to_l = []
    total_invalid = []
    count_invalid = 0

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
            if r < 11:
                continue
            r_str = str(r)
            chars = list(r_str)
            
            # 1 we will always check
            to_check = chars[0]
            matches = 0

            for i, c in enumerate(chars):
                if i != 0:
                    if c == to_check:
                        matches += 1
            
            if matches == len(r_str)-1:
                count_invalid += 1
                total_invalid.append(r)

            # If bigger than 3
            if len(r_str) > 3:
                
                window_size = 2
                # iterate through the window sizes
                while True:
                    # Only check the lengths that work
                    if len(r_str) % window_size == 0:
                        window = chars[0:window_size]
                        matches2 = 0
                        
                        # iterate through leftover windows
                        for ii in range(1, int(len(r_str)/window_size)):
                            ind1 = ii*window_size
                            ind2 = ind1+window_size
                            w_to_check = chars[ind1:ind2]
                            
                            if window != w_to_check:
                                break

                            matches2+=1

                            if matches2 == int(len(r_str)/window_size)-1:
                                count_invalid+=1
                                total_invalid.append(r)

                    if len(r_str) / window_size <= 2:
                        break
                    else:
                        window_size+=1

    total_invalid_l = list(set(total_invalid))
    print(total_invalid_l)
    final_result = sum(total_invalid_l)
    print(final_result)


if __name__ == '__main__':
    solve_part2()