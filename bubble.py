

#Ascending Order
def bubbleAesc(list):

    for rval in range(len(list)-1, 0, -1):
        for indx in range(rval):
            if list[indx] > list[indx+1]:
                temp = list[indx+1]
                list[indx+1] = list[indx]
                list[indx] = temp
    return list

#Descending Order
def bubbleDesc(ls):

    for findx in range(len(ls)-1):
        for sindx in range(findx, len(ls)-1):
            if ls[sindx] < ls[sindx + 1]:
                temp = ls[sindx]
                ls[sindx] = ls[sindx + 1]
                ls[sindx + 1] = temp
    return ls


ls = [1000,23,45,2,3,1,8,56,11,25,31,100,89]
print(f'Before Bubble Sort:', ls)
ls = bubbleAesc(ls)
print(f'After Bubble Sort:', ls)

