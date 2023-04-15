# Write a program that asks the user to enter the monthly costs
# for the following expenses incurred from operating his
# or her automobile: Loan payment, insurance, gas, oil, tires and maintenance.
# The program should then display the total monthly costs of these expenses,
# and the total annual costs of these expenses.


def main():
    loan = float(input("How much is your loan payment a month? "))
    insurance = float(input("How much is your insurance a month? "))
    gas = float(input("How much do you spend on gas a month? "))
    oil = float(input("How much do you spend on oil a month? "))
    tires = float(input("How much do you spend on tires a month? "))
    maintenance = float(input("How much do you spend on maintenance a month? "))
    print(f"The total monthly cost is: "
          f"{cost_month(loan,insurance,gas,oil,tires,maintenance)}$")
    print(f"The total annual cost is: "
          f"{cost_month(loan,insurance,gas,oil,tires,maintenance)*12}$")


def cost_month(exp1, exp2, exp3, exp4, exp5, exp6):
    month_sum = exp1 + exp2 + exp3 + exp4 + exp5 + exp6
    return month_sum

def cost_year(exp1, exp2, exp3, exp4, exp5, exp6):
    year_sum = exp1 + exp2 + exp3 + exp4 + exp5 + exp6
    return year_sum

main()