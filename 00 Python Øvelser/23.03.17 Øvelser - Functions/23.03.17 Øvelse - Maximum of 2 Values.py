# Write a function named max that accepts two integer values as arguments
# and returns the value that is the greater of the two.
# For example, if 7 and 12 are passed as arguments to the function,
# the function should return 12. Use the function in a program that
# prompts the user to enter two integer values.
# The program should display the value that is the greater of the two.


def main():
    num1 = int(input("Please input an integer: "))
    num2 = int(input("Please input another integer: "))
    print(f"The biggest integer is: {max(num1,num2)}")


def max(int1,int2):
    if int1 >= int2:
        return int1
    else:
        return int2

main()