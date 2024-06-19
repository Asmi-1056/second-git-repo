#Vehicle Rental System

#Creates a class as Vehicle
class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

    def __repr__(self):
        return f"Vehicle(vehicle_id={self.vehicle_id}, make={self.make}, model={self.model}, year={self.year}, category={self.category})"

#Creates a class as VehicleRentalSystem
class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.categories = {}

#To add vehicles to the vehicle rental system
    def add_vehicle(self, vehicle):
        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)
            print(f"The Vehicle '{vehicle.make} {vehicle.model}' is added successfully.")
            self._update_categories(vehicle.category, vehicle)
        else:
            print("The Vehicle already exists in the system.")

#To remove vehicles from the vehicles rental system
    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                print(f"The Vehicle with Id '{vehicle_id}' is removed successfully.")
                self._remove_from_categories(vehicle.category, vehicle)
                return
        print(f"No vehicle found with such Id '{vehicle_id}'.")

#To search vehicles in the vehicle rental system
    def search_vehicles(self, search_term):
        results = []
        for vehicle in self.vehicles:
            if search_term.lower() in vehicle.make.lower() or search_term.lower() in vehicle.model.lower():
                results.append(vehicle)
        if results:
            print(f"Matching vehicles were found for '{search_term}':")
            for vehicle in results:
                print(vehicle)
        else:
            print(f"No matching vehicles were found for '{search_term}'.")

#To list all the vehicles in the vehicle rental system
    def list_vehicles(self):
        if self.vehicles:
            print("List of all the vehicles in the vehicle rental system:")
            for vehicle in self.vehicles:
                print(vehicle)
        else:
            print("No vehicles available in the vehicles rental system.")

#To categorize the vehicles
    def categorize_vehicles(self):
        if self.categories:
            print("Vehicles are categorized by category:")
            for category, vehicles in self.categories.items():
                print(f"- {category}:")
                for vehicle in vehicles:
                    print(vehicle)
        else:
            print("No vehicles present in the system.")

#To update the categories in vehicle rental system
    def _update_categories(self, category, vehicle):
        if category in self.categories:
            self.categories[category].append(vehicle)
        else:
            self.categories[category] = [vehicle]

    def _remove_from_categories(self, category, vehicle):
        if category in self.categories:
            self.categories[category].remove(vehicle)

def vehicle_rental_system():
    rental_system = VehicleRentalSystem()
    choice = None

    while choice != '6':
        print("\n Welcome to the Vehicle Rental System.")
        print("\n Vehicle Rental System Menu:")
        print("1. Add a Vehicle")
        print("2. Remove a Vehicle")
        print("3. Search a Vehicle")
        print("4. List all the Vehicles")
        print("5. Categorize all Vehicles")
        print("6. Exit ")

        choice = input("Enter the choice (1-6): ")

        if choice == '1':
            vehicle_id = input("Enter the Vehicle Id: ")
            make = input("Enter the Vehicle make: ")
            model = input("Enter the Vehicle Model: ")
            year = input("Enter the Vehicle Year: ")
            category = input("Enter the Vehicle Category: ")
            vehicle = Vehicle(vehicle_id, make, model, year, category)
            rental_system.add_vehicle(vehicle)
        elif choice == '2':
            vehicle_id = input("Enter the Vehicle Id to remove: ")
            rental_system.remove_vehicle(vehicle_id)
        elif choice == '3':
            search_term = input("Enter the search term (make or model): ")
            rental_system.search_vehicles(search_term)
        elif choice == '4':
            rental_system.list_vehicles()
        elif choice == '5':
            rental_system.categorize_vehicles()
        elif choice == '6':
            print("Exiting the Vehicle Rental System.Goodbye.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    vehicle_rental_system()

