menu = {
    'apple': 10,
    'banana': 100,
    'kiwi': 60
}

cart = []
total = 0
print('----Menu----')
for k,v in menu.items():
    print(f'{k:8}:{v:5}')
print('------------')

while True:
    selected = input('請輸入品項(按q/Q完成輸入)').lower()
    if selected == 'q':
        break
    elif menu.get(selected) is not None:
        cart.append(selected)
print('訂單內容')
for p in cart:
    print(p, end='\n')
    # print(menu.get(p))
    # total = total + menu.get(p)
    total += menu.get(p)
print()
print(f'您共花費了${total}元')