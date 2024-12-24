def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

if __name__ == "__main__":
    # Example usage
    num1 = 5
    num2 = 3
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")