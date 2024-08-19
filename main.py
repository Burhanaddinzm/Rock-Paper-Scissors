import random

def take_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n"))
        
            while choice > 3 or choice < 1:
                choice = int(input("Enter a valid choice (1, 2, or 3): "))
            break
        
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    return choice

def logic(choice, comp_choice):
    if choice == comp_choice:
        print("Its a draw!")
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("Paper wins!")
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Rock wins!")
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        print("Scissors wins!")
        result = "Scissors"
        
    if result == 'DRAW':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

print('''Winning rules of the game ROCK PAPER SCISSORS are :
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins
''')

while True:
    choice = take_user_choice()
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print(f"Your choice is {choice_name}.")
    print("Now its computer turn...")
    
    comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
        
    print(f"Computer's choice is {comp_choice_name}.")
    print(f"{choice_name} VS {comp_choice_name}")

    logic(choice, comp_choice)
        
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n' or ans == 'N':
        break
    
print("Thanks for playing!")