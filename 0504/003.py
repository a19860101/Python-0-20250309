import pandas as pd

datas = pd.read_csv('Restaurant_C_f.csv')

print(datas.columns)
# print(datas['Name'])
# print(datas['Add'])

condition = datas['Add'].str.contains('中壢')
# result = result[['Name','Add','Tel']]
result = datas[condition]
result = result.drop(['Id','Px','Py'], axis=1)
#
# print(result['Name'])
result.to_excel('chungli.xlsx')


# datas = pd.read_csv('COA_OpenData.csv')
# # print(datas.columns)
# print(datas['animal_kind'])
# condition = datas['animal_kind'].str.contains('貓')
# result = datas[condition]
# print(result['animal_Variety'])