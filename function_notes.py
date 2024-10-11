# def say_hello():
#     print("Hello!")

# say_hello()

# def say_goodbye():
#     print("Goodbye!")

# say_goodbye()



# def cash_withdrawal(amount, acc_num):
#     print(f"You are withdrawing £{amount} from account: {acc_num}")

# cash_withdrawal(input("How much are you withdrawing?"), input("From which account?"))

# print(amount)



# def coffee_order(size, drink_type):
#     print(f"You have ordered a {drink_type} in size {size}.")

# coffee_order(input("What size drink would you like?"), input("What type of drink?"))



# balance = 100

# def cash_with(amount):
#     global balance
#     print(f"Your balance is {balance}")
#     print(f"You are withdrawing {amount}")
#     balance -=amount
#     print(f"Your new balance is {balance}")

# cash_with(30)
# cash_with(30)
# print(balance)

# Activity 1

# def happy_birthday(name):
#     print(f"Happy birthday to you. Happy birthday to you. Happy birthday dear {name}. Happy birthday to you!")

# happy_birthday(input("What is your name?"))


# Activity 2

order_count = 0 

def take_order(topping, base, size):
    global order_count
    print(f"A {size} pizza with {topping} and a {base} base.")
    order_count += 1
    print(f"You are order number: {order_count}")

take_order(input("What topping would you like?"), input("What base sauce would you like?"), input("What size pizza would you like?"))
take_order(input("What topping would you like?"), input("What base sauce would you like?"), input("What size pizza would you like?"))
take_order(input("What topping would you like?"), input("What base sauce would you like?"), input("What size pizza would you like?"))