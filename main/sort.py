
def sort(a):
    length = len(a)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a
