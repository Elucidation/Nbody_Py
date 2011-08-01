from re import findall
class Body:
    """Defines a body, containing mass, 2d position & velocity"""
    def __init__(self):
        Body(0,0,0,0,0)

    def __init__(self,x=0,y=0,vx=0,vy=0,m=1):
        self.load(x,y,vx,vy,m)

    def pp(self):
        print "P %.3e %.3e V %.3e %.3e M %.3e" \
              % (self.x, self.y, self.vx, self.vy, self.m)

    def __str__(self):
        return "%e %e %e %e %e" % (self.x,self.y,self.vx,self.vy,self.m)

    def loadFromString(self,string):
        """ provided string """
        self.load(*findall(r'[\-\+\w\.]+', string)) # Just splits by spaces
        return self
        
    def load(self,x,y,vx,vy,m,*extra):
        self.x,self.y,self.vx,self.vy,self.m = map(float,[x,y,vx,vy,m])
        return self

    def step(self,dt=1):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def isIn(self,quad):
        """ Returns boolean whether body is inside square region passed [x y x2 y2] """
        if self.x < quad[0] or self.x > quad[1]:
            return false
        if self.y < quad[2] or self.y > quad[3]:
            return false
        return true
