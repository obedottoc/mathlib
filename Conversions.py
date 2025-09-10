class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Convert Celsius to Kelvin."""
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15


class Length:
    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Convert Meters to Feet."""
        return meters * 3.281

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """Convert Feet to Meters."""
        return feet / 3.281

    @staticmethod
    def kilometers_to_miles(km: float) -> float:
        """Convert Kilometers to Miles."""
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """Convert Miles to Kilometers."""
        return miles / 0.621371


