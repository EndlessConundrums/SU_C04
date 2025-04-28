import math
G = 1 # dummy value; must change later (but also don't use the actual value for ease of programming)
def gravityEquation(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    gforceX = G * ((mass1.getMass() * mass2.getMass())/(xDist ** 2)) # newton?
    gforceY = G * ((mass1.getMass() * mass2.getMass())/(yDist ** 2)) # newton.
    accel1X = (gforceX / mass1.getMass())
    accel1Y = (gforceY / mass1.getMass())
    accel2X = (gforceX / mass2.getMass())
    accel2Y = (gforceY / mass2.getMass())
    mass1.accelerate(accel1X, accel1Y)
    mass2.accelerate(accel2X, accel2Y)

class Body:
    def __init__(self, mass, xPos, yPos):
        self.mass = mass
        self.x = xPos
        self.y = yPos
        self.velX = 0
        self.velY = 0
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getMass(self):
        return self.mass
    def accelerate(self, accelX, accelY):
        self.velX += accelX
        self.velY += accelY
    def update(self):
        self.x += self.velX
        self.y += self.velY

Bogol = Body(175, 100, 100)
Grumbill = Body(200, -250, -230)

while True:
    print("Starting loop...")