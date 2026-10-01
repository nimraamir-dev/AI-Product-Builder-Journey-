clients = [
    {"name": "Zaid", "amount": 6000},
    {"name": "Ali", "amount": 8000}
]

# Write initial clients
with open("clients.txt", "w") as file:
    for client in clients:
        file.write(f"{client['name']}, {client['amount']}\n")


# Read existing clients
with open("clients.txt", "r") as file:
    for line in file:
        name, amount = line.strip().split(",")
        print(f"{name} owes {amount}")


# Function to add new client
def add_client(name, amount):
    with open("clients.txt", "a") as file:
        file.write(f"{name}, {amount}\n")


# Add two new clients
add_client("Bilal", 7000)
add_client("Hina", 4000)


# Read file again
with open("clients.txt", "r") as file:
    for line in file:
        name, amount = line.strip().split(",")
        print(f"{name} owes {amount}")