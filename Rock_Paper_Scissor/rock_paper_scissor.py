import random
def game(rounds):
    u_score = 0
    c_score = 0
    r = 1
    while r<=rounds:
        print(f"Round {r}")
        print("1 - Rock, 2 - Paper, 3 - Scissors")
        choices = {1:"Rock", 2:"Paper", 3:"Scissors"}
        u_choice = int(input("Make your choice: "))
        # verify that the choices are correct
        if u_choice > 3 or u_choice < 1:
            print("Sorry! Please select between the mentioned number")

        print(f"Your choice: {choices[u_choice]}")

        comp_choice = random.randint(1,3)

        # two people doing same symbol won't work
        while comp_choice == u_choice:
            comp_choice = random.randint(1,3)

        print(f"Computer chose {choices[comp_choice]}")

        if (comp_choice==2 and u_choice==1) or (comp_choice==3 and u_choice==2) or (comp_choice==1 and u_choice==3):
            c_score +=1
        else:
            u_score +=1
        
        print(f"You:{u_score}, Computer:{c_score}")
        r +=1
        print()

    if u_score > c_score:
        print("YOU WINNNNN!!!!!!!")
    elif u_score == c_score:
        print("DRAW")
    else:
        print("YOU LOST :(")

def main():
    print("Welcome to the Rock Paper Scissors")
    print()
    while True:        
        rounds = int(input("Enter the number of rounds you'd like to play: "))
        print()
        game(rounds)
        print("Wanna Continue?")
        y = input("Press Y for yes and N for No: ")
        if y=="N":
            break

if __name__ == '__main__':
    main()