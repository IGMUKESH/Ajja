import math
import cmath # Complex math ke liye, jaise sqrt(-1)

# Allowed names (functions and constants) jo eval() mein use ho sakti hain
ALLOWED_NAMES = {
    "abs": abs,
    "round": round,
    "pow": pow,
    "sqrt": math.sqrt,
    "csqrt": cmath.sqrt, # Complex square root
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "exp": math.exp,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "degrees": math.degrees,
    "radians": math.radians,
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": float('inf'),
    "nan": float('nan'),
    "j": 1j, # Imaginary unit
    # Aap aur bhi functions add kar sakte hain
}

# Restricted __builtins__ to prevent execution of arbitrary code
RESTRICTED_BUILTINS = {
    'True': True,
    'False': False,
    'None': None,
    # Standard exceptions (optional, but good for some error handling in eval itself if needed)
    'ArithmeticError': ArithmeticError,
    'AssertionError': AssertionError,
    'AttributeError': AttributeError,
    'Exception': Exception,
    'FloatingPointError': FloatingPointError,
    'LookupError': LookupError,
    'NameError': NameError,
    'NotImplementedError': NotImplementedError,
    'OSError': OSError,
    'OverflowError': OverflowError,
    'RuntimeError': RuntimeError,
    'SyntaxError': SyntaxError,
    'SystemError': SystemError,
    'TypeError': TypeError,
    'ValueError': ValueError,
    'ZeroDivisionError': ZeroDivisionError,
}


def calculate_expression(expression):
    """
    Ek mathematical expression ko safely evaluate karta hai.
    """
    try:
        # User input ko thoda clean karte hain (extra spaces hataana)
        expression = expression.strip()

        # Simple replacements for user-friendliness
        expression = expression.replace('^', '**') # Power ke liye ^ ko ** se replace
        expression = expression.replace('ans', str(LAST_RESULT)) # Pichla result 'ans' se access

        # Evaluate the expression using the allowed names and restricted builtins
        # __builtins__ ko restrict karna bahut zaroori hai security ke liye
        result = eval(expression, {"__builtins__": RESTRICTED_BUILTINS}, ALLOWED_NAMES)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except NameError as e:
        return f"Error: Invalid name or function used: {e}"
    except SyntaxError:
        return "Error: Invalid syntax in expression!"
    except TypeError as e:
        return f"Error: Type mismatch in expression: {e}"
    except OverflowError:
        return "Error: Result too large to compute!"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def print_help():
    print("\n--- Advanced Calculator Help ---")
    print("Type 'quit' or 'exit' to close the calculator.")
    print("Type 'help' to see this message again.")
    print("Type 'ans' to use the previous result in your expression.")
    print("\nAvailable Functions & Constants:")
    for name in sorted(ALLOWED_NAMES.keys()):
        print(f"  {name}")
    print("\nOperators:")
    print("  + (addition), - (subtraction), * (multiplication), / (division)")
    print("  % (modulus), ** or ^ (power)")
    print("  () for grouping expressions (e.g., (2+3)*5 )")
    print("\nExamples:")
    print("  2 * (sin(pi/2) + cos(0))")
    print("  log10(100) + sqrt(16)")
    print("  2^10")
    print("  csqrt(-1)  (for complex numbers, like sqrt of -1)")
    print("--- End of Help ---\n")

# Global variable to store the last result
LAST_RESULT = 0

if __name__ == "__main__":
    print("Welcome to Advanced Calculator!")
    print_help()

    while True:
        expression = input("Calc> ")
        if expression.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        elif expression.lower() == 'help':
            print_help()
            continue
        elif not expression: # Empty input
            continue

        result = calculate_expression(expression)
        if isinstance(result, (int, float, complex)):
            LAST_RESULT = result # Store successful result for 'ans'
            print(f"Result: {result}")
        else: # Error message
            print(result)
