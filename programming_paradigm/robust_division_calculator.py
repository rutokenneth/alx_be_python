def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both inputs must be numeric."
