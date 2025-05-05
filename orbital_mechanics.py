import math
import time
G = 0.003 # this is the actual value :D
def getDistance(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    totalDist = math.sqrt((xDist ** 2) + (yDist ** 2))
    return totalDist
def planetCollision(mass1, mass2):
    if getDistance(mass1, mass2) < (mass1.getRadius() + mass2.getRadius()):
        return True
    else:
        return False
def gravityEquation(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    gforceX2 = G * ((mass1.getMass() * mass2.getMass())/(xDist ** 2)) # newton?
    gforceY2 = G * ((mass1.getMass() * mass2.getMass())/(yDist ** 2)) # newton.
    gforceX1 = (G * ((mass1.getMass() * mass2.getMass())/(xDist ** 2))) * (-1)
    gforceY1 = (G * ((mass1.getMass() * mass2.getMass())/(yDist ** 2))) * (-1)
    accel1X = (gforceX1 / mass1.getMass()) #also newton
    accel1Y = (gforceY1 / mass1.getMass()) #thanks newton for making important physics equations and also calculus
    accel2X = (gforceX2 / mass2.getMass()) #or was it lebneiz?
    accel2Y = (gforceY2 / mass2.getMass())
    mass1.accelerate(accel1X, accel1Y)
    mass2.accelerate(accel2X, accel2Y)
class Body:
    def __init__(self, mass, xPos, yPos, xVel, yVel, rad):
        self.mass = mass
        self.x = xPos
        self.y = yPos
        self.velX = xVel
        self.velY = yVel
        self.radius = rad
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

class Ship(Body):
    def __init__(self, xPos, yPos):
        self.mass = 0.01
        self.x = xPos
        self.y = yPos
        self.velX = 0
        self.velY = 0
        self.radius = 0.1
    def move(self, dirX, dirY):
        self.velX += dirX
        self.velY += dirY
    def getVelX(self):
        return self.velX
    def getVelY(self):
        return self.velY
    def left(self):
        self.move(-1, 0)
    def right(self):
        self.move(1, 0)
    def up(self):
        self.move(0, 1)
    def down(self):
        self.move(0, -1)
Bogol = Body(175000, 100, 100, -1, 1, 17)
Grumbill = Body(200000, -250, -230, 1, -1, 20)
Spiker = Ship(10, 300)

while True:
    print("Starting loop...")
    gravityEquation(Bogol, Grumbill)
    gravityEquation(Bogol, Spiker)
    gravityEquation(Grumbill, Spiker)
    Spiker.down()
    Bogol.update()
    Grumbill.update()
    Spiker.update()
    if (planetCollision(Bogol, Grumbill)) or (planetCollision(Bogol, Spiker)) or (planetCollision(Grumbill, Spiker)):
        print("Collision detected!")
        break
    print("Bogol position:")
    print(Bogol.getX())
    print(Bogol.getY())
    print("Grumbill position:")
    print(Grumbill.getX())
    print(Grumbill.getY())
    print("Spiker position:")
    print(Spiker.getX())
    print(Spiker.getY())
    print("Spiker velocity:")
    print(Spiker.getVelX())
    print(Spiker.getVelY())
    print("Distance(total):")
    print(str(getDistance(Bogol, Grumbill)) + "(Bogol/Grumbill)")
    print(str(getDistance(Bogol, Spiker)) + "(Bogol/Spiker)")
    print(str(getDistance(Grumbill, Spiker)) + "(Spiker/Grumbill)")
    time.sleep(2)