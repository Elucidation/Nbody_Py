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
            for i in range(0,self.N):
                line = f.readline()
                if not line or line == '':
                    raise Exception('Unexpected End of File')
                self.bodies.append(
                    Body().loadFromString(line.strip()) 
                    )
        if len(self.bodies) != self.N :
            raise Exception('Expected %i bodies, only found %i' % (self.N,len(self.bodies)))

    def step(self):
        self.accCount = 0

        # Update via gravitational acceleration
        self.leapfrog()
        
        self.steps += 1
        self.time += self.DT
    def updatePos(self,dt=None):
        if dt==None:
            dt = self.DT
        for b in self.bodies:
            b.step(dt)
        
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
                    self.bodies[i].vx += ax * self.DT / self.bodies[i].m
                    self.bodies[i].vy += ay * self.DT / self.bodies[i].m
                    
        # Update positions based on velocities
        self.updatePos()
        
    def bruteCompHalf(self):
        for i in range(0,self.N):
            for j in range(i+1,self.N):
                if i != j:
                    ax,ay = self.acc(self.bodies[i],self.bodies[j])
                    self.bodies[i].vx += ax * self.DT / self.bodies[i].m
                    self.bodies[i].vy += ay * self.DT / self.bodies[i].m

                    self.bodies[j].vx -= ax * self.DT / self.bodies[j].m
                    self.bodies[j].vy -= ay * self.DT / self.bodies[j].m
        # Update positions based on velocities
        self.updatePos()

    def leapfrog(self):
        self.updatePos(self.DT/2.0)
        for i in range(0,self.N):
            for j in range(i+1,self.N):
                if i != j:
                    ax,ay = self.acc(self.bodies[i],self.bodies[j])
                    self.bodies[i].vx += ax * self.DT / self.bodies[i].m
                    self.bodies[i].vy += ay * self.DT / self.bodies[i].m

                    self.bodies[j].vx -= ax * self.DT / self.bodies[j].m
                    self.bodies[j].vy -= ay * self.DT / self.bodies[j].m
        # Update positions based on velocities
        self.updatePos(self.DT/2.0)
    
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
