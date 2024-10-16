class Circle:
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self,point):
        sm=0
        for i in range(0,1):
            sm += ((point)[i] - (self.centre)[i])**2
            
        
        if sm < (self.radius)**2:
            return sm
        elif sm >= (self.radius)**2:
            return False
