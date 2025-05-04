import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

datas = [23,66,88]
labels = ['國中','高中','大專院校']
total = sum(datas)
# labels = [ str(100 * d / total) for d in datas]

# plt.pie([10,20,30])
plt.pie(
    datas,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    textprops={'size':10, 'weight':'bold'},
    autopct='%.1f%%'
)

plt.legend()


plt.show()


# data = [30, 70, 120]
# total = sum(data)
#
#
# data_2 = [ str(round(100 * d / total)) + '%' for d in data]
# print(data_2)


