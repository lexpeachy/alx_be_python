#Prompt the user for their monthly income
monthly_income = int(input("enter your monthly income"))
#prompt the user for their total monthly expenses
monthly_expenses = int(input("enter your total monthly expenses"))
#calculate the users monthly saving
monthly_savings = monthly_income - monthly_expenses
#Calculate the projected savings after one year, incorporating the interest
Projected_Savings = monthly_savings * 12 + monthly_savings * 0.05
#Display the user’s monthly savings.
#Display the projected annual savings after including interest.
print ("your monthly savings are $",monthly_savings)
print ("Projected savings after one year, with interest, is:", Projected_Savings)
