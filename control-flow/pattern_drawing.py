size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Please enter a positive integer for the pattern size.")
else:
    row_count = 0
    while row_count <size:
        for _ in range(size):
            print("*", end='')
        print()
        row_count += 1
