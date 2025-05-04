import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')
datas = pd.read_csv('outbound.csv')


labels = datas.columns[2:-1]


data = datas.iloc[1][2:-1]
print(data)

plt.pie(
    data,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    textprops={'size':10, 'weight':'bold'},
    autopct='%.1f%%'
)
plt.legend()
plt.show()

