import random
pointsInCirlce = 0

for i in range(0, 1000_000_0):
    x = random.random()
    y = random.random()

    distance = (x*x + y*y)**0.5
    if distance < 1:
        pointsInCirlce += 1
pi = 4 * pointsInCirlce / 1000_000_000 * 100
print(pi)