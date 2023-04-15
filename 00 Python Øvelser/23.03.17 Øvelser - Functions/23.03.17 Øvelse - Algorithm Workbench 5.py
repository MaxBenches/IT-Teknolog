# Write a function named times_ten that accepts a number as an argument.
# When the function is called,
# it should return the value of its argument multiplied by 10

def main():
    user_num = times_ten(int(input('Please input an integer: ')))
    print(user_num)

def times_ten(num):
    calc = num * 10
    return calc

main()