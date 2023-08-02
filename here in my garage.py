print("Welcome to the Virtual Garage")
class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage} miles")

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, num_doors):
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

class Pickup(Vehicle):
    def __init__(self, make, model, year, mileage, bed_size):
        super().__init__(make, model, year, mileage)
        self.bed_size = bed_size

    def display_info(self):
        super().display_info()
        print(f"Bed Size: {self.bed_size} feet")


def create_car():
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    year = input("Enter the car's year: ")
    mileage = input("Enter the car's mileage: ")
    num_doors = input("Enter the number of doors: ")
    return Car(make, model, year, mileage, num_doors)


def create_pickup():
    make = input("Enter the pickup's make: ")
    model = input("Enter the pickup's model: ")
    year = input("Enter the pickup's year: ")
    mileage = input("Enter the pickup's mileage: ")
    bed_size = input("Enter the pickup's bed size (in feet): ")
    return Pickup(make, model, year, mileage, bed_size)


def main():
    garage = []

    while True:
        print("\n1. Add a Car")
        print("2. Add a Pickup")
        print("3. Display Garage")
        print("4. Exit")

        choice = input("Please input a number corresponding to the above choices: ")

        if choice == '1':
            car = create_car()
            garage.append(car)
            print("Car added to the garage.")
        elif choice == '2':
            pickup = create_pickup()
            garage.append(pickup)
            print("Pickup added to the garage.")
        elif choice == '3':
            if not garage:
                print("Garage is empty.")
            else:
                print("\nGarage Contents:")
                for vehicle in garage:
                    vehicle.display_info()
        elif choice == '4':
            print("Thank you for using the Virtual Garage.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
