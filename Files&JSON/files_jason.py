import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Task 1 — Read the inventory
'''Explanation: 
1. Opens the file inventory.json in read mode using WITH block to ensure file closes automatically 
and prevents memory leaks. 
2. Reads JSON data from the file and converts it into Python objects and store it in inventory variable
3. len() counts the number of items in the list and print the total number books currently in the file'''

with open("inventory.json", "r") as file:
    inventory = json.load(file)
print(f"Total number of books: {len(inventory)}")

# Task 2 — Update and save
'''Explanation:
1. append() adds an element to the end of the list.
2. Using a WITH block opens the file in write mode to override the exisiting file
3. json.dump() writes Python data into a JSON file with an indentation of 4 spaces'''

inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# Task 3 — Display the updated inventory
'''Explanation:
1. Opens the file inventory.json in read mode using WITH block to ensure file closes automatically 
and prevents memory leaks. 
2. Reads JSON data from the file and converts it into Python objects and store it in updated_inventory variable
3. Using a for loop to loop through each item in the list
4. Print the item details in the given format'''

with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")