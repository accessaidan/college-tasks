import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((50,50), dtype=int)

grid [24,25] = 1
grid [25,25] = 1
grid [26,25] = 1

neighbours = [
    np.roll(grid, 1, axis=0),
    np.roll(grid, -1, axis=0),
    np.roll(grid, 1, axis=1),
    np.roll(grid, -1, axis=1),
    np.roll(np.roll(grid, 1, axis=0), 1, axis=1),
    np.roll(np.roll(grid, 1, axis=0), -1, axis=1),
    np.roll(np.roll(grid, -1, axis=0), 1, axis=1),
    np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
]

plt.imshow(grid, cmap='binary', interpolation='nearest')
plt.axis('off')
plt.show()