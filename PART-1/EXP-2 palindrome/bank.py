# Input transaction ID
txn_id = input("Enter Transaction ID:")
if txn_id == txn_id[::-1]:
    print("The Transaction ID is a Palindrome.")
else:
    print("The Transaction ID is NOT a Palindrome.")
# Count frequency of each digit
print("Digit Frequency:")
for d in range(10):
    count = txn_id.count(str(d))
    if count> 0:
        print(f"Digit {d}: {count} times")
    
