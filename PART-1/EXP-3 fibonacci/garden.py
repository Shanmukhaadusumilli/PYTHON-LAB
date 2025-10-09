N = int(input("Enter N (number of terms for layout design):"))
if N <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    a, b = 0, 1
    print("Fibonacci sequence for garden layout:")

for i in range(N):
    print(a, end="")
    a, b = b, a + b
