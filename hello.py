def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
number = 5
rerust = factorial(number)
print(f"the factorial of the {number} is {rerust}")