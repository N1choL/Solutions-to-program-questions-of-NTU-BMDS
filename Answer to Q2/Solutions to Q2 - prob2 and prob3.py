import matplotlib.pyplot as plt


# define rate constants k1, k2, k3
k1 = 100
k2 = 600
k3 = 150

# define 4 rate equations and 4 concentrations of E, S, ES, P are y1, y2, y3 and y4
def f1(t, y1, y2, y3, y4):
    return k1*y1*y2 - k2*y3 - k3*y3
def f2(t, y1, y2, y3, y4):
    return k1*y1*y2 - k2*y3
def f3(t, y1, y2, y3, y4):
    return k1*y1*y2 - k2*y3 - k3*y3
def f4(t, y1, y2, y3, y4):
    return k3*y3


# set the time interval h and number of iterations N
h = 0.00001
N = 2000


# initial conditions of f1, f2, f3, f4
t = [0]
y1 = [1]
y2 = [10]
y3 = [0]
y4 = [0]


# calculate using Runge-Kutta method
for i in range(N):
    # concentration of E
    K11 = f1(t[-1], y1[-1], y2[-1], y3[-1], y4[-1])  # find the last element in y1, y2, y3, y4
    K12 = f1(t[-1] + 0.5*h, y1[-1] + 0.5*h*K11, y2[-1] + 0.5*h*K11, y3[-1] + 0.5*h*K11, y4[-1] + 0.5*h*K11)
    K13 = f1(t[-1] + 0.5*h, y1[-1] + 0.5*h*K12, y2[-1] + 0.5*h*K12, y3[-1] + 0.5*h*K12, y4[-1] + 0.5*h*K12)
    K14 = f1(t[-1] + h, y1[-1] + h*K13, y2[-1] + h*K13, y3[-1] + h*K13, y4[-1] + h*K13)
    y1_temple = y1[-1] - h/6*(K11 + 2*K12 + 2*K13 + K14)


    # concentration of S
    K21 = f2(t[-1], y1[-1], y2[-1], y3[-1], y4[-1])  # find the last element in y1, y2, y3, y4
    K22 = f2(t[-1] + 0.5*h, y1[-1] + 0.5*h*K21, y2[-1] + 0.5*h*K21, y3[-1] + 0.5*h*K21, y4[-1] + 0.5*h*K21)
    K23 = f2(t[-1] + 0.5*h, y1[-1] + 0.5*h*K22, y2[-1] + 0.5*h*K22, y3[-1] + 0.5*h*K22, y4[-1] + 0.5*h*K22)
    K24 = f2(t[-1] + h, y1[-1] + h*K23, y2[-1] + h*K23, y3[-1] + h*K23, y4[-1] + h*K23)
    y2_temple = y2[-1] - h/6*(K21 + 2*K22 + 2*K23 + K24)


    # concentration of ES
    K31 = f3(t[-1], y1[-1], y2[-1], y3[-1], y4[-1])  # find the last element in y1, y2, y3, y4
    K32 = f3(t[-1] + 0.5*h, y1[-1] + 0.5*h*K31, y2[-1] + 0.5*h*K31, y3[-1] + 0.5*h*K31, y4[-1] + 0.5*h*K31)
    K33 = f3(t[-1] + 0.5*h, y1[-1] + 0.5*h*K32, y2[-1] + 0.5*h*K32, y3[-1] + 0.5*h*K32, y4[-1] + 0.5*h*K32)
    K34 = f3(t[-1] + h, y1[-1] + h*K33, y2[-1] + h*K33, y3[-1] + h*K33, y4[-1] + h*K33)
    y3_temple = y3[-1] + h/6*(K31 + 2*K32 + 2*K33 + K34)

    # concentration of P
    K41 = f4(t[-1], y1[-1], y2[-1], y3[-1], y4[-1])  # find the last element in y1, y2, y3, y4
    K42 = f4(t[-1] + 0.5*h, y1[-1] + 0.5*h*K41, y2[-1] + 0.5*h*K41, y3[-1] + 0.5*h*K41, y4[-1] + 0.5*h*K41)
    K43 = f4(t[-1] + 0.5*h, y1[-1] + 0.5*h*K42, y2[-1] + 0.5*h*K42, y3[-1] + 0.5*h*K42, y4[-1] + 0.5*h*K42)
    K44 = f4(t[-1] + h, y1[-1] + h*K43, y2[-1] + h*K43, y3[-1] + h*K43, y4[-1] + h*K43)
    y4_temple = y4[-1] + h/6*(K41 + 2*K42 + 2*K43 + K44)

    if y1_temple > 0:
        y1.append(y1_temple)
    else:
        y1.append(0)

    if y2_temple > 0:
        y2.append(y2_temple)
    else:
        y2.append(0)

    y3.append(y3_temple)

    if y4_temple > 10:
        y4.append(10)
    else:
        y4.append(y4_temple)

    t.append(t[-1] + h)


# show plots of 4 substances E, S, ES and P
plt.title('Concentration of E')
plt.xlabel('Time/min')
plt.ylabel('Concentration/μM')
plt.plot(t,y1)
plt.show()

plt.title('Concentration of S')
plt.xlabel('Time/min')
plt.ylabel('Concentration/μM')
plt.plot(t,y2)
plt.show()

plt.title('Concentration of ES')
plt.xlabel('Time/min')
plt.ylabel('Concentration/μM')
plt.plot(t,y3)
plt.show()

plt.title('Concentration of P')
plt.xlabel('Time/min')
plt.ylabel('Concentration/μM')
plt.plot(t,y4)
plt.show()


# the rate V = k3 * [ES], show the relationship between V and [S]
V = []
for i in range(len(y3)):
    V.append(k3*y3[i])

plt.title('Relationship between [S] and V')
plt.xlabel('Concentration of S/μM')
plt.ylabel('Rate of change of the product P')
plt.plot(y2, V)
plt.show()

