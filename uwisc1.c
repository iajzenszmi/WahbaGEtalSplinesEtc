#include <stdio.h>
#include <math.h>

void rq(double *x, double *y, int n, double *b) {
  // Compute the mean and standard deviation of the x-coordinates.
  double mu = 0.0;
  for (int i = 0; i < n; i++) {
    mu += x[i];
  }
  mu /= n;
  double sigma = 0.0;
  for (int i = 0; i < n; i++) {
    sigma += (x[i] - mu) * (x[i] - mu);
  }
  sigma = sqrt(sigma / n);

  // Compute the weights.
  double w[n];
  for (int i = 0; i < n; i++) {
    w[i] = 1.0;
    for (int j = 0; j < n; j++) {
      if (i != j) {
        w[i] += (x[i] - x[j]) * (x[i] - x[j]);
      }
    }
  }

  // Compute the coefficients of the robust quadratic fit.
  b[0] = sum(w * (y - mu) * (x - mu)) / sum(w * (x - mu) * (x - mu));
  b[1] = sum(w * (y - mu) - b[0] * (x - mu)) / sum(w);
}

int main() {
  double x[] = {1, 2, 3, 4, 5};
  double y[] = {2, 4, 6, 8, 10};
  int n = sizeof(x) / sizeof(x[0]);
  double b[2];
  rq(x, y, n, b);
  printf("b = %f %f\n", b[0], b[1]);
  return 0;
}

