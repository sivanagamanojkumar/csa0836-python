statement = input("Enter a statement: ")
special_characters = "!@#$%^&*()-_+=[]{}|;:',.<>?/\\"
count = 0
for char in statement:
    if char in special_characters:
        count += 1
print("Number of special characters", count)
