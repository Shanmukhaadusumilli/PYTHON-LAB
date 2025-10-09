# Read performance values for three trials
t1 = float(input("Enter performance in Trial 1:"))
t2 = float(input("Enter performance in Trial 2: "))
t3 = float(input("Enter performance in Trial 3: "))
# Store in list and sort
trials = [t1, t2, t3]
trials.sort(reverse=True)
# Average of best two
average = (trials[0] + trials[1]) / 2
print("Average of best two performances:", average)
