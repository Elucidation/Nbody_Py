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
        self.load(*string.split(' '))
        return self
        
    def load(self,x,y,vx,vy,m):
        self.x,self.y,self.vx,self.vy,self.m = map(float,[x,y,vx,vy,m])
        return self
    
