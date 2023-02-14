import numpy as np
import pandas as pd

myArr = [['hi', 'hello', 'bye']]

myArr.append(['fart', 'toont', 'poonp'])

pd.DataFrame(myArr).to_csv('test.csv')
print(myArr)