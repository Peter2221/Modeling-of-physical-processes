import numpy as np
import matplotlib.pyplot as plt

def updateBorders(T, value):
    T[0, :] = value
    T[len(T) - 1, :] = value
    T[:, 0] = value
    T[:, len(T) - 1] = value

# 1 zadanie
steps = 10
padding = 1
padding += 1

x = steps + padding

lenOfSquare = steps/5
first = int(x/2.5 + 1)
second = int(first + lenOfSquare)

# Temparatures
T_edge = 40
T_all = 20
T_middle = 80

# Warunki poczatkowe macierzy
T = np.ones((x, x))
T[0:len(T), 0:len(T)] = T_edge
T[1:len(T)-1, 1:len(T)-1] = T_all
T[first:second, first:second] = T_middle

size = len(T) - 1
# obramowanie
T[0, :] = T[1, :]
T[size, :] = T[size - 1, :]
T[:, 0] = T[:, 1]
T[:, size] = T[:, size - 1]
# Rogi
T[0,0] = T[1,1]
T[0,size] = T[1,size - 1]
T[size,0] = T[size - 1, 1]
T[size, size] = T[size - 1, size - 1]

plt.figure(1)
plt.imshow(T)
plt.colorbar()
plt.show()
