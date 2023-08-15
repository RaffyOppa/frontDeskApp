class Customer:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.box_size = None

class StorageArea:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.available_space = max_capacity

class FrontDeskApp:
    def __init__(self):
        self.customers = []
        self.small_area = StorageArea("Small", 10)
        self.medium_area = StorageArea("Medium", 15)
        self.large_area = StorageArea("Large", 20)
        self.transactions = []

    def create_customer(self, first_name, last_name, phone_number):
        new_customer = Customer(first_name, last_name, phone_number)
        self.customers.append(new_customer)
        return new_customer

    def check_availability(self, customer):
        if customer.box_size == "Small" and self.small_area.available_space > 0:
            self.small_area.available_space -= 1
            return True
        elif customer.box_size == "Medium" and self.medium_area.available_space > 0:
            self.medium_area.available_space -= 1
            return True
        elif customer.box_size == "Large" and self.large_area.available_space > 0:
            self.large_area.available_space -= 1
            return True
        else:
            return False

    def store_box(self, customer):
        if self.check_availability(customer):
            self.transactions.append(f"{customer.first_name} {customer.last_name} stored a {customer.box_size} box.")
            return True
        else:
            return False

    def retrieve_box(self, customer):
        if customer.box_size == "Small":
            self.small_area.available_space += 1
        elif customer.box_size == "Medium":
            self.medium_area.available_space += 1
        elif customer.box_size == "Large":
            self.large_area.available_space += 1
        self.transactions.append(f"{customer.first_name} {customer.last_name} retrieved their {customer.box_size} box.")

    def show_customers(self):
        for customer in self.customers:
            print(f"{customer.first_name} {customer.last_name} - {customer.box_size} box")

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def check_available_slots(self):
        print("Available Slots:")
        print(f"Small: {self.small_area.available_space}")
        print(f"Medium: {self.medium_area.available_space}")
        print(f"Large: {self.large_area.available_space}")

app = FrontDeskApp()

while True:
    print("Front Desk App Menu:")
    print("1. Create Customer")
    print("2. Store Box")
    print("3. Retrieve Box")
    print("4. Show Customers")
    print("5. Show Transactions")
    print("6. Check Available Slots")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        customer = app.create_customer(first_name, last_name, phone_number)
        print("Customer created successfully!")

    elif choice == "2":
        app.show_customers()
        customer_index = int(input("Enter the index of the customer: "))
        if 0 <= customer_index < len(app.customers):
            customer = app.customers[customer_index]
            box_size = input("Enter box size (Small, Medium, Large): ")
            customer.box_size = box_size
            if app.store_box(customer):
                print("Box stored successfully!")
            else:
                print("Box cannot be stored due to insufficient space.")

    elif choice == "3":
        app.show_customers()
        customer_index = int(input("Enter the index of the customer: "))
        if 0 <= customer_index < len(app.customers):
            customer = app.customers[customer_index]
            if customer.box_size:
                app.retrieve_box(customer)
                print("Box retrieved successfully!")
            else:
                print("No box associated with this customer.")

    elif choice == "4":
        app.show_customers()

    elif choice == "5":
        app.show_transactions()
        
    elif choice == "6":
        app.check_available_slots() 

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
