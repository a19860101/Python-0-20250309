# Set 集合
集合是一種無序且不可重複的資料結構，資料不支援索引也不可修改。
集合資料的內容可以是字串、數值、Tuple等，但不可以是串列List（可變）。

## 集合操作
### 建立集合
```python
s1 = {98,92,85,72}
print(s1)
# {72, 98, 92, 85}

```
但要建立空集合時則要用```set()```建立，否則會視為字典dict

```python
s1 = {}
s2 = set()
print(type(s1)) # <class 'dict'>
print(type(s2)) # <class 'set'>
```
### 新增資料
```python
fruits = {'apple','banana','kiwi'}
fruits.add('coconut')
print(fruits)
# {'banana', 'coconut', 'apple', 'kiwi'}
# 因為無序，所以呈現的資料位置會隨機變化
```
### 移除資料
```python
fruits = {'apple','banana','kiwi'}
fruits.remove('kiwi')
print(fruits)
# {'banana', 'apple'}

fruits = {'apple','banana','kiwi'}
fruits.discard('apple')
print(fruits)
# {'banana', 'kiwi'}

# 隨機刪除
fruits = {'apple','banana','kiwi'}
fruits.pop()
print(fruits)
# {'banana', 'kiwi'}

# 數字集合
ss = {2,5,1,6,8}
ss.pop()
print(ss)
# {2, 5, 6, 8}
# 若為數字集合，則pop都會刪除第一筆資料
```
> remove與discard都是刪除，差別在於remove時若項目不存在會報錯；discard則不會報錯
### 清除資料
```python
fruits = {'apple','banana','kiwi'}
fruits.clear()
print(fruits)
# set()
```

### 數學運算
```python
se1 = {1,2,3,4,5}
se2 = {4,5,6,7,8}

# 聯集
# result_union = se1.union(se2)
result_union = se1 | se2
print(result_union)
# {1, 2, 3, 4, 5, 6, 7, 8}

# 交集
# result_intersection = se1.intersection(se2)
result_intersection = se1 & se2
print(result_intersection)
# {4, 5}

# 差集
# result_difference_a = se1.difference(se2)
result_difference_a = se1 - se2
print(result_difference_a)
# {1, 2, 3}

# result_difference_b = se2.difference(se1)
result_difference_b = se2 - se1
print(result_difference_b)
# {8, 6, 7}

# 對稱差集
# result_symmetric_difference = se1.symmetric_difference(se2)
result_symmetric_difference = se1 ^ se2
print(result_symmetric_difference)
# {1, 2, 3, 6, 7, 8}

```

### 判斷資料是否存在
```python
s1 = {1,2,3,4,5}
print(6 in s1)
# False
print(3 in s1)
# True
```