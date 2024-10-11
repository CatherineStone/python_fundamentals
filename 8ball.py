import random
from colorama import Fore, Back, Style

print(Style.RESET_ALL)

bad_fortune = ["It is not looking good...", 
               "Try again.", 
               "Unfortunately not...",
               "All stars point to no.",
               "Maybe next time.",
               "You are not in luck.",
               "The answer is no.",
               "Pray for better times.",
               "I woudln't buy any lottery tickets today...",
               "Maybe next year."]

good_fortune = ["Absolutely.", 
                "You are in luck.", 
                "Go and buy a lottery ticket",
                "It's your lucky day.",
                "Everything points to yes.",
                "YES YES YES",
                "It is decidedly so.",
                "You betcha!",
                "All the yes's",
                "My fortune tells me good things are ahead for you..."
                ]

while True:

    random_number = random.randint(1,20)

    question = input("What is your question?")

    if question == "":
        print("Please input a question.")

    elif random_number % 2 == 0:
        print(Fore.GREEN + (random.choice(good_fortune)))
        print(Style.RESET_ALL)

    else:
        print(Fore.RED + (random.choice(bad_fortune)))
        print(Style.RESET_ALL)