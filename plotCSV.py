import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('data.tsv',delimiter=';', dtype = float)

a = [row[0] for row in data]
b = [row[1] for row in data]
c = [row[2] for row in data]

fig = plt.figure()
ax = fig.add_subplot(111, axisbg = 'w')
ax.plot(a,b,'g',lw=1.3)
ax.plot(a,c,'r',lw=1.3)
plt.show()
