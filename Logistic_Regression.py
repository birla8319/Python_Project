#Logistic Regression
#Experiment 3
import numpy as np
height = np.array([142,162,180,170,120,110,200,90,155]) 
label = np.array([1,0,1,1,0,0,0,1,1])

#male = 1
#female = 0

#for i in range()

heightmean = np.mean(height)
print(heightmean)

labelmean = np.mean(label)
print(labelmean)


slope1 = np.sum((height-heightmean)*(label-labelmean))
slope2 = np.sum((height-heightmean)*(height-heightmean))
b1 = slope1/slope2
print("B1 is",b1)


b0 = labelmean- b1*heightmean
print("B0 is",b0)

ynew =[]
sigmoidnew = []

for i in range(len(height)):
    y = b0+b1*height[i]
    ynew.append(y)
    sigmoid = np.exp(-y)
    sigmoidd = (1/(1+sigmoid))
    sigmoidnew.append(sigmoidd)
    #print(ynew)
print("y is",ynew)
print("Sigmoid is",sigmoidnew)

threshold = 0.5

for i in range(len(sigmoidnew)):
    if(sigmoidnew[i]<=0.2):
        print("class_0")
    else:
        print("class_1")
