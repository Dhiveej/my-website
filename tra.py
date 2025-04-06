import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
a=5
rad=np.arange(0,(2*np.pi),0.001)# generates an array of values from 0 to 2pie with a stepsize of 0.001(represents the range of angles
for t in rad:#Loops through each angle t in the rad array.
    r=a-a*np.cos(t)#1st Cardioid
    plt.polar(t,r,'g.')#Plots the first cardioid in green
    s=a+a*np.cos(t)#2nD Cardiod
    plt.polar(t,s,'y.')#plots the first cardioid in yellow
plt.title('Graph of Cardioid')
plt.show()

