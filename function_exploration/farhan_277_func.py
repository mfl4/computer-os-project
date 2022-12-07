# function/method

# python function syntax
# def function_name(arguments):
#     # function body
#     """ docstring """
#     instructions

# def show_profile(name, nim):
#     return f"Welcome {name}, your student id is {nim}"


# print(show_profile("Mhd. Farhan lubis", "L200220277"))

user_name = input("Enter your name (1 word): ").lower()
user_pin = input("Enter your pin (3 digit): ")


def basic_login(name, pin):
    nim = "L200220277"
    if user_name == name and user_pin == pin:
        return f"\nWelcome {name}, your student id is {nim}"
    else:
        return "\nYou are not a student of this university"


print(basic_login("farhan", "277"))
