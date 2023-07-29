def check_prime(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
check_prime(number=n)
