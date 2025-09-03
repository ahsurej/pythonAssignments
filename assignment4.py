# Ask the user for a filenamee
filename = input("Enter the name of the file to read: ")

try:
    # Try reading the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to '{new_filename}'.")

except FileNotFoundError:
    print(" Error: File not found.")
except IOError:
    print(" Error: Cannot read the file.")
