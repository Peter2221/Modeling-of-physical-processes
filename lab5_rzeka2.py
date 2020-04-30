import numpy as np
from matplotlib import pyplot as plt


def createMatrix(diag, diagUpper, diagBelow, length):
    a = np.zeros((length, length))
    np.fill_diagonal(a, diag)

    for i in range(len(a) - 1):
        a[i, i + 1] = diagUpper
        a[i + 1, i] = diagBelow

    return a

# dx, dt
dx = 1
dt = 1

Lmax = 200

# Stałe
Lin = 10
Lout = 90
A = 5
U = 0.2
D = 0.5
m = 10

n = 10

# adwekcyjna, dyfuzyjna liczba Couranta
Ca = U*dt/dx
Cd = D*dt/(dx*dx)

length = 200

# set  BB
BB = createMatrix(1 - Cd, Cd/2 - Ca/4, Cd/2 + Ca/4, length)
# set AA
AA = createMatrix(1 + Cd, -Cd/2 + Ca/4, -Cd/2 - Ca/4, length)

AB = np.matmul(np.linalg.inv(AA), BB)

AB[0, :] = 0

# test
c = createMatrix(5, 10, -10, 10)

def simulate(n):
    c = np.zeros(length)
    c_next = c.copy()

    c_in = m / (A * dx * n)

    data = []
    # dyskretyzacja rownania
    for i in range(0, 1000):
        if(i < n):
            c[int(Lin/dx)] = c_in
        else:
            c[int(Lin/dx)] = 0

        c_next = AB.dot(c)

        data.append(c[Lout])
        c, c_next = c_next, c

    return data

data10 = simulate(10)
data1 = simulate(1)

# Sprawdzenie masy
masa10 = print("10:", np.sum(data10) * A * dx)
masa1 = print("1:", np.sum(data1) * A * dx)

plt.figure(1)
plt.plot(range(0, len(data10)), data10, label="n=10")
plt.plot(range(0, len(data1)), data1, label="n=1")
plt.title("Krzywe przejścia zanieczyszczenia w punkcie Lout")
plt.ylabel("Stężenie zanieczyszczenia [kg / m^3]")
plt.xlabel("Czas symulacji [s]")
plt.legend(loc="upper left")
plt.grid()
plt.show()