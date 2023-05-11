
# This program gives the user the choice to access one of two financial calculators
# The programe returns an error message if user fails to choose 'bond' or 'investment'

import math
investment = ("To calculate the amount of interest you'll earn on your investment" )
bond = ("To calculate the amount you'll have to pay on a home loan" )

print(investment)
print(bond)

investment_type = ["bond", "investment"]

user_input = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

if user_input == "investment":
    amount_deposited = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate as a percentage without the sign, %: "))/100
    investment_years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Would you like a simple or compound interest?: ")

# A = P*(1 + r*t)
    if interest == "simple":
        total_amount = (amount_deposited) * (1 + interest_rate * investment_years)
        print("Your total interest is:", total_amount)

# A = P * math.pow((1+r),t)
    elif interest == "compound":
        total_amount = (amount_deposited) * math.pow((1 + interest_rate), investment_years)
        print("The total amount is:", total_amount)
    
    else:
        print("invalid entry. Please enter simple or compound interest")

# monly_repayment = (i * P)/(1 - (1 + i)**(-n))
elif user_input == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate as a percentage without the sign, %: "))
    months = float(input("Enter the number of months you plan to take to repay the bond: "))

# The monthly repayment is calculated by dividing by 12
    monthly_interest = (interest_rate/100)/12
    monthly_repayment = (monthly_interest * present_value) / (1 - (1 + monthly_interest)**(-months))
    
    print("Your monthly repayment is: ", monthly_repayment)

else:
    print("Invalid selection. Please, choose 'bond' or 'investment'")


