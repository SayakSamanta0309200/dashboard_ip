import pandas as pd
data = {'product':['computer', 'tablet', 'printer', 'laptop'],'price':[850, 200, 150, 1300]}
df=pd.DataFrame(data)
df.to_csv(r'D:/IP dashboard/export_dataframe.csv', index=False, header=True)
print(df)