def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        a1 = quicksort(x[:i])
        a2 = quicksort(x[i + 1:])
        a1.append(x[i])
        return a1 + a2


list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(list1)
print(list1)