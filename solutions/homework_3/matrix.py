import numpy as np
import linalg

A = np.matrix([[-1, 1, 0, 0, 0, 0],
[0, 0, 0, -1, 1, 0],
[-1, 0, 1, 0, 0, 0],
[0, 0, 0, -1, 0, 1],
[1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, -1, 0, 0, 0],
[0, 0, 0, 0, 0, -1],
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0]])

b = np.matrix([4, 4, 4, 4, 4, 1, 1.25, 4, 3, 4, 4.25, 4.25, 4.25, 3.25])

print(linalg.solve(A, b))