from gpfit.fit import fit
from numpy import logspace, log, log10, random
from matplotlib import pyplot as plt
# fixed initial guess for fitting
random.seed(33404)

cl = logspace(0, log10(3), 101)
cd = (cl**2)
x = log(cl)
y = log(cd)
K = 3

cMA, errorMA = fit(x, y, K, "MA")
# cSMA, errorSMA = fit(x, y, K, "SMA")
# cISMA, errorISMA = fit(x, y, K, "ISMA")

print "MA RMS Error: %.5g" % errorMA
# print "SMA RMS Error: %.5g" % errorSMA
# print "ISMA RMS Error: %.5g" % errorISMA