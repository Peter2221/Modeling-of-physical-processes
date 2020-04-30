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
T_edge = 20

# constans
K = 400
cw = 385
ro = 8900
h = 0.002
q = 1000

kappa = 1.17 * 10**(-4)

# Przyjeta dyskretyzacja
dt = 0.1
dx = 1/steps
dy = 1/steps

# Warunki poczatkowe macierzy
T = np.ones((x, x))
T[0:len(T), 0:len(T)] = T_edge
T[1:len(T)-1, 1:len(T)-1] = T_all
T[first:second, first:second] = T_middle

# Elementy kontaktujace sie z blaszka
coor = []

T[first-1, first-1:second+1] = 200
for i in range(first-1, second+1):
    coor.append([first-1, i])

T[second, first-1:second+1] = 200
for i in range(first-1, second+1):
    coor.append([second, i])

T[first:second, first-1] = 200
for i in range(first, second+1):
    coor.append([i, first-1])

T[first:second, second] = 200
for i in range(first, second+1):
    coor.append([i, second])

temp_prev = None
temp_curr = np.mean(T)
delta = 1000
count = 0

all_dt = 0

# Pojedyncza iteracja -> nie bierzemy pod uwage wartosci na brzegu ktore sa stale
while delta > 0.00001:
    for i in range(1, len(T)-1):
        for j in range(1, len(T)-1):
            if [i, j] in coor:
                T[i, j] = T[i, j] + (kappa * dt / (dx ** 2)) * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) + (
                            kappa * dt / (dy ** 2)) * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) + (q/(K*h*ro))
            else:
                T[i, j] = T[i, j] + (kappa * dt / (dx ** 2)) * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) + (
                        kappa * dt / (dy ** 2)) * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1])
                # Dla elementow kontaktujacych sie z blaszka
    # stale wartosci w srodku i na brzegach
    size = len(T) - 1
    # obramowanie
    T[0, :] = T_edge
    T[size, :] = T_edge
    T[:, 0] = T_edge
    T[:, size] = T_edge
    # srodek
    T[first:second, first:second] = T_middle
    if count % 1 == 0:
        temp_prev = temp_curr
        temp_curr = np.mean(T)
        delta = abs(temp_curr - temp_prev)
        print(delta)
    count += 1
    all_dt += dt

plt.figure(1)
plt.title('Rozkład po czasie t = %.2f, Średnia temperatura: %.2f' % (all_dt, np.mean(T)))
plt.imshow(T)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()



