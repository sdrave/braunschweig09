int mandelbrot(double x, double y, int N) {
    double c_x = x;
    double c_y = y;
    x = 0.;
    y = 0.;
    for (int n = 0; n < N; n++){
        if (x*x + y*y > 4) {
            return n;
	}
        double x_new = x*x - y*y + c_x;
        double y_new = 2*x*y + c_y;
        x = x_new;
        y = y_new;
    }
    return 0;
}

void mandelbrot_set(int *A, int A_ny, int A_nx, double left, double right, double bottom, double top, int N) {
    double dx = (right - left) / A_nx;
    double dy = (top - bottom) / A_ny;
    for (int x_i=0; x_i < A_nx; x_i++) {
        for (int y_i=0;  y_i < A_ny; y_i++) {
            A[y_i * A_nx + x_i] = mandelbrot(left + x_i*dx, bottom + y_i*dy, N);
	}
    }
}

