from random import randint

rand = []
n = 10
for i in range(n):
    rand.append(randint(1, 10))
print(rand)


def selectionSort(number):
    length = len(rand)

    for k in range(length - 1):
        minimal = k

        for sorting in range(k + 1, length):
            if number[sorting] < number[minimal]:
                minimal = sorting

        number[k], number[minimal] = number[minimal], number[k]

    return number


print(selectionSort(rand))


def binary_search():
    value = int(input('choose a number from 1 to 10: '))
    a = rand
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return 'this number does not exist in this list'
    else:
        return f'your number is found on index: {mid}'


print(binary_search())
