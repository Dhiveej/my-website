import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
a=3
rad=np.arange(0,(2*np.pi),0.001)
for t in rad:
    r=a*np.sin(3*t)
    plt.polar(t,r,'y.')
plt.title('Graph of Three Leaved Rose')
plt.show()