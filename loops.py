# for i in range(1,11,1):
#     print(i)


# sum = 0 

# for i in range(1,101,1):    
#     sum = sum + i

#     print(sum)



# answer = input("Who ordered a Cortado?")

# while answer != "Alex":
#     print("Incorrect!")
#     answer = input("Who ordered a Cortado?")
# else:
#     print("Correct!")


# phrase = ["Hello world "]

# for i in phrase:
#     print(i*13)


# phrase = "Hello world "

# while phrase == "Hello world ":
#     print(phrase*13)
#     break


# for i in range(1, 13):
#     print("i =", i, ":", end=" ")
#     for j in range(1, 13):
#         print("{:2d}".format(i * j), end=" ")
#     print()

tries = 1
password = input("Password: ")

while password != "hunter2":
    tries += 1
    print("Incorrect password.")
    password = input("Password: ")
    if tries >= 3:
        print("Too many attempts, you have been locked out.")
        break

else:
    print("Welcome back!")
