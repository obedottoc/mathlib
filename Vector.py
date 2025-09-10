class Vector:
    @staticmethod
    def vector_addition(v1, v2):
        if len(v1) != len(v2):
            return "Error: Vectors must be of the same dimension"
        return [a + b for a, b in zip(v1, v2)]

    @staticmethod
    def vector_subtraction(v1, v2):
        if len(v1) != len(v2):
            return "Error: Vectors must be of the same dimension"
        return [a - b for a, b in zip(v1, v2)]

    @staticmethod
    def scalar_multiplication(v, scalar):
        return [a * scalar for a in v]

    @staticmethod
    def scalar_division(v, scalar):
        if scalar == 0:
            return "Error: Division by zero is not allowed"
        return [a / scalar for a in v]

    @staticmethod
    def dot_product(v1, v2):
        if len(v1) != len(v2):
            return "Error: Vectors must be of the same dimension"
        return sum(a * b for a, b in zip(v1, v2))

    @staticmethod
    def cross_product(v1, v2):
        if len(v1) != 3 or len(v2) != 3:
            return "Error: Cross product is only defined for 3D vectors"
        return [
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0],
        ]
