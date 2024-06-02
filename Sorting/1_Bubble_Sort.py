# How to implement Bubble sort using python
# Write a python function to implement Bubble Sort

"""
In Bubble sort, we compare value at first index to value at second index of a List of N items
and in case values needs to be swapped in order to sort them
we swap the values, otherwise we let them stay at their indexes.

For a list of N items we need to perform N-1 Comparison.

After one round of these steps, the largest item will reach the last position of List
In next iteration/Round we will not do anything on last item,
we will now consider only N-1 items and perform comparisons N-2 Times.

We will keep on doing this until this has been done for N-1 rounds.

# Tutorial Link
#   -> https://www.youtube.com/watch?v=AFYpNdN83Zg&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&t=62s
#   -> https://www.youtube.com/watch?v=4iNPAFH8rTM&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=40
"""


def bubble_sort(data_list):
    l = len(data_list)
    for r in range(1, l):  # number of rounds is 1 less than length of input list
        print(f'r is = {r}')
        for i in range(l - r):  # in each round comparison are Round number - 1
            # print(f'Comparison -> {i}')
            if data_list[i] > data_list[i + 1]:  # if first item is greater than second then swap
                data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]  # swapping items
    return data_list


bubble_sort([4, 3, 1, 2, 101, -5, 34, -1, -0.05])
