try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error!File does not exist")      

with open("clients.txt", "r") as file:
    for line in file:
        try:
            parts = line.strip().split(",")
            name = parts[0].strip()
            amount = parts[1].strip()
            print(f"{name} owes {amount}")
        except IndexError:
            print(f"Skipping bad value: {line.strip()}")