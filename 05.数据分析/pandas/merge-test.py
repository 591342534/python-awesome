import pandas as pd

a1 = pd.DataFrame({
    'code': [1, 2, 3],
    'price': [3.4, 5.6, 90]
})

a2 = pd.DataFrame({
    'code': [2, 3, 4],
    'news': ['aa', 'bb', 'cc']
})

b = pd.merge(a1, a2)
print b

c = pd.merge(a1, a2, how='left')
print c


a3 = pd.DataFrame({
    'code1': [1, 2, 3],
    'price': [3.4, 5.6, 90]
})

a4 = pd.DataFrame({
    'code2': [2, 3, 4],
    'news': ['aa', 'bb', 'cc']
})

d = pd.merge(a3, a4, left_on='code1', right_on='code2')
print d

e = a3.join(a4, how='outer', on='code1')
print e 
