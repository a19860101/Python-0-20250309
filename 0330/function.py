def foo():
    x = 100
    y = 1.2
    result = x * y
    # print(result)
#
def area(w,h):
    # print(w * h)
    return w * h

result = area(100,2)

# Default Arguments

def jp_to_tw( dollar,rate=0.22):
    return dollar * rate

# print(jp_to_tw(10000))

# s = int(input('請輸入秒數:'))

import time
def count(end,start=0):
    for x in range(end, start, -1):
        print(x)
        time.sleep(1)
    print('完成')

# count(s)

# for i in range(5,0,-1):
#     print(i)


def greeting(first, last):
    print(f'Hello , {first} {last}')

# greeting('Max','Lee')
# greeting(last='Chen',first='Mary')