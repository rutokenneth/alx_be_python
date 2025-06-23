class Calculator:
    """
    A class demonstrating static and class methods for calculations.
    """

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        It does not access or modify class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        It can access and modify class state (e.g., class attributes).
        """
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

# Demonstrating the usage of Calculator methods

# Using the static method
sum_result = Calculator.add(10, 5)
print(f"Sum using static method: {sum_result}")

# Using the class method
product_result = Calculator.multiply(10, 5)
print(f"Product using class method: {product_result}")

# You can also call static/class methods from an instance,
# but it's more idiomatic to call them directly on the class.
my_calculator = Calculator()
sum_result_instance = my_calculator.add(20, 3)
print(f"Sum using static method via instance: {sum_result_instance}")

product_result_instance = my_calculator.multiply(20, 3)
print(f"Product using class method via instance: {product_result_instance}")

# Demonstrating how the class method can access class attributes
# You can change the class attribute and the class method will reflect it
Calculator.calculation_type = "Basic Math"
print("\n--- After changing calculation_type ---")
product_result_new_type = Calculator.multiply(7, 8)
print(f"Product using class method with new type: {product_result_new_type}")
