import pandas as pd

# datas = pd.read_csv('Restaurant_C_f.csv')

# print(datas.columns)
# print(datas['Name'])
# print(datas['Add'])

# condition = datas['Add'].str.contains('中壢')
# result = datas[condition]
#
# print(result['Name'])

datas = pd.read_csv('COA_OpenData.csv')
# print(datas.columns)
print(datas['animal_kind'])
condition = datas['animal_kind'].str.contains('貓')
result = datas[condition]
print(result['animal_Variety'])