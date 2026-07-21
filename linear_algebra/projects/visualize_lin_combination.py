
import numpy as np
import matplotlib.pyplot as plt

def example():
    # basis/transformation columns
    x = np.array([[1],
                  [2]])

    y = np.array([[3],
                  [2]])

    # transformation matrix
    matrix = np.column_stack((x, y))

    det = np.linalg.det(matrix)

    print("Matrix:\n", matrix)
    print("Determinant:", det)

    # input vector
    vector = np.array([[1],
                       [5]])

    # individual column contributions
    part_1 = vector[0,0] * matrix[:,0]
    part_2 = vector[1,0] * matrix[:,1]

    # final transformed vector
    result = part_1 + part_2

    # original vector
    plt.quiver(
        0, 0,
        vector[0,0], vector[1,0],
        angles='xy',
        scale_units='xy',
        scale=1,
        label="original vector"
    )

    # first column contribution
    plt.quiver(
        0, 0,
        part_1[0], part_1[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color="red",
        label="column 1 contribution"
    )

    # second column contribution
    plt.quiver(
        0, 0,
        part_2[0], part_2[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color="yellow",
        label="column 2 contribution"
    )

    # final transformed vector
    plt.quiver(
        0, 0,
        result[0], result[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color="green",
        label="final transformed vector"
    )

    plt.xlim(0,20)
    plt.ylim(0, 20)

    plt.axhline(0, color='red')
    plt.axvline(0, color='red')

    plt.grid()
    plt.legend()
    plt.show()











# ========================================================================
import numpy as np
import matplotlib.pyplot as plt

def visualize_linear_combination(vector, matrix):
    """Visualizing how each matrix column contributes
    to the final transformed vector."""

    # Validation
    if not isinstance(vector, np.ndarray) or not isinstance(matrix, np.ndarray):
        raise TypeError("Both inputs must be numpy arrays")

    if vector.ndim == 1:
        vector = vector.reshape(2, 1)

    if vector.shape != (2, 1):
        raise ValueError("Vector must have shape (2,1)")

    if matrix.shape != (2, 2):
        raise ValueError("Matrix must have shape (2,2)")

    # Unpack vector components
    v1 = vector[0, 0]
    v2 = vector[1, 0]

    # Calculate column contributions
    part_1 = v1 * matrix[:, 0]
    part_2 = v2 * matrix[:, 1]
    
    # Final transformed vector
    result = part_1 + part_2

    plt.figure()

    # Original vector
    plt.quiver(
        0, 0, v1, v2,
        angles='xy', scale_units='xy', scale=1,
        color='blue', alpha=0.3, label='Original Vector'
    )

    # First column contribution
    plt.quiver(
        0, 0, part_1[0], part_1[1],
        angles='xy', scale_units='xy', scale=1,
        color='red', label='Col 1 Contrib'
    )

    # Second column contribution (Tip-to-Tail)
    plt.quiver(
        part_1[0], part_1[1], part_2[0], part_2[1],
        angles='xy', scale_units='xy', scale=1,
        color='orange', label='Col 2 Contrib (Tip-to-Tail)'
    )

    # Final transformed vector
    plt.quiver(
        0, 0, result[0], result[1],
        angles='xy', scale_units='xy', scale=1,
        color='green', label='Final Transformed Vector'
    )

    # Dynamic limits calculation (no list comprehensions)
    x_coords = np.array([0, v1, part_1[0], result[0]])
    y_coords = np.array([0, v2, part_1[1], result[1]])
    
    all_coords = np.concatenate((np.abs(x_coords), np.abs(y_coords)))
    limit = np.max(all_coords) * 1.2

    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.gca().set_aspect('equal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()
