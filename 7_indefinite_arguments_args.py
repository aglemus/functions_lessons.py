
#*args = allows you to pass multiple non-key arguments
#       Allows you to have as many arguments(placeholders) as you want.
#       When using args, it combines all arguments into a tuple
#       YOU CAN USE ANY NAME YOU WANT, but you HAVE to put * infront.
#**kwargs = allows you to pass multiple keywords-arguments
#           * unpacking perator
#           1. positional 2. default 3. keyword 4. ARBITRARY

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3, 2818, 989873, -3, 8372, -44955, 43773929274, -1121999377347392))

# def display_name(*args):
#     for arg in args:
#         print(arg, end="-")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants")


# def print_address(**kwargs):
#     for key, value in kwargs.values():
#         print(f"{key}: {value}")

# print_address(street= "1234 Fake St.",
#                 city ="Chicago", 
#                 state="IL",
#                 zip="60639",)


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr.", "Spongebob", "Harold", "Squarepants",
                street= "1234 Fake St.",
                apt="100",
                city ="Chicago", 
                state="IL",
                zip="60639",)


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"