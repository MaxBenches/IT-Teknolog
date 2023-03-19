# Write a statement that generates a random number in the range of 1-100
# and assigns it to a variable called 'rand'

import random

def main():
    user_num = gen_rand_num()
    print(user_num)


def gen_rand_num():
    rand_num = random.randint(1,100)
    return rand_num

main()