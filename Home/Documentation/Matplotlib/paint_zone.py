import matplotlib.pyplot as plt
import numpy as np

def plot_math_zones(x_range, offsets, colors):
    x = np.linspace(x_range[0], x_range[1], 200)
    fig, ax = plt.subplots()
    
    # Standard math backdrop
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    
    # The "Logic Engine"
    last_y = x_range[1] # Start from top
    for off, col in zip(offsets, colors):
        y = x + off
        ax.fill_between(x, y, last_y, facecolor=col, alpha=0.7)
        last_y = y
        
    ax.set(xlim=x_range, ylim=x_range)
    plt.show()

# ALL YOU DO IS THIS:
plot_math_zones((-10, 10), [6, 3, -1, -4], ['red', 'yellow', 'green', 'blue'])