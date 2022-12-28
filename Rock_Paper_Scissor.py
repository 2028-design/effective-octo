import random

print("Winning Rules of the Rock Paper Scissor game as follows: \n"+ "Rock  vs Paper     -> Paper wins \n"+ "Rock  vs Scissor   -> Rock wins \n"+ "Paper vs Scissor   -> Scissor wins \n")

Dict={1:'Rock',2:'Paper',3:'Scissor'}

while True:
    print("Entry choice \n 1 for Rock, \n 2 for Paper and \n 3 for Scissor \n")

    user= int(input("Your choice: "))

    while user > 3 or user < 1:
        user= int(input("enter valid input: "))


    print("Your choice is: " + Dict[user])
    print("\nNow its my turn.......")

    comp= random.randint(1, 3)
    
    while comp == user:
        comp = random.randint(1, 3)
    
    print("My choice is: " + Dict[comp]+'\n')
    
    print(Dict[user] + " V/s " + Dict[comp])
           
    if((user == 1 and comp == 2) or (user == 2 and comp == 1)):
        print("paper wins", end="\n")
        result = "paper"
    elif((user == 1 and comp == 3) or (user == 3 and comp == 1)):
        print("Rock wins", end="\n")
        result = "Rock"
    else:
        print("scissor wins", end="\n")
        result = "scissor"
        
    if result == Dict[user]:
        print("<== You win ==>")
    else:
        print("<== I win ==>")
        
    print("Do you wanna play again? (Y/N)")
    ans = input().upper()
    
    if ans == 'N':
        break
    else:
        print('\n')

print("\nHad fun playing with you")
print('Dust me up, when you get bored')