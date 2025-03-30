"""
Tuple 元組
Tuple類似List，但資料順序、個數、內容皆不可改變 基本上可以當作不可變動的List
"""
t1 = tuple()

t2 = (1,2,3,4,5)
# print(type(t2))
# print(t2[3])

# t3 = 1,2,3,4,5

t4 = True, 'Hello', 123, 0.2

# t5 = t2 + t4

# t4 = t4 + ('apple',)
t4 = list(t4)
t4.append('Apple')
t4 = tuple(t4)
# print(t4)

# print(len(t4))
# print(t4.count(True))
# print(t4.index(123))

t6 = ('apple',)
# print(type(t6))


print(1 in t2)