# Task 1
name = input("What's your name? : ")
if name:
    print("Hello", name, ". Welcome to the program")
    print("_______________________________________________")
else:
    print("Hello stranger. Welcome to the program")
    print("_______________________________________________")

# Task 2 & 3 & 4 & 5
while 1:

    password = input("Please enter a password: ")
    password1 = input("Please re-enter your password: ")
    length = int(len(password))
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

    if password == password1:

        if password == BAD_PASSWORDS[4]:
            print("Password is common, please use a less common password")
            print("_______________________________________________")

        else:
            if length < 8 or length > 12:
                print("The password needs to be between 8-12 letters")
                print("_______________________________________________")

            else:
                print("Password successfully saved")
                break

    else:
        print("The passwords are not matching. Please try again")
        print("_______________________________________________")

# Task 6 & 7 & 8

counter = 0


while 1:
    number = int(input("Enter the number you would like to multiply"))
    if type(number) == int:
        break
    else:
        print("Not a number")

#while counter < 13:
