
def insertionSort(ls):

    for x in range(1, len(ls)):
        temp = ls[x]
        j = x-1

        while j >= 0 and ls[j] > temp:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = temp
    return ls
ls = [4,6,3,9,56,1,7]
print('Before Insertion Sort:', ls)
insertionSort(ls)
print('After Insertion Sort:', ls)