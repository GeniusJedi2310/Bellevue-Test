print("Hello, welcome to Anon E. Mouse's Fiber Optic Cable Installation Calculator! ")

company_name = input("Before we begin, please enter your company name here: ")

feet = float(input("Now then, please enter the number of feet of fiber optic you need to be installed here: "))

if feet < 100: 
  total_cost = feet * 0.87
elif feet < 250:
  total_cost = feet * 0.80
elif feet < 500:
  total_cost = feet * 0.70
elif feet > 500:
  total_cost = feet * 0.50
print("Here's your total cost")
print("Company Name:", company_name)
print("Total Cost: $", format(total_cost, ".2f"))

print("Thank you for using Anon E. Mouse's Fiber Optic Installation Calculator")