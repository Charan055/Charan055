def is_prime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True


print('Program to print prime number in given range')
low = int(input('Enter lower bound : '))
up = int(input('Enter upper bound : '))
print('Prime numbers between '+str(low)+' and '+str(up)+' :')
for i in range(low, up+1):
    if is_prime(i):
        print(i)
print('\n')
