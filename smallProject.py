import random

####### Dice Generator
while True:
    try:
        nbDice = int(input("How many dice ? (maximum 6, press 9 to quit)"))
        if nbDice == 9:
            break
        elif nbDice == 0 or nbDice > 6:
            print("Please between 1 & 6")
        else:
            print("Generating " + str(nbDice) + " number between 1 & 6:")
            for i in range(nbDice):
                print(random.randint(1, 6))
    except ValueError:
        print("Please, only integer)")

####### Password générator
try:
    length = int(input("Password générator ! Lenght ?"))
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    print("".join(random.sample(s, length)))
except ValueError:
    print("Please, enter an integer)")

####### Rock paper cisor
user = str(input("Please select ROCK (R), PAPER(P), CISOR(C)," +
      "the program will use the random function..: )"))
if user == 'C' or user == 'P' or user == 'R':
    choices=['C','P','R']
    cpu = random.choice(choices)
    print("Computer choose " + cpu)
    if user == cpu: print("Same")
    elif user == 'R':
        if cpu == 'P': print("Rock against paper, computer win.")
        elif cpu == 'C': print("Rock against cisor, you win.")
    elif user == 'P':
        if cpu == 'R': print("Paper against rock, you win.")
        elif cpu == 'C': print("Paper against cisor, computer win.")
    elif user == 'C':
        if cpu == 'P': print("Cisor against rock, computer win.")
        elif cpu == 'R': print("Cisor against rock, computer win.")
else: print("Only C P or R please")