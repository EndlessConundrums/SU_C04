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
        for j in range(len(bodyList)):
            if bodyList[i] == bodyList[j]:
                continue
            else:
                mass1 = bodyList[i]
                mass2 = bodyList[j]
                if np.linalg.norm(getDistVector(mass1, mass2)) < (mass1.getRadius() + mass2.getRadius()):
                    print(np.linalg.norm(getDistVector(mass1, mass2)))
                    return True
    return False
def gravityEquation(mass1):
    gVector1 = np.array([0., 0.])
    for i in (range(len(bodyList))):
        if bodyList[i] == mass1:
            continue
        else:
            mass2 = bodyList[i]
            totalDist = getDistVector(mass1, mass2)
            mag = np.linalg.norm(totalDist)
            gForce1 = (G * ((mass1.getMass() * mass2.getMass()) / (mag ** 2))) * -1
            unitForce = totalDist / mag
            gVector1 += unitForce * gForce1
            gVector1 = gVector1 / mass1.getMass()
        mass1.accelerate(gVector1)
class Body:
    def __init__(self, mass, position, velocity, rad, name):
        self.mass = mass
        self.pos = position
        self.vel = velocity
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
    def __init__(self, position, name):
        self.mass = 0.01
        self.pos = position
        self.vel = np.array([0., 0.])
        self.radius = 0.1
        self.name = name
    def move(self, direction):
        self.vel[0] += direction
    def getVelX(self):
        return self.velX
    def getVelY(self):
        return self.velY
    def left(self):
        self.move([-1, 0])
    def right(self):
        self.move([1, 0])
    def up(self):
        self.move([0, 1])
    def down(self):
        self.move([0, -1])
Bogol = Body(175000., np.array([100., 100.]), np.array([0., 0.]), 17., "Bogol")
Grumbill = Body(200000., np.array([-250., -230.]), np.array([0., 0.]), 20., "Grumbill")
Spiker = Ship(np.array([10., 300.]), "Spiker")
bodyList = [Bogol, Grumbill, Spiker]

def mainLoop():
    print("Starting loop...")
    for i in range(len(bodyList)):
        gravityEquation(bodyList[i])
    for i in range(len(bodyList)):
        bodyList[i].update()
        print(bodyList[i].getName() + " position:")
        print(bodyList[i].getX())
        print(bodyList[i].getY())
    if planetCollision():
        print("Collision detected!")

for i in range(2):
    mainLoop()
    time.sleep(1)