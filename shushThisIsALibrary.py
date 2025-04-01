import random
# now we have 1000000000 random-ish points, next we need to know which are in the circle and which aren't
totalPoints = 1000000000
circlePoints = 0
for i in range(1000000000):
    x = random.uniform(1,-1)
    y = random.uniform(1,-1)
    if ((x ** 2) + (y ** 2) < 1):
        circlePoints += 1
approximatePi = (circlePoints / totalPoints) * 4
print(approximatePi)