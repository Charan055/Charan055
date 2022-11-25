name = input('Enter your name : ')
age = input('Enter your age : ')
print('Thanks for sharing your details...!')
print("Hi "+name+"!")
if(int(age) > 18):
    print("Yay, You are eligible to vote!")
else:
    print("Sorry, "+name+" you can not vote yet!")
print('\n')
