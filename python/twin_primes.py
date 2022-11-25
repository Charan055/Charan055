def is_prime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True


print('Twin Primes program')
low = int(input('Enter lower bound : '))
up = int(input('Enter upper bound : '))
print('Twin primes from '+str(low)+' and '+str(up)+' :')
for i in range(low, up-1):
    if is_prime(i) and is_prime(i+2):
        print('['+str(i)+','+str(i+2)+']')
print('\n')
