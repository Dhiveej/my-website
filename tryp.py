import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')#sets up polar projection
a=2
rad=np.arange(0,(2*np.pi),0.001)#creates an array of values from 0 to 2pie with a stepsize of 0.001
for t in rad:#iterates through the array of  values (angles)
    r=np.sqrt(a*a*np.cos(2*t))#calculates the r value for each point
    plt.polar(t,r,'g.')#plots the graph for each angle
plt.title("Lemniscate of Bernoulli")
plt.show()