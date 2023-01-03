import matplotlib.pyplot as plt


x = list(range(0,10))

y = list(range(-10,0))

plt.plot(x,y)

plt.show()

a = [0, -50, 25, 67, -223]
b = [0, 5, 7, 5, 9]
plt.plot(a, b)
plt.show()

plt.axis([-50, 25, 5, 9])
plt.plot(a, b)
plt.show()

plt.title("My Graph")
plt.xlabel("Array A")
plt.ylabel("Array B")
plt.plot(a, b)
plt.show()

