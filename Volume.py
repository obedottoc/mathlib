class Volume:
    def Sphere(self):
        pass

    def Cylinder(self):
        pass

    def Cone(self):
        pass

    def Cube(self,a):
        return a**3

    def Cuboid(self,length,breadth,height):
        return length*breadth*height
    
    def Hemisphere(self,radius):
        return (2/3)*(22/7)*(radius**3)