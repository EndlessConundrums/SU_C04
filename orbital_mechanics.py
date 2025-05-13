import time
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env
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
    def getPos(self):
        return self.pos
    def getVelX(self):
        return self.vel[0]
    def getVelY(self):
        return self.vel[1]
    def getVel(self):
        return self.vel
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
        self.vel += direction
    def reset(self):
        self.pos = np.array([np.random.uniform(-1000., 1000.), np.random.uniform(-1000., 1000.)])
    def left(self):
        self.move(np.array([-0.3, 0.]))
    def right(self):
        self.move(np.array([0.3, 0.]))
    def up(self):
        self.move(np.array([0., 0.3]))
    def down(self):
        self.move(np.array([0., -0.3]))
Bogol = Body(175000., np.array([100., 100.]), np.array([-1., 0.]), 17., "Bogol")
Grumbill = Body(200000., np.array([-250., -230.]), np.array([1., 0.]), 20., "Grumbill")
Spiker = Ship(np.array([np.random.uniform(-1000., 1000.), np.random.uniform(-1000., 1000.)]), "Spiker")
bodyList = [Bogol, Grumbill, Spiker]

class WorldEnv(gym.Env):
    def __init__(self):
        super(WorldEnv, self) .__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=-10000, high=10000, shape=(2,), dtype=np.int32)
        self.state = self._reset()
    def reset(self, seed=None, options=None):
        Spiker.reset()
        self.state = self._reset()
        return np.array(self.state, dtype=np.int32), {}
    def step(self, action):
        distVector = getDistVector(Spiker, Grumbill)
        distance = np.sqrt((distVector[0] ** 2) + (distVector[1] ** 2))
        if action == 0: #up
            Spiker.up()
        elif action == 1: #right
            Spiker.right()
        elif action == 2: #down
            Spiker.down()
        elif action == 3: #left
            Spiker.left()
        
        if distance < (Spiker.getRadius() + Grumbill.getRadius()):
            reward = 100.
            done = True
        else:
            reward = 1 / distance
            done = False
        mainLoop()
        self.state = (Spiker.getX(), Spiker.getY())
        return np.array(self.state, dtype=np.int32), reward, done, False, {}
    def _reset(self):
        return (Spiker.getX(), Spiker.getY())
    

def costFunction():
    distVector = getDistVector(Spiker, Grumbill) #Grumbill is the target because it's far away
    distance = np.linalg.norm(distVector)
    score = distance * -1
    return score
def mainLoop():
    for i in range(len(bodyList)):
        gravityEquation(bodyList[i])
    for i in range(len(bodyList)):
        bodyList[i].update()
    if planetCollision():
        print("Collision detected!")

env = WorldEnv()
check_env(env)

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

obs, _ = env.reset()
for _ in range(10):
    action, _ = model.predict(obs)
    obs, reward, done, _, _ = env.step(action)
    print("Action: " + str(action) + ", reward: " + str(reward) + ", current position: " + str(obs))
    if done:
        print("Collided with Grumbill!")
        break