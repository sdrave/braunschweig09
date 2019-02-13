#cython: language_level=3

import cython
from cython.parallel import prange

cdef int mandelbrot(double x, double y, int N) nogil:
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


@cython.boundscheck(False)
@cython.wraparound(False)
def mandelbrot_set(int [:, ::1] A, double left, double right, double bottom, double top, int N):
    cdef int x_i, y_i
    dx = (right - left) / A.shape[1]
    dy = (top - bottom) / A.shape[0]
    for x_i in prange(A.shape[1], schedule='dynamic', nogil=True):
        for y_i in range(A.shape[0]):
            A[y_i, x_i] = mandelbrot(left + x_i*dx, bottom + y_i*dy, N)
