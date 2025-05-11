import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')
datas = pd.read_csv('../0504/outbound.csv')

# x = ['A','B','C','D','E']
# h = [30,10,40,50,20]
#
# plt.bar(x,h)
#
# plt.show()

# print(datas.head())
# print(datas.columns[1:-1])
# print(datas)

x = datas.columns[2:-1]

# datas.iloc[1][2:-1]取出的資料型態為<class 'pandas.core.series.Series'>所以直接使用會有問題，需要轉成list
h = [int(h) for h in datas.iloc[1][2:-1]]

# h = datas.iloc[1][2:-1]
# print(type(h))
# print(datas.iloc[1][2:-1])

color = ['red', 'skyblue', 'brown', '#ff5847', '#fa0']
# 顏色參考 https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py

tick_label = ['Japan', 'Korea', 'North Korea','Vietnam', 'Thailand']

plt.bar(x,h, color=color, tick_label=tick_label, width=.2)
plt.show()