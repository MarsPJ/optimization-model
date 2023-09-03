import numpy as np 
import pandas as pd 
df = pd.read_excel('./data.xlsx')
data = df.iloc[:,1].tolist()
data = [set(i.replace('其他','').strip('、').split('、')) for i in data]
result = [len(i & j)  for i in data for j in data]
result = np.array(result).reshape(len(data),-1)
np.savetxt(r'./mydata.csv', result, delimiter=',', fmt="%d")