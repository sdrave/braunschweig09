import matplotlib.pyplot as plt
import numba
import numpy as np
import time


@numba.jit(nopython=True)
def mandelbrot(x, y, N):
    c_x = x
    c_y = y
    x = 0.
    y = 0.
    for n in range(N):
        if x**2 + y**2 > 4:
            return n
        x_new = x*x - y*y + c_x
        y_new = 2*x*y + c_y
        x = x_new
        y = y_new
    return 0


@numba.jit(nopython=True, parallel=True)
def mandelbrot_set(A, left, right, bottom, top, N):
    dx = (right - left) / A.shape[1]
    dy = (top - bottom) / A.shape[0]
    for x_i in numba.prange(A.shape[1]):
        for y_i in range(A.shape[0]):
            A[y_i, x_i] = mandelbrot(left + x_i*dx, bottom + y_i*dy, N)


A = np.zeros((1000, 1000), dtype=np.intc)
mandelbrot_set(A, -2.0, 0.5, -1.25, 1.25, 80)

tic = time.time()
mandelbrot_set(A, -2.0, 0.5, -1.25, 1.25, 80)
print(time.time() - tic)

plt.imshow(A)
plt.show()
