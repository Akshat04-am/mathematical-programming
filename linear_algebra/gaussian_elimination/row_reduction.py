import numpy as np
from sympy import Matrix

# Create your NumPy array
np_arr = np.array([[1, 2, -1], [2, 4, 5], [3,3,2]])

# Convert to SymPy Matrix and call rref()
sympy_matrix = Matrix(np_arr)
rref_matrix, pivots = sympy_matrix.rref()

# Convert back to NumPy if needed
rref_np = np.array(rref_matrix).astype(np.float64)

print(rref_np)
