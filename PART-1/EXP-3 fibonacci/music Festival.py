N = int(input("Enter number of seats (N): "))
if N <= 0:
    print("Number of seats must be greater than 0.")
else:
    a, b = 0, 1
    print("Seat arrangement (Fibonacci sequence):")
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
