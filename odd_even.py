"""Task 1: Odd or Even."""

def modulo(num: int) -> bool:
    """Use % operator to check if num is Even"""

    return num % 2 == 0

def bitwise_and(num: int) -> bool:
    """Use & operator to check if num is Even"""

    return num & 1 == 0

def bitwise_shift(num: int) -> bool:
    """Use >> and <<  to check if num is Even"""

    return num >> 1 << 1 == num

def recursion(num: int) -> bool:
    """Use recursion to check if num is Even"""

    if num == 1:
        return False

    if num == 0:
        return True

    return recursion(num - 2)

# Use lambda function to check if num is Even
lambda_approach = lambda num: num % 2 == 0

test_size = 15

for num in range(test_size):
    assert(modulo(num) == bitwise_and(num) == recursion(num) == bitwise_shift(num) == lambda_approach(num))
    print(num, modulo(num), bitwise_and(num),
          recursion(num), bitwise_shift(num),
          lambda_approach(num))