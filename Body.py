class Body:
    """Defines a body, containing mass, 2d position & velocity"""
    def __init__(self):
        Body(0,0,0,0,0)

    def __init__(self,x=0,y=0,vx=0,vy=0,m=1):
        self.x = x;
        self.y = y;
        self.vx = vx;
        self.vy = vy;
        self.m = m;

    def __str__(self):
        return "%d %d %d %d %d" % (self.x,self.y,self.vx,self.vy,self.m)
