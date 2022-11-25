# working on functions
# a function with zero parameters and no return
# declaring a function called hello
def hello():
    print('hello world')


# calling the function hello
hello()

# a function with one parameter


def tables(num):
    for a in range(10):
        print(num, '*', (a+1), "=", num*(a+1))


tables(int(input("enter a value : ")))

# function with return statement


def square(num):
    # returinig square of num
    return num*num


# storing square of 55 in a
a = square(55)
print(a)
