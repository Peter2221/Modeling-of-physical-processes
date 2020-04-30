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
T_edge = 20
T_all = 20
T_middle = 80

a = 1

# constans
kappa = 1.17 * 10**(-4)
# Przyjeta dyskretyzacja
dt = 0.1
dx = a/steps
dy = a/steps

# Warunki poczatkowe macierzy
T = np.ones((x, x), dtype=np.float64)
T[0:len(T), 0:len(T)] = T_edge
T[1:len(T)-1, 1:len(T)-1] = T_all
T[first:second, first:second] = T_middle

temp_prev = None
temp_curr = np.mean(T)
delta = 1000
count = 0

all_dt = 0

# Pojedyncza iteracja -> nie bierzemy pod uwage wa rtosci na brzegu ktore sa stale
while delta > 0.00001:
    for i in range(1, len(T)-1):
        for j in range(1, len(T)-1):
            T[i,j] = T[i,j] + (((kappa*dt)/(dx**2))*(T[i+1,j] - 2*T[i,j] + T[i-1,j])) + (((kappa*dt)/(dy**2))*(T[i,j+1] - 2*T[i,j] + T[i,j-1]))
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
    count += 1
    all_dt += dt

plt.figure(1)
plt.title('Rozkład po czasie t = %.2f, Średnia temperatura: %.2f' % (all_dt, np.mean(T)))
plt.imshow(T)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()



