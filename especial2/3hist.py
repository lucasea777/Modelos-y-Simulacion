import numpy as np
import matplotlib.pyplot as plt


np.random.seed(101)
a = np.random.normal(size=1000)
b = np.random.normal(size=1000)
c = np.random.normal(size=1000)

common_params = dict(bins=20, 
                     range=(-5, 5), 
                     normed=True)

#plt.subplot(312)
plt.title('Skinny shift - 3 at a time')
plt.hist((a, b, c), **common_params)


plt.show()