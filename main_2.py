import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import linregress

def randNum():
    return np.random.normal(0, 1)

def rSquared(x, y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return r_value ** 2, intercept, slope
R2 = 0
numOfSteps = 1000
numOfParticles = 1

x = 0
y = 0

dx = 0
dy = 0

x_coor_all = []
y_coor_all = []

dx_values = []
dy_values = []

for i in range(numOfParticles):
    x = 0
    y = 0
    x_coor = []
    y_coor = []
    dx_all = []
    dy_all = []
    for j in range(0, numOfSteps):
        dx = randNum()
        dy = randNum()
        x += dx
        y += dy

        x_coor.append(x)
        y_coor.append(y)
        dx_all.append(dx)
        dy_all.append(dy)

    x_coor_all.append(x_coor)
    y_coor_all.append(y_coor)
    dx_values.append(dx_all)
    dy_values.append(dy_all)

plt.figure(1)
plt.title("Trajektoria dla " + str(numOfParticles) + " cząstki")
for i in range(numOfParticles):
    plt.plot(x_coor_all[i], y_coor_all[i])
plt.ylabel("y")
plt.xlabel("x")
# plt.show()

# Średni kwadrat położenia po n krokach czasowych dla m cząstek
r2 = []

for i in range(numOfParticles):
    x_all = x_coor_all[i]
    y_all = y_coor_all[i]
    r = 0
    steps_coor = []
    for j in range(0, len(x_all)):
        # Kwadrat położenia dla pojedynczego punktu cząstki
        sum_squared = np.power(x_all[j], 2) + np.power(y_all[j], 2)
        # Dodawanie elementu do wektora położeń
        steps_coor.append(sum_squared)
    r2.append(steps_coor)

# obliczanie średniej dla wszystkich cząstek
r2 = np.asmatrix(r2)
r2 = np.mean(r2, axis=0)
r2 = np.asarray(r2)
r2 = r2.tolist()

t = []
value = []

# dziedzina czasu
for i in range(0, numOfSteps):
    t.append(i)

# WSPOLCZYNNIK REGRESJI
R_2, intercept, slope = rSquared(t, r2[0])
print("R_2 : ", R_2, " Num of particles : ", numOfParticles)

for i in range(0, numOfSteps):
   value.append(t[i]*slope + intercept)

plt.figure(3)
plt.title("Zależność średniego kwadratu położenia od czasu dla " + str(numOfParticles) + " cząstek")
plt.suptitle("Krzywa regresji liniowej")
plt.plot(t, r2[0], label='original data')
plt.plot(t, value, 'r', label='fitted line')
plt.xlabel("t")
plt.ylabel("Średni kwadrat położenia")
plt.show()

# rysowanie
plt.figure(2)
plt.title("Zależność średniego kwadratu położenia od czasu dla " + str(numOfParticles) + " cząstek")
plt.xlabel("t")
plt.ylabel("Średni kwadrat położenia")
plt.plot(t, r2[0])
plt.show()

dr2 = []

points_x = []
points_y = []

points_x = np.concatenate(x_coor_all, axis=0)
points_y = np.concatenate(y_coor_all, axis=0)

plt.figure(3)
plt.title("Rozkład gęstości dla 1000 cząstek i 1000 kroków czasowych.")
plt.xlabel("x")
plt.ylabel("y")
plt.hist2d(points_x, points_y, bins=(50,50), cmap=plt.cm.viridis)
plt.show()

sum_all = 0

# Średni kwadrat przemieszczen po n krokach czasowych dla 1 czastki
for i in range(numOfParticles):
    dx_all = dx_values[i]
    dy_all = dy_values[i]
    r = 0
    steps_coor = []
    for j in range(0, len(x_all)):
        # Kwadrat położenia dla pojedynczego punktu cząstki
        sum_squared = np.power(dx_all[j], 2) + np.power(dy_all[j], 2)
        # Dziele przez liczbe kroków
        # sum_squared = sum_squared / (j+1)
        # Suma poprzedniego położenia z nowym
        sum_all += sum_squared

sum_all = sum_all / numOfParticles
print("SUM ALL : ", sum_all)
print("D parameter = ", sum_all / (2 * 2))




