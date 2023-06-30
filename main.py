from datetime import datetime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_age_calculator():
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year

    while True:
        age = current_year - birth_year
        if is_prime(age):
            print(f"The next year when your age will be a prime number is: {current_year}")
            break
        current_year += 1


prime_age_calculator()
