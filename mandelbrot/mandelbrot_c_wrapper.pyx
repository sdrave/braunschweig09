# cython: language_level=3
# distutils: sources = mandelbrot_c.c

from cython cimport view

cdef extern from "mandelbrot_c.h":
    int mandelbrot(double x, double y, int N);
    void mandelbrot_set(int *A, int A_ny, int A_nx, double left, double right, double bottom, double top, int N);

def mandelbrot_wrapper(x, y, N):
    return mandelbrot(x, y, N)

def mandelbrot_set_wrapper(int [:,::view.contiguous] A, left, right, bottom, top, N):
    mandelbrot_set(&A[0,0], A.shape[0], A.shape[1], left, right, bottom, top, N)
