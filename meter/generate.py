# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
# Genereren van intervallen met hulp van Kevin van der Toorn 


import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

with open('intervals.txt') as file:
    content = file.readlines()

t = list()
h = list()
for line in content:
    time, height = line.split('-')
    height = int(height)
    time1, time2 = time.split(':')
    time = int(time1) * 60 + int(time2)
    t.append(time)
    h.append(height)


f = interpolate.interp1d(t, h, kind='linear')

t = np.arange(0, t[-1], 1/1000)

y = f(t)

with open('timestamps.js', 'w') as file:
    file.write('var timestamps = [\n')
    for value in y:
        file.write('    ' + str(value) + ',\n')
    file.write('];')

plt.plot(t, y)
plt.show()

