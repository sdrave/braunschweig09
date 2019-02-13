#!/bin/sh
CFLAGS="-fopenmp" cythonize -a -i mandelbrot_cython.pyx
cythonize  -i -a  mandelbrot_c_wrapper.pyx
