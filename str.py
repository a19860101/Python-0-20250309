
# a = 'hello "John"'
# a = "hello 'john'"

# 跳脫字元

# a = 'hello \'john\''
# a = "hello \"John\""
# a = 'hello\njohn'
# a = 'hello\tjohn\nhello\tmary'
# a = 'name:\tJohn\nemail:\tasdf@gmail.com'

# a = 'C:\\Users\\B-21\\Desktop\\Python'
# a = r'C:\Users\B-21\Desktop\Python'
# print(a)

# String index
# s = 'helloworld!!'
# print(s[5])
# print(s[2:6])
# print(s[3:])
# print(s[:7])
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4:-1])
# print(s[0:6:2])

# String Method
s = 'helLO world'

# len()
# 計算字串長度
# print(len(s))

# count()
# 計算字串內文字數量
# print(s.count('p'))

# index()
# 取得字串索引值 若找不到會報錯

# find()
# 取得字串索引值 若找不到會回傳-1
# print(s.index('h'))
# print(s.find('h'))

# isalpha()
# 判斷字串是否為英文
# print(s.isalpha())
# isdigit()
# 判斷字串是否為數字
# print(s.isdigit())
# endswith()
# 判斷字串最後一個字母是否為指定字母
# print(s.endswith('o'))
# startswith()
# 判斷字串第一個字母是否為指定字母
# print(s.startswith('H'))


# upper()
print(s.upper())
# lower()
print(s.lower())
# capitalize()
print(s.capitalize())
# title()
print(s.title())


# replace()
s2 = 'hello john !!'
# print(s2.replace('john','Andy'))

# split()
# q = s2.split()
q = s2.split('o')
print(type(s2))
print(q)
print(type(q))

# strip()
s3 = '   hello   '
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())
