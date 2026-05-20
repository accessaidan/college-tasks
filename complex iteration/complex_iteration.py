import numpy as np
import matplotlib.pyplot as plt

width = 600
height = 400
max_iter = 100

y_min, x_min = 2.5, 1.0
y_max, x_max = 1.24, 1.25

x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
c = x[np.newaxis, :] + 1j*y[:, np.newaxis]

print(f"GRID SHAPE: {c.shape}")
print(f"sample c: {c[0,0]}, {c[height//2, width//2]}")

def mandelbrot(c, max_iter):
    z=np.zeros_like(c)
    escape_time = np.zeros(c.shape, dtype=int)
    mask = np.ones(c.shape, dtype=bool)
    for i in range(1, max_iter+1):
        z[mask] = z[mask]**2 + c[mask]
        escaped = np.abs(z) > 2
        escape_time[escaped & mask] = i
        mask [escaped] = False
    return escape_time

escape_time = mandelbrot(c, max_iter)
