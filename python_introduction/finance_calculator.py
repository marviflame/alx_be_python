monthly_income = int(input ("Enter your monthly income: "))
monthly_expenses = int(input ("Enter your total monthly expenses: "))
monthly_savings = (float(monthly_income) - float(monthly_expenses))
print (("Your monthly savings are: "), (monthly_savings))

projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print (("Your projected savings after one year is: "), (projected_savings))
