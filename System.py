from Body import *
from math import sqrt
class System:
    def __init__(self,filename,dt = 1, G = 6.673e-11):
        self.steps = 0
        self.DT = dt
        self.bodies = []
        self.accCount = 0
        self.time = 0
        self.G = G
        with open(filename,'r') as f:
            self.N = int(f.readline())
            self.R = float(f.readline())
            for line in f.readlines():
                self.bodies.append(
                    Body().loadFromString(line.strip()) 
                    )
        if len(self.bodies) != self.N :
            raise Exception('Expected '+self.N+' bodies, only found '+len(self.bodies))

    def step(self):
        self.accCount = 0

        # Update velocities via gravitational acceleration
        self.bruteCompHalf()

        # Update positions based on velocities
        for b in self.bodies:
            b.step(self.DT)
        
        self.steps += 1
        self.time += self.DT

    def __str__(self):
        s = str(self.N) + "\n" + str(self.R) + "\n"
        for b in self.bodies:
            s += str(b) + "\n"
        return s

    def bruteComp(self):
        for i in range(0,self.N):
            for j in range(0,self.N):
                if i != j:
                    ax,ay = self.acc(self.bodies[i],self.bodies[j])
                    self.bodies[i].x += ax * self.DT / self.bodies[i].m;
                    self.bodies[i].y += ay * self.DT / self.bodies[i].m
        
    def bruteCompHalf(self):
        for i in range(0,self.N):
            for j in range(i+1,self.N):
                if i != j:
                    ax,ay = self.acc(self.bodies[i],self.bodies[j])
                    self.bodies[i].vx += ax * self.DT / self.bodies[i].m
                    self.bodies[i].vy += ay * self.DT / self.bodies[i].m

                    self.bodies[j].vx -= ax * self.DT / self.bodies[j].m
                    self.bodies[j].vy -= ay * self.DT / self.bodies[j].m

    
    def acc(self,a,b):
        """ Determines acceleration between two bodies """
        self.accCount += 1
        dx,dy = self.distV(a,b)
        d = self.magn(dx,dy)
        f = self.G*a.m*b.m / (d*d*d) # G*m1*m2/r^3 (r^3 so mult by dx & dy for dir)
        return f*dx,f*dy

    def distV(self,a,b):
        return b.x-a.x,b.y-a.y

    def magn(self, dx, dy):
        return sqrt(dx*dx+dy*dy)
