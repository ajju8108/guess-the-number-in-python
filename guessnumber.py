import random
randNumber = random.randint(1,10)
print(randNumber)
name = input("Enter your NAME : ")
print(f"Start Your GAME : {name}")

userGuess = None
guess = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess Number : " ))
    guess += 1
    if(userGuess == randNumber):
        print("your guess is right")
    else:
        if(userGuess > randNumber):
            print("your guess is wrong! please enter a smaller number")
        else:
            print("your guess is wrong! please enter a larger number")

print(f"{guess} Attempt of guesses {name}")


#f = open("highscorenumber.txt", "r")
#print(f.read())

if(guess == 1):
    f = open ("highscorenumber.txt", "w")
    print(f.write (f"Highest score is {guess} by {name}"))
else:
    f= open("highscorenumber.txt", "r")
    print(f.read())




f= open("highscorenumber.txt", "r")
print(f.read())
f.close()
