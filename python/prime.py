# function to check if a number is prime or not
def is_prime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True


print('Prime numbers program')
num = int(input('Enter a number : '))
if is_prime(num):
    print(str(num)+' is a prime number\n')
else:
    print(str(num)+' is not a prime number\n')
