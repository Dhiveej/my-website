import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,1000)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,z,label ='z=cosx')
plt.plot(x,y,label='y=sinx')
plt.title('Graph of sine curve and cosine curve ')
plt.legend()
plt.grid()
plt.show()
