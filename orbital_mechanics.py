import math
import time
import numpy as np
G = 0.003 # this is the actual value :D
def getDistVector(mass1, mass2):
    xDist = mass1.getX() - mass2.getX()
    yDist = mass1.getY() - mass2.getY()
    totalDist = np.array([xDist, yDist])
    return totalDist
def planetCollision():
    for i in range(len(bodyList)):
        for j in range(len(bodyList) - 1):
            if bodyList[i] == bodyList[j]:
                break
            mass1 = bodyList[i]
            mass2 = bodyList[j]
            if np.linalg.norm(getDistVector(mass1, mass2)) < (mass1.getRadius() + mass2.getRadius()):
                return True
    return False
def gravityEquation(mass1):
    gVector1 = np.array([0., 0.])
    for i in (range(len(bodyList))):
        if bodyList[i] == mass1:
            break
        else:
            mass2 = bodyList[i]
            totalDist = getDistVector(mass1, mass2)
            mag = np.linalg.norm(totalDist)
            gForce1 = G * ((mass1.getMass() * mass2.getMass()) / (mag ** 2))
            unitForce = totalDist / mag
            gVector1[0] += unitForce[0] * gForce1
            gVector1[1] += unitForce[1] * gForce1
            print(gForce1)
        mass1.accelerate(gVector1)
class Body:
    def __init__(self, mass, xPos, yPos, xVel, yVel, rad, name):
        self.mass = mass
        self.pos = np.array([xPos, yPos])
        self.vel = np.array([xVel, yVel])
        self.radius = rad
        self.name = name
    def getX(self):
        return self.pos[0]
    def getY(self):
        return self.pos[1]
    def getMass(self):
        return self.mass
    def getRadius(self):
        return self.radius
    def getName(self):
        return self.name
    def accelerate(self, accel):
        self.vel += accel
    def update(self):
        self.pos += self.vel

class Ship(Body):
    def __init__(self, xPos, yPos, name):
        self.mass = 0.01
        self.pos = np.array([xPos, yPos])
        self.vel = np.array([0., 0.])
        self.radius = 0.1
        self.name = name
    def move(self, dirX, dirY):
        self.vel[0] += dirX
        self.vel[1] += dirY
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
Bogol = Body(175000., 100., 100., -1., 1., 17, "Bogol")
Grumbill = Body(200000., -250., -230., 1., -1., 20, "Grumbill")
Spiker = Ship(10., 300., "Spiker")
bodyList = [Bogol, Grumbill, Spiker]
counter = 0
while True:
    print("Starting loop...")
    for i in range(len(bodyList)):
        gravityEquation(bodyList[i])
        bodyList[i].update()
        print(bodyList[i].getName() + " position:")
        print(bodyList[i].getX())
        print(bodyList[i].getY())
    if planetCollision():
        print("Collision detected!")
        break
    if counter == 2:
        break
    time.sleep(2)
    counter += 1