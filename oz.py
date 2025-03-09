# 1oz = 29.573ml

x = input('請輸入轉換的數字')
s = input('單位是oz還是ml?(o/m)')

if s=='o':
    result = float(x) * 29.573
    result = round(result,2)
    print(f'您的換算結果為{x}oz約{result}ml')
else:
    result = float(x) / 29.573
    result = round(result,2)
    print(f'您的換算結果為{x}ml約{result}oz')
