# Input PNR number
pnr = input("Enter PNR Number: ")
# Check palindrome
if pnr == pnr[::-1]:
    print("The PNR Number is a Palindrome.")
else:
    print("The PNR Number is NOT a Palindrome.")
# Digit frequency
print("Digit Frequency in PNR Number:")
for d in range(10):
    count = pnr.count(str(d))
    if count > 0:
        time_word = "time" if count == 1 else "times"
        print(f"Digit {d}: {count} {time_word}")
