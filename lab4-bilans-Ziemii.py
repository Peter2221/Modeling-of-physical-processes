import numpy as np
from scipy.optimize import *
from matplotlib import pyplot as plt

def toCel(x):
    return x - 273.15

A = 0.3
S = 1366
sigma = 5.67*(10**(-8))

T = ((S*(1 - A))/(4*sigma))**(1/4)

print("Temperatura na Ziemii nie uwzgledniajac wplywu atmosfery: %f" % toCel(T))

# Uwzgledniajac wplyw atmosfery
a_s = 0.19
t_a = 0.53
a_a = 0.30

t_a_prime = 0.06
a_a_prime = 0.31

S = 1366
sigma = 5.67*(10**(-8))
c = 2.7

# Szukane
Ts = 0
Ta = 0

a_ice = 0.45

def equation_a(Ta, Ts):
    equation = -t_a * (1 - a_s) * S/4 + c * (Ts - Ta)
    equation += sigma * (Ts**4) * (1 - a_a_prime) - sigma * Ta**4
    return equation

def equation_b(Ta, Ts):
    equation = -(1 - a_a - t_a + a_s * t_a) * S/4
    equation -= c * (Ts - Ta)
    equation -= sigma * (Ts**4) * (1 - t_a_prime - a_a_prime)
    equation += 2 * sigma * (Ta**4)
    return equation

def equations(parameters):
    Ta, Ts = parameters
    return equation_a(Ta, Ts), equation_b(Ta, Ts)


x, y = fsolve(equations, (1,1))
print("Temperatura z uwzglednieniem atmosfery: %f" % toCel(x))
print("Temperatura z uwzglednieniem atmosfery: %f" % toCel(y))

Ta_all = []
Ts_all = []
S_all = []

S_range = [S * i / 100 for i in range(80, 120)]
S_reversed = S_range.copy()
S_reversed.reverse()

S_switch = []

for i in S_reversed:
    S = i
    x, y = fsolve(equations, (1,1))

    if y < -10:
        print("Applied")
        a_s = a_ice
        S_switch.append(S)
    else:
        a_s = 0.19

    print(toCel(x), toCel(y))
    S_all.append(S)
    Ta_all.append(toCel(x))
    Ts_all.append(toCel(y))

# print
plt.figure(1)
plt.plot(S_all, Ts_all, label="Temperatura powierzchni")
plt.plot(S_all, Ta_all, label="Temperatura atmosfery")
plt.title("Zależność temperatury od stałej słonecznej. \n Stała słoneczna, dla której następowana zmiana %.2f" % S_switch[0])
#plt.title("Zależność temperatury od stałej słonecznej")
plt.xlabel("Stała słoneczna [W/m^2]")
plt.ylabel("Temperatura [°C]")
plt.legend(loc="upper left")
plt.grid()
plt.show()
