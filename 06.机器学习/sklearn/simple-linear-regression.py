# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics

x = pd.DataFrame([1.5,2.8,4.5,7.5,10.5,13.5,15.1,16.5,19.5,22.5,24.5,26.5])
y = pd.DataFrame([7.0,5.5,4.6,3.6,2.9,2.7,2.5,2.4,2.2,2.1,1.9,1.8])

linreg = LinearRegression()
linreg.fit(x, y)

y_pred = linreg.predict(x)
print y_pred

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x, y_pred)

print metrics.mean_squared_error(y, y_pred)

plt.show() 
