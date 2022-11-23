import random

while True:
    up = 0  # user point
    cp = 0  # computer point
    for a in range(1, 7):
        uc = input("Enter a choice (rock, paper, scissors): ")  # user choice
        options = ["rock", "paper", "scissors"]  # set of possible options
        cc = random.choice(options)  # computer choice
        print(f"\nYou chose {uc}, computer chose {cc}.\n")

        if uc == cc:
            print(f"Both players selected {uc}. It's a tie!")

        elif uc == "rock":
            if cc == "scissors":
                print("Rock smashes scissors! You win!")
                up = up + 1
            else:
                print("Paper covers rock! You lose.")
                cp = cp + 1
        elif uc == "paper":
            if cc == "rock":
                print("Paper covers rock! You win!")
                up = up + 1
            else:
                print("Scissors cuts paper! You lose.")
                cp = cp + 1
        elif uc == "scissors":
            if cc == "paper":
                print("Scissors cuts paper! You win!")
                up = up + 1
            else:
                print("Rock smashes scissors! You lose.")
                cp = cp + 1
    else:
        break

if up == cp:
    print("Game result=Draw :|")
    print("User Score:", up)
    print("CPU Score:", cp)
elif up > cp:
    print("Game result= User WON the game :)CONGRATSS!!!")
    print("User Score:", up)
    print("CPU Score:", cp)
elif cp > up:
    print("Game result= CPU WON the game LOL XDD")
    print("User Score:", up)
    print("CPU Score:", cp)
else:
    pass
