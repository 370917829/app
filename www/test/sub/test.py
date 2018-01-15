import numpy as np, pandas as pd

arr1 = np.arange(10)
print(arr1)
type(arr1)
s1 = pd.Series(arr1)
print(s1)
type(s1)


dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},
'two':{'a':5,'b':6,'c':7,'d':8},
'three':{'a':9,'b':10,'c':11,'d':12}}
print(dic3)
type(dic3)
df3 = pd.DataFrame(dic3)
print(df3)
type(df3)

