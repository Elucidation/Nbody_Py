class BHTree:
    """ Barnes-Hut Tree to contain all bodies """
    def __init__(self,quad):
        self.body = Body() # body/aggregate body stored in this node
        self.quad = quad # square region that tree represents [x,y,x2,y2]
        self.NW = None
        self.NE = None
        self.SW = None
        self.SE = None

    def insert(b):
        """ Insert a body into the tree """
        pass

    def updateForce(b):
        """ approximate net force on body b from all bodies in tree """
