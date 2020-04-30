import numpy as np
from matplotlib import pyplot as plt

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

def simulate(n):
    length = 200
    c = np.zeros(length)
    c_next = c.copy()

    c_in = m / (A * dx * n)

    data = []
    # dyskretyzacja rownania
    for i in range(0, 1000):
        for j in range(2, len(c)-1):
            if(i < n):
                c[int(Lin/dx)] = c_in
            else:
                c[int(Lin/dx)] = 0
            c_next[j] = c[j] + (Cd*(1-Ca) - (Ca/6)*(Ca*Ca - 3*Ca + 2))*c[j+1]\
                        - (Cd*(2 - 3*Ca) - (Ca/2)*(Ca*Ca - 2*Ca - 1))*c[j]\
                        + (Cd*(1 - 3*Ca) - (Ca/2)*(Ca*Ca - Ca - 2))*c[j-1]\
                        + (Cd*Ca + (Ca/6)*(Ca*Ca - 1))*c[j-2]

        data.append(c[Lout])
        c, c_next = c_next, c

    return data

data10 = simulate(10)
data1 = simulate(1)

# Sprawdzenie masy
masa10 = print("10:", np.sum(data10) * A * dx)
masa1 = print("1:", np.sum(data1) * A * dx)

masa10 = print("10:", np.sum(data10) * A * dx * 10)
masa1 = print("1:", np.sum(data1) * A * dx * 10)

plt.figure(1)
plt.plot(range(0, len(data10)), data10, label="n=10")
plt.plot(range(0, len(data1)), data1, label="n=1")
plt.title("Krzywe przejścia zanieczyszczenia w punkcie Lout")
plt.ylabel("Stężenie zanieczyszczenia [kg / m^3]")
plt.xlabel("Czas symulacji [s]")
plt.legend(loc="upper left")
plt.grid()
plt.show()