# Look at the following function header: def my_function(a, b, c).
# Now look at the following call to my_function: my_function(3, 2, 1).
# When this call executes, What value will be assigned to a?
# What value will be assigned to b – and to c?

def main():
    my_function(3,2,1)


def my_function(a,b,c):
    print(c,a,b)

main()