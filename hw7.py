from random import randint


def binary_search(search_object, list):
    list.sort()

    middle = len(list) // 2
    last = 0
    first = len(list) - 1

    while list[middle] != search_object and last <= first:
        if search_object > list[middle]:
            last = middle + 1
        else:
            first = middle - 1
        middle = (last + first) // 2

    if last > first:
        print("Not found")
    else:
        print(f"index = {middle}")
binary_search(5, [1,2,3,4,5,6,7,8,9,10])


def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        for k in range(len(unsorted_list) - i - 1):
            if unsorted_list[k] > unsorted_list[k + 1]:
                unsorted_list[k], unsorted_list[k + 1] = unsorted_list[k + 1], unsorted_list[k]
    print(f"your sorted list: {unsorted_list}")
bubble_sort([5,4,9,10,3,7,2,8,1,6])