import math
class Area:
    @staticmethod
    def circle(radius: float) -> float:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (radius ** 2)

    @staticmethod
    def rectangle(length: float, width: float) -> float:
        
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return length * width
    
    @staticmethod
    def square(side: float) -> float:
        """Calculate the area of a square."""
        if side < 0:
            raise ValueError("Side length cannot be negative")
        return side * side

    @staticmethod
    def triangle(base: float, height: float) -> float:
        """Calculate the area of a triangle."""
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height