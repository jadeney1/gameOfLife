import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

N = 100

rules = [
    (2,3,3),
    (1,5,3),
    (2,2,3),
    (3,4,3)
]

gmain = np.random.randint(2, size=(N,N))
grids = [gmain.copy() for _ in rules]


def update(frame):
    for k, (lower, upper, birth) in enumerate(rules):
        grid = grids[k]
        new = grid.copy()

        for i in range(N):
            for j in range(N):
                total = (
                    grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, j] + grid[(i-1)%N, (j+1)%N] +
                    grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                    grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, j] + grid[(i+1)%N, (j+1)%N]
                )
                if grid[i,j] == 1 and (total < lower or total > upper):
                    new[i,j] = 0
                elif grid[i,j] == 0 and total == birth:
                    new[i,j] = 1

        grids[k][:] = new
        images[k].set_data(grids[k])

    return images
        

fig, axes = plt.subplots(2,2, figsize=(8,8))
axes = axes.flatten()

images = []

for ax, grid, rule in zip(axes, grids, rules):
    img = ax.imshow(grid, cmap='binary')
    ax.set_title(f"SR: {rule[0]}-{rule[1]}, RB: {rule[2]}")
    ax.axis("off")
    images.append(img)

fig.suptitle("Conway's Game of Life for different Survival Rates (SR) and Rebirth Rates (RB)")
ani = FuncAnimation(fig, update, frames=100, interval=1000, blit=False)

plt.show()
ani.save("Conway's.gif", writer=PillowWriter(fps=5))