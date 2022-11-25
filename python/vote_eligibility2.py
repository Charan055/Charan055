name = input("please enter your name...")
age = input("please enter yor age...")
gender = input("please select your gender...").lower()
print("thanks for sharing details.")
if gender == ("male"):
    greet = "Mr."
elif gender == ("female"):
    greet = "Ms."
if (int(age) > 18):
    print("Congrats, you are eligible to vote, "+greet+name+'\n')
else:
    print("Sorry, you are not eligible to vote, "+greet+name+'\n')
