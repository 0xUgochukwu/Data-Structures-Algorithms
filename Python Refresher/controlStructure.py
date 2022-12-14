def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_positive_num = float('inf')
    for i in in_list:
        if i >= 0 and i < smallest_positive_num:
            smallest_positive_num = i
    
    return smallest_positive_num

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2