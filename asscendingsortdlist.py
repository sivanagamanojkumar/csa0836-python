
elements = input("Enter words separated by space: ").split()
sorted_elements = sorted(elements, key=len)
print("Sorted list according to length of elements:", sorted_elements)
