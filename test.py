import json

# Load the JSON file
with open("C:/Users/abdon/Desktop/Datasets/ai2d/categories.json", "r") as file:
    data = json.load(file)  # Load JSON as a dictionary

# Extract unique classes
unique_classes = set(data.values())  # Get all unique values (class names)

# Convert to a sorted list (optional)
unique_classes = sorted(unique_classes)

# Print or save the results
print("Unique Classes:", unique_classes)

# Save to a file (optional)
with open("unique_classes.txt", "w") as output:
    output.write("\n".join(unique_classes))
