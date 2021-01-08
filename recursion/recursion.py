# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 4! = 4 * 3 * 2 * 1
import math


def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!
# -----------
# 0! = 0 * -1!
# -1! = -1 * -2!

def non_recursion_factorial(num):
    output = 1
    while num > 0:
        output = output * num
        num = num - 1


# 1 1 2 3 5 8

def fib(index):
    if index == 1 or index == 2:
        return 1
    return fib(index - 1) + fib(index - 2)


def merge_sort(nums):
    if nums == []:
        return []

    if len(nums) == 1:
        return nums

    def split_in_two(arr):
        # 4 --> 2, 01 23
        # 5 --> 3, 012 34
        # 6 --> 3, 012 345
        # 7 --> 4, 0123 456

        middle_index = math.ceil(len(arr) / 2)
        return arr[:middle_index], arr[middle_index:]

    def merge_sorted_arrays(arr1, arr2):
        print()
        print('merging', arr1, arr2)
        i1 = 0
        i2 = 0
        sorted_arr = []
        while(i1 < len(arr1) and i2 < len(arr2)):
            if (arr1[i1] < arr2[i2]):
                sorted_arr.append(arr1[i1])
                i1 += 1
            else:
                sorted_arr.append(arr2[i2])
                i2 += 1

            # print('SORTED ARRAY', sorted_arr)

        # the "lazy" way -- knowing one list will be empty
        # sorted_arr.extend(arr1[i1:] + arr2[i2:])

        # print('-----> indexes', i1, i2)

        if i1 >= len(arr1):
            # print('starting at index', i2)
            # print('extending by', arr2[i2:])
            sorted_arr.extend(arr2[i2:])
        else:
            # print('starting at index', i1)
            # print('extending by', arr1[i1:])
            sorted_arr.extend(arr1[i1:])

        print('(()) merge returning', sorted_arr)
        return sorted_arr

    # split
    (n1, n2) = split_in_two(nums)

    # print()
    # print(n1)
    # print(n2)
    # print()

    # sort
    sorted_n1 = merge_sort(n1)
    sorted_n2 = merge_sort(n2)

    # print('****** sorted n1', sorted_n1)
    # print('****** sorted n2', sorted_n2)

    # merge
    print()
    return merge_sorted_arrays(sorted_n1, sorted_n2)


# write it out

#### every new penguin
# what is nums?
# what is n1, n2

###  every step of the while loop
# what is arr1, arr2, i1, i2, sorted_arr 
# with arrows on the whiteboard for i1, i2