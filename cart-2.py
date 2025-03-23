menu = [
    {
        'id':1,
        'name':'1.滷肉飯',
        'price':50,
    },
    {
        'id':2,
        'name':'2.牛肉麵',
        'price':120,
    },
    {
        'id':3,
        'name':'3.貢丸湯',
        'price':40,
    },
]
cart = []
total = 0
print('----Menu----')
for item in menu:
    print(f'{item['name']}: {item['price']}')
print('------------')

while True:
    selected = input('請輸入品項編號(按q/Q完成輸入)').lower()
    if selected == 'q':
        break
    elif
