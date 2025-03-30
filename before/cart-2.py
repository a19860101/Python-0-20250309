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
    elif int(selected) > len(menu):
        print('請選擇正確的品項編號')
        continue
    elif menu[int(selected) - 1] in menu:
        cart.append(menu[int(selected) - 1])

print('您購買了:\n')
for item in cart:
    itemName = item['name'][2:]
    print(f'{itemName:10}:${item['price']}元')
    total += item['price']

print('----------------------------------------------')
print(f'共${total}元')