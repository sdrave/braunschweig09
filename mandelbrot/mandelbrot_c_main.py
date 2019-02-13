import matplotlib.pyplot as plt
import numpy as np
import time
from mandelbrot_c_wrapper import mandelbrot_set_wrapper

A = np.zeros((1000, 1000), dtype=np.intc)
tic = time.time()
mandelbrot_set_wrapper(A, -2.0, 0.5, -1.25, 1.25, 80)
print(time.time() - tic)

plt.imshow(A)
plt.show()
