print("Hello, and welcome to the miles to kilometers calculator!")

def convert_miles_to_kilometers(miles):
  kilometers = miles * 1.60934
  return kilometers
miles = float(input("Enter the number of miles driven:"))
kilometers = convert_miles_to_kilometers(miles)

print(f"Total miles driven: {miles}")
print(f"Total kilometers driven: {kilometers}")
print("Thank you for using this converter! Have a nice day!")