import math
massOne = [100,300,300,10,0] #first number is mass, next two are position, final two are velocity
massTwo = [120,-300,-300,-10,0]
numMasses = 2
gravitationalConstant = 1 #DUMMY VALUE; REPLACE LATER
while True:
    xDist = massOne[1] - massTwo[1]
    yDist = massOne[2] - massTwo[2]
    distance = math.sqrt((xDist ** 2) + (yDist ** 2))
    force = gravitationalConstant * ((massOne[0] * massTwo[0]) / (distance ** 2))