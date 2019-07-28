
#Linear Regression
#Experiment 1

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as plt
x = np.array([1,2,4,3,5])
y = np.array([1,3,3,2,5])

a = [1,2,3,4,5]
b = [7,8,8,9,4]

xmean = np.mean(x)
print(xmean)

ymean = np.mean(y)
print(ymean)


slope1 = np.sum((x-xmean)*(y-ymean))
slope2 = np.sum((x-xmean)*(x-xmean))
b1 = slope1/slope2
print(b1)


b0 = ymean- b1*xmean
print("B0 is",b0)

y1 = b0+b1*x[0]
y2 = b0+b1*x[1]
y3 = b0+b1*x[2]
y4 = b0+b1*x[3]
y5 = b0+b1*x[4]

ypredict = np.array([y1,y2,y3,y4,y5])
print("ypredict is",ypredict)

error = np.mean((ypredict-y)*(ypredict-y))
print(error)

#errormean = np.mean(error)
#print(errormean)

errorsqrt = np.sqrt(error)
print(errorsqrt)

plt.scatter(x,y)
plt.scatter(x,ypredict)

plt.show()
