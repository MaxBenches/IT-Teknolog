"""
Write a function named shout.
The function should accept a string argument and
display it in uppercase with an exclamation mark concatenated at the end.
"""

def shout():
    user_shout = input("What would you like to shout?\n")
    big_shout = user_shout.upper()
    print(f"{big_shout}" + "!")

shout()