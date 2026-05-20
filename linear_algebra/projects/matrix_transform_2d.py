import numpy as np
import matplotlib.pyplot as plt

def matrix_transform_2d(vector, matrix):


    # checks if input is in array formq
    if not isinstance(vector, np.ndarray) or not isinstance(matrix, np.ndarray):
        raise TypeError("Both inputs must be numpy arrays")

    # enforce 2D vector and 2x2 matrix
    if vector.shape != (2,1):
        raise ValueError("Vector must have shape (2,1)")

    if matrix.shape != (2,2):
        raise ValueError("Matrix must have shape (2,2)")



    # start fresh figure
    plt.figure()



    # matrix transformation
    transformed = matrix @ vector

    # unpack coordinates
    vx, vy = vector.ravel()
    tx, ty = transformed.ravel()

    # dynamic axis scaling
    axis_limit = np.array([vx, vy, tx, ty])
    limit = np.max(np.abs(axis_limit)) + 1



    # original vector
    plt.quiver(
        0, 0,
        vx, vy,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='blue',
        label='Original Vector'
    )

    # transformed vector
    plt.quiver(
        0, 0,
        tx, ty,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='red',
        label='Transformed Vector'
    )
    


    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.gca().set_aspect('equal')
    plt.grid()
    plt.legend()
    plt.show()










import numpy as np
import matplotlib.pyplot as plt


def matrix_transform_2dplus (vector, matrix):

    # ----------------------------
    # Input validation
    # ----------------------------
    if not isinstance(vector, np.ndarray):
        raise TypeError("vector must be a numpy array")

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy array")

    if vector.shape != (2, 1):
        raise ValueError("vector must have shape (2,1)")

    if matrix.shape != (2, 2):
        raise ValueError("matrix must have shape (2,2)")

    # ----------------------------
    # Transformation
    # ----------------------------
    transformed = matrix @ vector

    # unpack vectors
    vx, vy = vector.ravel()
    tx, ty = transformed.ravel()

    # ----------------------------
    # Transform basis vectors
    # ----------------------------
    i_hat = np.array([[1],
                      [0]])

    j_hat = np.array([[0],
                      [1]])

    transformed_i = matrix @ i_hat
    transformed_j = matrix @ j_hat

    ix, iy = transformed_i.ravel()
    jx, jy = transformed_j.ravel()

    # ----------------------------
    # Dynamic scaling
    # ----------------------------
    axis_values = np.array([
        vx, vy,
        tx, ty,
        ix, iy,
        jx, jy
    ])

    limit = np.max(np.abs(axis_values)) + 1

    plt.figure(figsize=(8, 8))

    # ----------------------------
    # Original vector
    # ----------------------------
    plt.quiver(
        0, 0,
        vx, vy,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='blue',
        label='Original Vector'
    )

    # ----------------------------
    # Transformed vector
    # ----------------------------
    plt.quiver(
        0, 0,
        tx, ty,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='red',
        label='Transformed Vector'
    )

    # ----------------------------
    # Transformed basis vectors
    # ----------------------------
    plt.quiver(
        0, 0,
        ix, iy,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='green',
        label='Transformed î'
    )

    plt.quiver(
        0, 0,
        jx, jy,
        angles='xy',
        scale_units='xy',
        scale=1,
        color='purple',
        label='Transformed ĵ'
    )

    # ----------------------------
    # Axes and grid
    # ----------------------------
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.gca().set_aspect('equal')

    plt.grid()

    # ----------------------------
    # Labels
    # ----------------------------
    plt.title("2D Matrix Transformation")

    plt.legend()

    plt.show()
