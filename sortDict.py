z = {'a':3, 'd':5, 'b':1, 'c':2}

#Sort using Sorted Function
# print(sorted(z))
# print(sorted(z.values()))
# print(sorted(z.items()))

# #Sort using collections
# from collections import OrderedDict
# print(OrderedDict(sorted(z.items())))

#Sort by Key without using any in built-in functions
# def insertionSort(kList):
#
#     for i in range(1, len(kList)):
#         temp = kList[i]
#         j = i - 1
#
#         while j >=0 and kList[j] > temp:
#             kList[j+1] = kList[j]
#             j -= 1
#         kList[j+1] = temp
#     return kList
#
# print('Before Sorting:', z)
# sortedKeys = insertionSort(list(z.keys()))
# tempDict = {}
# for x in sortedKeys:
#     tempDict[x] = z[x]
# print('After Sorting:', tempDict)



# #Sort by Value without using built-in functions
#
# def insertionSort(ls):
#     for x in range(1, len(ls)):
#         temp = ls[x]
#         j = x-1
#
#         while j >= 0 and ls[j][1] > temp[1]:
#             ls[j+1] = ls[j]
#             j -= 1
#         ls[j+1] = temp
#
#     return ls
# print('Before Sorting', z)
# z = insertionSort(list(z.items()))
# print('After Sorting', dict(z))


#Sort using lambda fuction
print(sorted(z.items(), key=lambda x:x[1]))



