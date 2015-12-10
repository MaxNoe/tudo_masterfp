import matplotlib.style
matplotlib.style.use('../matplotlibrc')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.cosh(x)/ np.sinh(x) -  1/x

plt.plot(x, y, label=r'Langevin Funktion $ L(x) = \coth(x) - \frac{1}{x}$', color="#19d73d")
plt.xlabel(r'$x$')
plt.ylabel(r'$ L(x)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/langevin.pdf')