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

class Time:
    @staticmethod
    def hours_to_minutes(hours: float) -> float:
        """Convert Hours to Minutes."""
        return hours * 60

    @staticmethod
    def minutes_to_hours(minutes: float) -> float:
        """Convert Minutes to Hours."""
        return minutes / 60

    @staticmethod
    def seconds_to_minutes(seconds: float) -> float:
        """Convert Seconds to Minutes."""
        return seconds / 60

    @staticmethod
    def minutes_to_seconds(minutes: float) -> float:
        """Convert Minutes to Seconds."""
        return minutes * 60


class Mass:
    @staticmethod
    def kilograms_to_pounds(kg: float) -> float:
        """Convert Kilograms to Pounds."""
        return kg * 2.20462

    @staticmethod
    def pounds_to_kilograms(pounds: float) -> float:
        """Convert Pounds to Kilograms."""
        return pounds / 2.20462

    @staticmethod
    def grams_to_ounces(grams: float) -> float:
        """Convert Grams to Ounces."""
        return grams / 28.3495

    @staticmethod
    def ounces_to_grams(ounces: float) -> float:
        """Convert Ounces to Grams."""
        return ounces * 28.3495
