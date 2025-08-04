# -----------------------------------
# Integer Division & Modulus Basics
# -----------------------------------

x = 123456

# Quotient using Integer Division
print("Quotient (x // 10):", x // 10)  # Output: 12345

# Last digit using Modulus Operator
print("Last Digit (x % 10):", x % 10)  # Output: 6

# -----------------------------------
# Count Number of Digits
# -----------------------------------

def count_digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

print("Digit Count:", count_digits(23487))

# -----------------------------------
# Sum of Digits
# -----------------------------------

def sum_of_digits(n):
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result

print("Sum of Digits:", sum_of_digits(123876))

# -----------------------------------
# Product of Digits
# -----------------------------------

def product_of_digits(n):
    result = 1
    while n != 0:
        result *= n % 10
        n = n // 10
    return result

print("Product of Digits:", product_of_digits(12345))

# -----------------------------------
# Sum of Even Digits
# -----------------------------------

def sum_even_digits(n):
    result = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            result += digit
        n = n // 10
    return result

print("Sum of Even Digits:", sum_even_digits(12436784))

# -----------------------------------
# Count of Even Digits
# -----------------------------------

def count_even_digits(n):
    count = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
    return count

print("Count of Even Digits:", count_even_digits(2341684))

# -----------------------------------
# Largest Digit in a Number
# -----------------------------------

def largest_digit(n):
    max_digit = float("-inf")
    while n != 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n = n // 10
    return max_digit

print("Largest Digit:", largest_digit(124579))

# -----------------------------------
# Homework - Product of Largest and Smallest Digit
# -----------------------------------

def product_largest_smallest_digit(n):
    max_digit = float("-inf")
    min_digit = float("inf")
    while n != 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
        n = n // 10
    return max_digit * min_digit

print("Product of Largest & Smallest Digit:", product_largest_smallest_digit(5924137))

# -----------------------------------
# Frequency of a Digit in a Number
# -----------------------------------

def frequency_count(n, k):
    count = 0
    while n != 0:
        if n % 10 == k:
            count += 1
        n = n // 10
    return count

print("Frequency of 2 in 12324562:", frequency_count(12324562, 2))



"""
# range (start , ending , step)

# Single Value is always the end value
# Will go up to 9 , end is always excluded
# Start value by default is zero
for i in range(10):
    print(i, end=" ")

print() 
# Starting at 2 
for i in range(2,10):
    print(i, end=" ")
print()
# By defaut step is 1
for i in range(2,10,2):
    print(i, end=" ")

"""
