import pandas as pd
import numpy as np

a = pd.DataFrame({
    'a': np.arange(1, 4),
    'b': np.arange(4, 7),
    'c': np.arange(7, 10),
})

b = a.replace([1, 2], [11, 22])
print b 
