# Write a program that generates 100 random numbers and
# keep a count of how many of those random numbers are
# even and how many of them are odd.


# Virker ikke
import random

def main():
    print(rand_numb_plus_count())




def rand_numb_plus_count():
    num_even = 0
    num_odd = 0
    for i in range(10):
        num = print(random.randint(0,100))
        if (num%2) == 0:
            num_even =+ 1
        else:
            num_odd =+1
    return num_odd + num_even



main()