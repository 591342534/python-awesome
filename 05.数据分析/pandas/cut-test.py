import pandas as pd
import numpy as np

a = np.random.randint(1, 100, 10)
print a

b = pd.cut(a, [0, 20, 60, 80, 100], labels=['a', 'b', 'c', 'd'])
print b
print pd.value_counts(b)

c = pd.qcut(a, 5)
print c
print pd.value_counts(c) 
