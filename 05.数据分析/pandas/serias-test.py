import pandas as pd

a = pd.Series(['a', 'b', 'c'])
b = pd.Series({'a': 1, 'b': 2, 'c': 3})
print a
print b

a.index = ['a1', 'a2', 'a3']
print a

b['a2'] = 22
b['xxx'] = 55
b.a3 = 33
b.index.name = 'test'
b.name = 'test-name'
print b 
