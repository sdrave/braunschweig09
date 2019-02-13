import matplotlib.pyplot as plt
import numpy as np
import time
from mandelbrot_cython import mandelbrot_set

A = np.zeros((1000, 1000), dtype=np.intc)
tic = time.time()
mandelbrot_set(A, -2.0, 0.5, -1.25, 1.25, 80)
print(time.time() - tic)

plt.imshow(A)
plt.show()
