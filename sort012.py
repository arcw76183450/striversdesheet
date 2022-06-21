def sort012(arr, n):
    count0, count1, count2 = 0
    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    index = 0
    while count0 > 0:
        arr[index] = 0
        index += 1
        count0 -= 1
    while count1 > 0:
        arr[index] = 1
        index += 1
        count1 -= 1
    while count2 > 0:
        arr[index] = 2
        index += 1
        count2 -= 1

    return arr


arr = [0, 1, 2, 1, 0, 1, 2, 1, 0, 0, 0, 2, 1]
n = len(arr)
print(sort012(arr, n))
