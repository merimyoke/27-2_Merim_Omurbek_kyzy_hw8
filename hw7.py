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
    value = input('your number: ')
    n = len(rand)
    first = rand[0]
    last = n - 1
    resultOk = False
    pos = -1
    while first <= last:
        middle = (first + last) // 2
        if value == n[middle]:
            first = middle
            last = first
            resultOk = True
            pos = middle
        else:
            if value > n[middle]:
                first = middle + 1
            else:
                last = middle - 1
    else:
        if resultOk:
            print(f'your number has been found on index: {pos}')
        else:
            print('this number has not been found')


print(binary_search())
