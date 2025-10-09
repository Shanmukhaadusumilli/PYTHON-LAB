N = int(input("Enter N (number of terms): "))
if N <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    a, b = 0, 1
    print("Fibonacci Series up to", N, "terms:")
    for i in range(N):
        print(a, end="")
        a, b = b, a + b
