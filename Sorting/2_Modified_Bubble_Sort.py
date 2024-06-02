# How to implement Modified Bubble sort using python
# Write a python function to implement Modified Bubble Sort

"""
In Modified Bubble sort, if there is no swapping taking place in any iteration, then list is sorted.
so we break from the logic/loop at that point.

# Tutorial Link
#   -> https://youtu.be/AFYpNdN83Zg?list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&t=388
"""


def modified_bubble_sort(data_list):
    l = len(data_list)
    for r in range(1, l):   # number of rounds is 1 less than length of input list
        swap_flag = 0       # using a flag to identify if swapping happened or not
        print(f'r is = {r}')
        for i in range(l - r):  # in each round comparison are Round number - 1
            # print(f'Comparison -> {i}')
            if data_list[i] > data_list[i + 1]:  # if first item is greater than second then swap
                data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]  # swapping items
                swap_flag = 1   # setting swapping flag to one when swapping happens
                # print(f'swap_flag is -> {swap_flag}')

        if swap_flag == 0:      # in any round/iteration if no swapping happens, break the loop
            # print(f'swap_flag is -> {swap_flag}')
            break
    return data_list


modified_bubble_sort([1, 2, 3, 4, 101, -5, 34, -1, -0.05])
# for 9 element list, its sorted in 7 iterations only

# modified_bubble_sort([1,2,4,3])
