def main():
    avg_3_num(a,b,c)


a = float(input("Input 1. number: "))
b = float(input("Input 2. number: "))
c = float(input("Input 3. number: "))


def avg_3_num(num1,num2,num3):
    sum = num1 + num2 + num3
    avg = sum/3
    print(avg)

main()