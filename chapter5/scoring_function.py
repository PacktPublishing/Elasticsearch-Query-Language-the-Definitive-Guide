import matplotlib.pyplot as plt
import numpy as np


def score_function(x):
    if x < 60:
        return 5
    elif 60 <= x <= 360:
        return 5 * (1 - (x - 60) / 300)  # linear decay between 60 and 360
    else:
        return 0


x_values = np.linspace(0, 540, 500)
y_values = np.array([score_function(x) for x in x_values])

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Score Function", color="blue")
plt.title("Score Function")
plt.xlabel("Time (seconds)")
plt.ylabel("Score")
plt.ylim(-0.5, 5.5)
plt.axhline(0, color="black", lw=0.5, ls="--")
plt.axvline(0, color="black", lw=0.5, ls="--")
plt.grid()
plt.legend()
plt.show()
