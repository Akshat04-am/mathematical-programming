import numpy as np
def vector_independence(*vectors):

    # check all are numpy arrays
    for vec in vectors:
        if not isinstance(vec, np.ndarray):
            raise TypeError("All inputs must be numpy arrays")

    # check all shapes match
    first_shape = vectors[0].shape

    for vec in vectors:
        if vec.shape != first_shape:
            raise ValueError("Vector shape incompatibility")

    matrix = np.column_stack(vectors)
    determinant = np.linalg.det(matrix)

    if determinant == 0:
        print("Dependent:", determinant)
    else:
        print("Independent:", determinant)

    return matrix










import numpy as np
def vector_independenceplus(*vectors):

    # check all are numpy arrays
    for vec in vectors:
        if not isinstance(vec, np.ndarray):
            raise TypeError("All inputs must be numpy arrays")

    # check shape compatibility
    first_shape = vectors[0].shape

    for vec in vectors:
        if vec.shape != first_shape:
            raise ValueError("Vector shape incompatibility")

    matrix = np.column_stack(vectors)

    rank = np.linalg.matrix_rank(matrix)

    if rank < len(vectors):
        print("Dependent")
    else:
        print("Independent")
    
    return matrix