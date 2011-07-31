class Body:
    """Defines a body, containing mass, 2d position & velocity"""
    def __init__(self):
        Body(0,0,0,0,0)

    def __init__(self,x=0,y=0,vx=0,vy=0,m=1):
        self.load(x,y,vx,vy,m)

    def pp(self):
        print ("p: %e %e " % (self.x,self.y)).rjust(20) \
              + ("v: %e %e " % (self.vx,self.vy)).rjust(20) \
              + ("m: %e " % self.m).rjust(20)

    def __str__(self):
        return "%d %d %d %d %d" % (self.x,self.y,self.vx,self.vy,self.m)

    def load(self,x,y,vx,vy,m):
        self.x,self.y,self.vx,self.vy,self.m = map(float,[x,y,vx,vy,m])
        return self
        
    def loadFromString(self,string):
        """ provided string """
        self.load(*string.split(' '))
        return self
        
        
