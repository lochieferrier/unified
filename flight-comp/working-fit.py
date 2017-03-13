
from gpfit.fit import fit
from numpy import logspace, log, log10, random
import numpy as np
import matplotlib.pyplot as plt
# fixed initial guess for fitting
# random.seed(33404)

cd0 = 0.020
cd1 = -0.004
cd2 = 0.020
cd8 = 1.0
cl0 = 0.8

cl = np.array(np.linspace(0.1,1.5,100))
cd = cd0 + cd1*(cl-cl0) + cd2*(cl-cl0)**2 + cd8*(cl-cl0)**8

K = 1

x = log(cl)
y = log(cd)

# plt.plot(mdot,delta_p)
# plt.show()
cMA, errorMA = fit(x,y, K, "MA")
cSMA, errorSMA = fit(x, y, K, "SMA")
cISMA, errorISMA = fit(x, y, K, "ISMA")

print "MA RMS Error: %.5g" % errorMA
print "SMA RMS Error: %.5g" % errorSMA
# print "ISMA RMS Error: %.5g" % errorISMA