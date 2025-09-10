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