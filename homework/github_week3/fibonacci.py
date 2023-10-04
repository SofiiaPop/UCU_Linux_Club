"""
This is a Python script that takes a number as input from the
user and returns the corresponding number of Fibonacci terms.
It uses the formula for the nth term of the Fibonacci sequence
and functionally decomposes the calculations.
Fill in all the missing code in the functions and in main
"""
import typing

def get_input() -> int:
    """Gets input from the user and returns it as an integer"""
    return int(input())


def fibonacci_list(n: int) -> typing.List[int]:
    """Returns a list of the first n Fibonacci numbers"""
    if isinstance(n, int):    
        fib_sequence = [1, 2]
        for i in range(n-2):
            add = fib_sequence[i] + fib_sequence[i + 1]
            fib_sequence.append(add)
        return fib_sequence


def fibonacci_single(n: int) -> int:
    """Returns the nth Fibonacci number"""
    pass


def golden_section_num() -> float:
    """Returns the golden section number (capital Phi)"""
    pass


def golden_section_reciprocal() -> float:
    """Returns the reciprocal of the golden section number (lowercase phi)"""
    pass


def power(num: int, n: int) -> int:
    """Raises num to the nth power"""
    pass


def sqrt(num: int) -> float:
    """Returns the square root of num"""
    pass


def main():
    """Main function"""
    pass


if __name__ == "__main__":
    main()
