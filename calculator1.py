# Display a welcome message
print("Welcome to the Fiber Optic Installation Cost Calculator!")

# Get the company name from the user
company_name = input("Please enter your company name: ")

# Get the number of feet of fiber optic to be installed from the user
feet = float(input("Please enter the number of feet of fiber optic to be installed: "))

# Multiply the total cost as the number of feet times $0.87
total_cost = feet * 0.87

# Display the calculated information and company name
print("Company Name:", company_name)
print("Total Cost: $", format(total_cost, ".2f"))
