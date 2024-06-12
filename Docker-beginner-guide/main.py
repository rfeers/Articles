import numpy as np

def calculate_square_root(number):
    return np.sqrt(number)

if __name__ == "__main__":
    number = float(input("Enter a number to calculate its square root: "))
    print(f"The square root of {number} is {calculate_square_root(number)}")