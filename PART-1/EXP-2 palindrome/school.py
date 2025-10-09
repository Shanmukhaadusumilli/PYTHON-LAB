# Input roll number
roll_no = input("Enter Roll Number: ")
# Check palindrome
if roll_no == roll_no[::-1]:
    print("The Roll Number is a Palindrome.")
else:
    print("The Roll Number is NOT a Palindrome.")
# Digit frequency
print("Digit Frequency in Roll Number:")
for d in range(10):
    count = roll_no.count(str(d))
    if count> 0:
        print(f"Digit {d}: {count} times")
