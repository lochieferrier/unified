from gpfit.fit import fit
from numpy import logspace, log, log10, random
from matplotlib import pyplot as plt
# fixed initial guess for fitting
random.seed(33404)

cd0 = 0.020
cd1 = -0.004
cd2 = 0.020
cd8 = 1.0
cl0 = 0.8
# cd = 0.02 -0.004*(cl-0.8) + 0.02*(cl-0.8)**2 + (cl-0.8)**2
cl = logspace(log10(0.8), log10(2.5), 101)
cd = 0.02 -0.004*(cl-0.8) + 0.02*(cl-0.8)**2 + (cl-0.8)**8
# cd = (cl-1)**2 + cl**3
x = log(cl)
y = log(cd)
K = 3

cMA, errorMA = fit(x, y, K, "MA")
cSMA, errorSMA = fit(x, y, K, "SMA")
# cISMA, errorISMA = fit(x, y, K, "ISMA")

print "MA RMS Error: %.5g" % errorMA
print "SMA RMS Error: %.5g" % errorSMA
# print "ISMA RMS Error: %.5g" % errorISMA