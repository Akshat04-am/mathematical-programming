import numpy as np

def vector_independence(*vectors):
    """
    Returns True if vectors (columns) are linearly independent.
    Uses matrix rank to bypass floating-point determinant issues.
    Also returns matrix output
    """

    # Check all are numpy arrays
    for vec in vectors:
        if not isinstance(vec, np.ndarray):
            raise TypeError("All inputs must be numpy arrays")

    # Check shape compatibility
    first_shape = vectors[0].shape
    for vec in vectors:
        if vec.shape != first_shape:
            raise ValueError("Vector shape incompatibility")

    matrix = np.column_stack(vectors)
    
    # Single rank calculation
    rank = np.linalg.matrix_rank(matrix)
    is_independent = (rank == matrix.shape[1])
    
    if is_independent:
        print("Independent")
    else:
        print("Dependent")
    
    return matrix

