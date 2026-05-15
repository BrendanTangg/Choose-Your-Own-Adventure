print("Welcome to the Choose Your Own Adventure Game!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "Your age is", age, "years old.")

if age >= 18:
    print("You are old enough!")

    ans = input("Do you want to play? ")
    if ans == "yes":
        print("Let's play!")

else:
    print("You are not old enough to play...")