"""
List串列
List其實就很像是其他程式語言裡面的陣列。 是一種值可變、可重複、存放有順序性、有索引值且無上限的資料結構。
"""
# l1 = []
# l1 = list()

# l1 = ['apple','banana','cat']
# l1 = list(['apple','banana','cat'])
l1 = ['apple',123,0.98,True,True,123,'hello']

# print(l1[0::2])
# for 迴圈
# for data in l1:
    # print(data)

# len()
# print(len(l1))
# count()
# print(l1.count(123))
# index()
# print(l1.index(True))

# append()
# l1.append(['python','mysql'])
# extend()
# l1.extend('python')
# print(l1)

# insert()
# print(l1)
# l1.insert(2,'python')

# remove()
# l1.remove(123)
# l1.remove(123)

# pop()
# l1.pop(3)
# print(l1)

# clear()
# l1.clear()
# print(l1)

# sort()
l2 = [1,6,2,8,4]
l3 = ['2','5','1','3']
l4 = [1.2,9,5.2]
# l4.sort()
# print(l4)

# reverse()
# l2.sort(reverse=True)
# l2.reverse()
# print(l2)

# copy()
# c1 = [1,2,3,4]
# c2 = c1.copy()
# c3 = c1
# c1[0] = 'A'
# c2[0] = 'A'

import copy
c1 = [1,2,[3,4]]
# c2 = c1.copy()
c2 = copy.deepcopy(c1)
c3 = c1
c1[0] = 'Q'
c1[2][0] = 'A'

print(c1)
print(c2)
print(c3)

# 淺拷貝 深拷貝