import pandas as pd 
import numpy as np
import datetime

import matplotlib.pyplot as plt

dates = pd.date_range('20190214', periods=6) 
numbers = np.matrix([[ 101, 103], [105.5, 75], [102, 80.3], [100, 85], [110, 98], [109.6, 125.7 ]] ) 
df = pd.DataFrame(numbers, index=dates, columns=['A','B'])

print('Pandas DataFrame')
print('============================================')
print('')

print('1 užduotis')
print('===========')
df1 = df.loc['2019-02-18']
print(df1)
print('')
print('====================================')

print('2 užduotis')
print('===========')
df2 = df.loc[datetime.datetime(2019,2,18)]
print(df2)
print('')
print('====================================')

print('3 užduotis')
print('===========')
df3 = df.iloc[-2]
print(df3)
print('')
print('====================================')

print('4 užduotis')
print('===========')
df4 = df.head(2)['B']
print(df4)
print('')
print('====================================')

print('5 užduotis')
print('===========')
df5 = df.sort_values(by = 'B', ascending = False)
print(df5)
print('')
print('====================================')

print('6 užduotis')
print('===========')
df6 = df['A'].max()
print(df6)
print('')
print('====================================')

print('7 užduotis')
print('===========')
df.loc[df['A'].idxmax(), 'A'] *= 2
print(df)
print('')
print('====================================')

print('8 užduotis')
print('===========')
df8 = df[df.A > 105]
print(df8)
print('')
print('====================================')

print('9 užduotis')
print('===========')
df.index = df.index.strftime('%Y-%m-%d')
df9 = df.plot(kind = 'line', y = 'A', figsize = (10, 6), legend = False, rot = 45)
plt.show()
print('Žiūrėti diagramą')
print('')
print('====================================')

print('10 užduotis')
print('===========')
df10 = df.drop(df[df['B'] > df['A']].index)
print(df10)
print('')
print('====================================')



print('NumPy')
print('============================================')
print('')

print('1 užduotis')
print('===========')
a = np.random.randn(1, 10)
b = np.random.randn(1, 10)
c = np.sum(a + b)
print(c)
print('')
print('====================================')

print('2 užduotis')
print('===========')
a = np.random.randn(1, 10)
a = np.where(a > 0, 0, a)
print(a)
print('')
print('====================================')

print('3 užduotis')
print('===========')
a = np.random.randint(1, 11, size = 10)
print(a)
lt6 = np.less(a, 6)
print(a[lt6])
print('')
print('====================================')

print('4 užduotis')
print('===========')
a = np.random.randint(1, 6, size=10)
b = np.arange(len(a))
eq = np.equal(a[b], a[b-1])
print(a)
print(b)
print(eq)
print("Sutampančių skaičių indeksai: ", b[eq])
print("Sutampantys skaičiai: ", a[eq])
print('')
print('====================================')

print('5 užduotis')
print('===========')
a = np.random.randint(1, 10, size = 10)
b = np.random.randint(1, 10, size = 10)
print(a)
print(b)
gtb = np.greater(a, b)
print(a[gtb])
print('')
print('====================================')

print('6 užduotis')
print('===========')
a = np.random.randint(1, 11, size = 10)
print(a)
idx = np.arange(len(a))
idx[:-1] = idx[1:]
a = a[idx]
print(a)
print('')
print('====================================')

print('7 užduotis')
print('===========')
a = np.random.randint(1, 11, size = 10)
print(a)
idx = np.arange(len(a))
mirror_idx = np.flip(idx)
a[idx] = a[mirror_idx]
print(a)
print('')
print('====================================')

print('8 užduotis')
print('===========')
a = np.random.randint(1, 11, size = 10)
print(a)
idx = np.arange(len(a))
a = np.where(idx%2 == 1, 0, a)
print(a)
print('')
print('====================================')

print('9 užduotis')
print('===========')
a = np.random.randn(10, 20)
avg = np.mean(a, axis = 1)
print(avg)
print('')
print('====================================')

print('10 užduotis')
print('===========')
a = np.random.randint(1, 11, size = (10, 10))
print(a)
rows = a.shape[0]
columns = a.shape[1]
vert_row = np.arange(rows)
hor_col = np.arange(columns)
print(a[vert_row, hor_col])
print('')
print('====================================')
