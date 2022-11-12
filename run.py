import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Plaese type a number larger than 0 next time")
        quit()
else:
    print("Plaese type in a number next time")
    quit()

random_number = random.randrange(top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Plaese type in a number next time")
        continue

    if user_guess == random_number:
        print("You got it correct")
        break
    else:
        print("You got i wrong...")
        if user_guess > random_number:
            print("Try A Lower Number")
        else:
            print("Try A Higher Number")

print("You got it in", guesses, "guesses!")
        