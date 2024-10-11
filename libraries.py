from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


# import datetime

# def age_calculator(birthdate):
#     today = datetime.date.today()
#     age = (today - birthdate) // datetime.timedelta(days=365.2425) 
#     return age

# birthdate = datetime.date(2000, 11, 21)
# age = age_calculator(birthdate)*365

# print(f"The age of the person in days is {age} days.")