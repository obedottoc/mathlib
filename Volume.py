from math import pi,pow;

class Volume:
    @staticmethod
    def sphere(radius):
        """Returns Volume of Sphere"""
        return (4 * pi * pow(radius,3))/3


    @staticmethod
    def cylinder(radius,height):
        """Returns Volume of Cylinder"""
        return pi*(radius * radius )*height

    @staticmethod
    def cone(radius,height):
        """Returns Volume of Cone"""
        return pi*(radius * radius )*height/3

    @staticmethod
    def cube(a):
        """Returns Volume of Cube"""
        return a**3

    @staticmethod
    def cuboid(length,breadth,height):
        """Returns Volume of Cuboid"""
        return length*breadth*height
    
    @staticmethod
    def hemisphere(radius):
        """Returns Volume of Hemisphere"""
        return (2/3)*(22/7)*(radius**3)