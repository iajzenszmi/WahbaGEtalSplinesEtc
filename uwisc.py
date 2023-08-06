import numpy as np

def rq(x, y, n):
  # Compute the mean and standard deviation of the x-coordinates.
  mu = np.mean(x)
  sigma = np.std(x)

  # Compute the weights.
  w = np.ones(n)
  for i in range(n):
    for j in range(n):
      if i != j:
        w[i] += (x[i] - x[j]) ** 2

  # Compute the coefficients of the robust quadratic fit.
  b = np.zeros(2)
  b[0] = np.sum(w * (y - mu) * (x - mu)) / np.sum(w * (x - mu) ** 2)
  b[1] = np.sum(w * (y - mu) - b[0] * (x - mu)) / np.sum(w)

  return b

if __name__ == "__main__":
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 4, 6, 8, 10])
  n = len(x)
  b = rq(x, y, n)
  print("b = ", b)

