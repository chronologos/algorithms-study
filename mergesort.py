"""Fri Jun 10 05:50:35 PDT 2016
A learning implementation of mergesort.
"""

# import random
import math
import sort_tester

def mergesort(unsorted_list):
    if len(unsorted_list) > 1:
        middle = int(math.floor(len(unsorted_list)/2))
        result = merge(mergesort(unsorted_list[:middle]), mergesort(unsorted_list[middle:]))
        return result
    else:
        return unsorted_list
def merge(lhs, rhs):
    print("merge")
    print(lhs)
    print(rhs)
    total_length = len(lhs)+len(rhs)
    sorted_list = []
    lpointer = 0
    rpointer = 0
    for i in range(0, total_length):
        if lpointer >= len(lhs):
            sorted_list.append(rhs[rpointer])
            rpointer += 1
        elif rpointer >= len(rhs):
            sorted_list.append(lhs[lpointer])
            lpointer += 1
        elif lhs[lpointer] < rhs[rpointer]:
            sorted_list.append(lhs[lpointer])
            lpointer += 1
        else:
            sorted_list.append(rhs[rpointer])
            rpointer += 1
    print(sorted_list)
    print("endmerge")
    return sorted_list

if __name__ == "__main__":
    # Run Some Tests
    tester = sort_tester.Tester(mergesort)
    tester.test()
    # for i in range(0, 20):
        # print("--")
        # rand_list = []
        # for i in range(0, random.randint(5, 20)):
            # rand_list.append(random.randint(1, 100))
        # original_list = rand_list[:]
        # sorted_list = mergesort(rand_list)
        # print("ol is: ", original_list)
        # print("rl is: ", rand_list)
        # print("sl is:", sorted_list)
        # original_list.sort()
        # if original_list != sorted_list:
            # print("sort() gives: ", original_list)
            # print("wrong")
        # else:
            # print("good")
