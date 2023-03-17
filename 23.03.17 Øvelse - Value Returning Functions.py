

# Fungerer ikke
def get_res1():
    res1 = float(input("Please input the value of Resistor 1 in ohms: "))

def get_res2():
    res2 = float(input("Please input the value of Resistor 2 in ohms: "))

def calc_res_total():
    res_total = 1 / ((1/get_res1())+(1/get_res2()))
    return res_total

get_res1()
get_res2()
calc_res_total()


print(res_total)