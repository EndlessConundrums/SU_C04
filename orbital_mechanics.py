import math
import time
G = 3 # dummy value; must change later (but also don't use the actual value for ease of programming)
def getDistance(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    totalDist = math.sqrt((xDist ** 2) + (yDist ** 2))
    return totalDist
def gravityEquation(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    gforceX2 = G * ((mass1.getMass() * mass2.getMass())/(xDist ** 2)) # newton?
    gforceY2 = G * ((mass1.getMass() * mass2.getMass())/(yDist ** 2)) # newton.
    gforceX1 = (G * ((mass1.getMass() * mass2.getMass())/(xDist ** 2))) * (-1)
    gforceY1 = (G * ((mass1.getMass() * mass2.getMass())/(yDist ** 2))) * (-1)
    print("G-forces: ")
    print(gforceX1)
    print(gforceY1) # the issue is that they slingshot around each other, but placing them into an orbit should solve it
    print(gforceX2)
    print(gforceY2) # debugging
    accel1X = (gforceX1 / mass1.getMass()) # also newton
    accel1Y = (gforceY1 / mass1.getMass()) # thanks newton for making important physics equations and also calculus
    accel2X = (gforceX2 / mass2.getMass())
    accel2Y = (gforceY2 / mass2.getMass())
    mass1.accelerate(accel1X, accel1Y)
    mass2.accelerate(accel2X, accel2Y)

class Body:
    def __init__(self, mass, xPos, yPos, xVel, yVel):
        self.mass = mass
        self.x = xPos
        self.y = yPos
        self.velX = xVel
        self.velY = yVel
        self.radius = self.mass / 5
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getMass(self):
        return self.mass
    def getRadius(self):
        return self.radius
    def accelerate(self, accelX, accelY):
        self.velX += accelX
        self.velY += accelY
    def update(self):
        self.x += self.velX
        self.y += self.velY

Bogol = Body(175, 100, 100, 0, 0)
Grumbill = Body(200, -250, -230, 0, 0)

while True:
    print("Starting loop...")
    gravityEquation(Bogol, Grumbill)
    Bogol.update()
    Grumbill.update()
    if getDistance(Bogol, Grumbill) < (Bogol.getRadius() + Grumbill.getRadius()):
        print("Collision detected!")
        break
    print("Bogol position:")
    print(Bogol.getX())
    print(Bogol.getY())
    print("Grumbill position:")
    print(Grumbill.getX())
    print(Grumbill.getY())
    print("Distance(total):")
    print(getDistance(Bogol, Grumbill))
    time.sleep(1)