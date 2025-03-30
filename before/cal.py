import math

x = 3.6
y = -34
# print(pow(y,5))
# print(pow(2,3))
# print(round(x))
# print(abs(y))
# print(max(2,3,1))
# print(min(2,8,-23))

# print(math.sqrt(36))
# print(math.floor(x))
# print(math.ceil(x))

# print(math.pi)
# print(math.e)

# 運算子 operator
a = 10
b = 6
## 數學 +, -, *, /, %
# print(a + b) #16
# print(a - b) #4
# print(a * b) #60
# print(a / b) #1.67
# print(a % b) # 4

## 比較 ==, !=, >, >=, <, <=
print(a <= 0)

## 指定 =, +=, -=, *=, /=, %=
# print(a + b)
# print(a)
# a += b
# a = a + b
# print(a)

## 邏輯 and, or, not
v = ''
print(not v)

# 圓周 2*pi*r

# r = float(input('請輸入半徑'))
# result = 2 * math.pi * r
# print('周長為',result)

# 圓面積
r = float(input('請輸入半徑'))
result = math.pi * pow(r,2)
result = round(result,2)
print('圓面積為:',result)



