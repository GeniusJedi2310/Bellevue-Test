def calculate_years_to_double(interest_rate, initial_investment):
    years = 0
    investment = initial_investment

    while investment < (2 * initial_investment):
        investment += investment * (interest_rate / 100)
        years += 1

    return years


interest_rate = float(input("Enter the annualized interest rate (%): "))
initial_investment = float(input("Enter the initial investment amount: $"))

years_to_double = calculate_years_to_double(interest_rate, initial_investment)

print(f"It will take {years_to_double} years for the investment to double.")
