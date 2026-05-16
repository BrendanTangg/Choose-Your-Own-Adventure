print("Welcome to the Choose Your Own Adventure Game!")

name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

print("Hello", name, "Your age is", age, "years old.")

if age >= 18:
    print("You are old enough!")

    ans = input("Do you want to play? ").lower()
    if ans == "yes":
        print("You are starting with", health, "health.")
        print("Let's play!")

        direction = input("Do you want to go left or right? (left/right) ")
        if direction == "left":
            ans = input("Nice, you follow the path, but encounter a pond. Do you swim across or around? (across/around) ")

            if ans == "across":
                print("You swim across, but were bit by an alligator. You lost 5 health.")
                health -= 5

                ans = input("You notice a house and a river. Which one do you go to? (house/river) ")
                if ans == "house":
                    print("You go to the house and meet the owner. He doesn't like you and you lose 5 health")
                    health -= 5
                    if health <= 0:
                        print("You have 0 health and lose the game...")
                    else:
                        print("You survive and win the game.")
                else:
                    print("You fall into the river and die")
            else:
                print("Nice, you go around the pond and reach the other side.")
                ans = input("You notice a house and a river. Which one do you go to? (house/river) ")
                if ans == "house":
                    print("You go to the house and meet the owner. He doesn't like you and you lose 5 health")
                    health -= 5
                    if health <= 0:
                        print("You have 0 health and lose the game...")
                    else:
                        print("You survive and win the game.")
                else:
                    print("You fall into the river and die")
        else:
            print("You fell down and died...")
    else:
        print("Cya...")
else:
    print("You are not old enough to play...")