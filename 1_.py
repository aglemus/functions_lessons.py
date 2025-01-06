
# Functions are ways to wrap your code
# into reuseable units
# Function = a block of reuseable code
#            place () after the function name to invoke it

### This is how you define it, anything indented means it belongs to the function
# "name" is a placeholder for the information that will be used later.
# in this case, "Bro" is the information that will be used in "name"
## "name" is a parameter
# You only need to define it once, then you can call it as many times
# as you want
# Function is useless you call it
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

### This is how you invoke/call a function, it can be used only once.
## To use it multiple times, you must invoke/call it set number of times
    # For example, to use this song 3 times, you must invoke/call it three times
#happy_birthday()
#happy_birthday()
#happy_birthday()

### This is called an argument, you are sending information to the function
    # so that it can then be used.
## An argument can be used in diffirent ways, in this case
    # diffirent names can be inputed
# "Bro" , "Aliyana" , "Valeria" , are arguments.
# inorder to call the function with an argument, you must have an equal number
    # of perameters so that both peices of information in the argument can
    # be used in the function
# The order of the arguments matter.
happy_birthday("Bro", 20)
happy_birthday("Aliyana", 20)
happy_birthday("Valeria", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Valeria", 42.50, "01/01") 

# Return = statement used to end a function
        # and send a result back to the caller.
# You cannot put anything at the end of a Return.
# When you use a return, you change the data on the original function
#### A function becomes whatever is returned.

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

# Another example

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last

full_name = create_name("valeria", "nunez")

print(full_name)