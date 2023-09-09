"""
Module: f_calculator

This module contains a basic calculator class.
"""

class Calculator:
    def add(self, x_value, y_value):
        """
        Adds two numbers and returns the result.

        Args:
            x_value (float): The first number.
            y_value (float): The second number.

        Returns:
            float: The sum of x_value and y_value.
        """
        return x_value + y_value

    def subtract(self, x_value, y_value):
        """
        Subtracts one number from another and returns the result.

        Args:
            x_value (float): The first number.
            y_value (float): The number to subtract from x_value.

        Returns:
            float: The result of subtracting y_value from x_value.
        """
        return x_value - y_value

    def multiply(self, x_value, y_value):
        """
        Multiplies two numbers and returns the result.

        Args:
            x_value (float): The first number.
            y_value (float): The second number.

        Returns:
            float: The product of x_value and y_value.
        """
        return x_value * y_value

    def divide(self, x_value, y_value):
        """
        Divides one number by another and returns the result.

        Args:
            x_value (float): The numerator.
            y_value (float): The denominator.

        Returns:
            float: The result of dividing x_value by y_value.

        Raises:
            ValueError: If y_value is zero.
        """
        if y_value == 0:
            raise ValueError("Division by zero is not allowed")
        return x_value / y_value
