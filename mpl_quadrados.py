import matplotlib.pyplot as plt

quadrados = []

for i in range (1, 10):
    n = (i) ** 2
    quadrados.append(n)


fig, ax = plt.subplots()
ax.plot(quadrados)
plt.show()