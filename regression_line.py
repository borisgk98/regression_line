import pylab
from matplotlib import mlab

data = [list(map(int, el.split(';'))) for el in open("data.cvs").readlines()]
n = len(data)
xdata, ydata = [], []
sum1, sum2, sum3, sum4 = 0, 0, 0, 0  # xi, yi, xiyi, xi**2
for el in data:
    sum1 += el[0]
    sum2 += el[1]
    sum3 += el[0] * el[1]
    sum4 += el[0] ** 2
    xdata.append(el[0])
    ydata.append(el[1])
k = (n * sum3 - sum1 * sum2) / (n * sum4 - sum1 ** 2)
b = (sum4 * sum2 - sum1 * sum3) / (n * sum4 - sum1 ** 2)
f = lambda x: k * x + b
sum5, sum6 = 0, 0
for el in data:
    sum5 += (el[1] - sum2 / n) ** 2
    sum6 += (el[1] - f(el[0])) ** 2
r = (1 - sum6 / sum5) ** 0.5
xmin, xmax, step = min(xdata), max(xdata), 0.5
xlist = mlab.frange(xmin, xmax, step)
pylab.scatter(xdata, ydata, color='b')
pylab.plot(xlist, [f(x) for x in xlist], color='r', label=("regression line(r=%.3f)" % r))
pylab.legend()
pylab.show()
