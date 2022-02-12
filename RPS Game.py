import random #importing modules

outputList = ("rock", "paper", "scissors") #varibales and lists
computerChoice = (outputList[random.randrange(0,2)])
playerChoice = (input("Type rock, paper or scissors then press enter"))

if computerChoice == playerChoice:
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","You guys brawled it out but mostley to no avail")

elif computerChoice == "rock" and playerChoice == "paper":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","You win")

elif computerChoice == "paper" and playerChoice == "rock":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","You lost bitch")

elif computerChoice == "scissors" and playerChoice == "rock":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","you win")

elif computerChoice == "scissors" and playerChoice == "paper":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","You lost to cutty thingies")

elif computerChoice == "rock" and playerChoice == "scissors":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","you have the same IQ as a rock considering you lost to one")

elif computerChoice == "paper" and playerChoice == "scissors":
    print("the computer chose",computerChoice, "and you chose", playerChoice, "\n","you win")

elif playerChoice == "ar-15":
    print("heheheh gun go burrrrrrrrrr")
else:
    print("either type rock, paper, or scissors or stop putting a space infront of the word you fuck")






