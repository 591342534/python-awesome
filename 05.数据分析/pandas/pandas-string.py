import pandas as pd
import re

a = pd.Series({'robin': 'robin201107@126.com', 'zhanfei': 'zhanfei2018@gmail.com'})
print a.str
b = a.str.contains('gmail')
print type(b)

reg = re.compile('\d+')
c = a.str.findall(reg)
d = a.str.replace(reg, '')
e = a.str.split('@').map(lambda x: ','.join(x))

r = pd.concat([a, b, c, d, e], axis=1)
print r 
