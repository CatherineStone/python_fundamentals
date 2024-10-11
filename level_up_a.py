# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name = "Dave"

# print(bool(music) ,bool(shopping_list), bool(num), bool(name), bool(my_name))



# shopping_list = []

# for i in shopping_list:
#     item = input("What would you like to add to your shopping list?")
#     if item in shopping_list:
#         print("You already have that item in your list!")
#     else:
#         shopping_list.append(item)
#         print(shopping_list)




# shopping_list = []

# item = input("What would you like to add to your shopping list?")

# if item in shopping_list:
#     print("You already have that item in your list!")
# else:
#     shopping_list.append(item)
#     print(shopping_list)



# shopping_list = []

# while True:
#     item = input("What would you like to add to your shopping list?").lower()

#     if item == "done":
#         break

#     if item in shopping_list:
#         print("You already have that item on your list!")
#     else:
#         shopping_list.append(item)
#         print(shopping_list)



# def add_up(num1, num2):
#     global total
#     return num1 + num2

# add_up(4,7)

# print(add_up(4,7))


# my_fave_games = ["Animal Crossing", "Stardew Valley", "Call of Duty", "Valorant"]

# while True:
#     game = input("What is your favourite video game?").capitalize()

#     if game == "done":
#         break

#     if game == "":
#         print("You must input a game name.")
#         game = input("What is your favourite video game?").capitalize()

#     if game in my_fave_games:
#         print(f"{game} is one of my favourite games too!")

#     elif game not in my_fave_games:
#         print("I've never played that game before...")



# dinosaurs = ["Triceratops", 
#             "Velociraptor", 
#             "Ankylosaurus", 
#             "Archaeopteryx", 
#             "Tyrannosaurus Rex", 
#             "Stegosaurus", 
#             "Iguanodon"]

# saurus_dinos = []

# for dino in dinosaurs:
#     if "saurus" in dino:
#         saurus_dinos.append(dino)

# print (saurus_dinos)

# saurus_list = [dino for dino in dinosaurs if "saurus" in dino]


print("Type two numbers in to multiply them.")

while True:
    try:
        num1 = int(input("Number 1:    >    "))
        num2 = int(input("Number 2:    >    "))
        break
    except ValueError:
        print("Please only type in whole numbers!")

print(num1*num2)

