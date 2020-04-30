import numpy as np
import matplotlib.pyplot as plt

# 1 zadanie
steps = 50
padding = 1
padding += 1

x = steps + padding

lenOfSquare = steps/5
first = int(x/2.5 + 1)
second = int(first + lenOfSquare)

# Temparatures
T_all = 20
T_middle = 80
T_edge = T_all

# constans
K = 400
cw = 385
ro = 8900

kappa = 1.17 * 10**(-4)

# Przyjeta dyskretyzacja
a = 1
dt = 0.1
dx = a/steps
dy = a/steps

# Warunki poczatkowe macierzy
T = np.ones((x, x))
T[0:len(T), 0:len(T)] = T_edge
T[1:len(T)-1, 1:len(T)-1] = T_all
T[first:second, first:second] = T_middle

temp_prev = None
temp_curr = np.mean(T)
delta = 1000
count = 0

all_dt = 0

# Pojedyncza iteracja -> nie bierzemy pod uwage wartosci na brzegu ktore sa stale
while delta > 0.001:
    for i in range(1, len(T)-1):
        for j in range(1, len(T)-1):
            T[i, j] = T[i, j] + (kappa * dt / (dx ** 2)) * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) + (kappa * dt / (dy ** 2)) * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1])
    # Przepisujemy wartości z obramowań do wartości na brzegach
    size = len(T) - 1
    # obramowanie
    T[0, :] = T[1, :]
    T[size, :] = T[size - 1, :]
    T[:, 0] = T[:, 1]
    T[:, size] = T[:, size - 1]
    # Rogi
    T[0, 0] = T[1, 1]
    T[0, size] = T[1, size - 1]
    T[size, 0] = T[size - 1, 1]
    T[size, size] = T[size - 1, size - 1]
    # srodek
    T[first:second, first:second] = 80
    if count % 1 == 0:
        temp_prev = temp_curr
        temp_curr = np.mean(T)
        delta = abs(temp_curr - temp_prev)
    count += 1
    all_dt += dt

plt.figure(1)
plt.title('Rozkład po czasie t = %.2f, Średnia temperatura: %.2f' % (all_dt, np.mean(T)))
plt.imshow(T)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()



