menu = [
    {
        'id':1,
        'name':'滷肉飯',
        'price':50,
    }, {
        'id':2,
        'name':'牛肉麵',
        'price':120,
    }, {
        'id':3,
        'name':'貢丸湯',
        'price':40,
    },

]

cart = []
total = 0
for data in menu:
    print(data['name'],data['price'])
while True:
    selected = input('請選擇項目(按q完成):')
    if selected == 'q':
        break
    elif menu[int(selected)-1].get('name') is not None:
        cart.append(menu[int(selected)-1])

    # else:
    #     print(menu[int(selected)-1])
# print(cart)

print('您購買了:\n')
for data in cart:
    # print(data['price'])
    total += data['price']
    print(data['name'],end="\n")
print()
print(f'共${total}元')