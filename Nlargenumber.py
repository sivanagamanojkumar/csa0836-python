lst = [14, 67, 48, 23, 5, 62]
N = int(input("Enter the value of N to find the Nth largest number: "))
sorted_list = sorted(lst, reverse=True)

if 0 < N <= len(lst):
    nth_largest = sorted_list[N - 1]
    print(f"{N}th Largest number: {nth_largest}")
else:
    print("Invalid input for N.")
