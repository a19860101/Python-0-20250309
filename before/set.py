"""
Set 集合
集合是一種無序且不可重複的資料結構，資料不支援索引也不可修改。
集合資料的內容可以是字串、數值、Tuple等，但不可以是串列List（可變）。
"""
s1 = {1,2,3,'台北市'}
s2 = set()
l1 = ['台北市','台北市','桃園市','桃園市','桃園市','桃園市','桃園市','新竹市','新竹市','台中市']
city = set(l1)
# city = list(city)
# city = tuple(city)
# print(city)


# s1.add(4)
# s1.remove(5)
# s1.discard(5)
# city.pop()
# s1.update(city)

# s1.clear()

# print(s1)

se1 = {1,2,3,4,5}
se2 = {4,5,6,7,8}

# result = se1.union(se2)
# result = se1 | se2

# result = se1.intersection(se2)
# result = se1 & se2

# result = se1.difference(se2)
# result = se1 - se2

# result = se2.difference(se1)
# result = se2 - se1

# result = se1.symmetric_difference(se2)
result = se1 ^ se2

# print(result)
print(6 in se1)
print(6 in se2)
s1 = {1,2,3,4,5}
print(6 in s1)
print(3 in s1)