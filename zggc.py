# Create a list of fruits
fruits = ["apple", "banana", "mango", "orange"]

# Print the whole list
print("Fruit list:", fruits)

# Access individual items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a new fruit
fruits.append("grape")
print("After adding grape:", fruits)

# Remove a fruit
fruits.remove("banana")
print("After removing banana:", fruits)

# Loop through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)
