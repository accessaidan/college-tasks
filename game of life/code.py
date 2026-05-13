import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid = np.zeros((50,50), dtype=int)
#R-PENTOMINO
grid [24,25] = 1
grid[24,26] = 1
grid [25,24] = 1
grid [25,25] = 1
grid [26,25] = 1

#GLIDER
#grid [2,3] = 1
#grid [3,4] = 1
#grid [4,2] = 1
#grid [4,3] = 1
#grid [4,4] = 1

#BLOCK
# grid [24,24] = 1
# grid [24,25] = 1
# grid [25,24] = 1
# grid [25,25] = 1

#BLINKER
# grid[24,25] = 1
# grid[25,25] = 1
# grid[26,25] = 1


def update(frame):
    global grid
    neighbours = (
        np.roll(grid, 1, axis=0)+
        np.roll(grid, -1, axis=0)+
        np.roll(grid, 1, axis=1)+
        np.roll(grid, -1, axis=1)+
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1)+
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1)+
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1)+
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )
    new_grid = np.zeros_like(grid)
    survive = (grid == 1) & ((neighbours == 2) | (neighbours == 3))
    birth = (grid == 0) & (neighbours == 3)
    new_grid[survive] = 1
    new_grid[birth] = 1
    grid = new_grid
    im.set_data(grid)
    return (im,)


fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(grid, cmap='binary', interpolation='nearest')

ani = animation.FuncAnimation(
    fig, update, 
    frames=200, interval=100, blit=True)


plt.imshow(grid, cmap='binary', interpolation='nearest')
plt.axis('off')
plt.show()