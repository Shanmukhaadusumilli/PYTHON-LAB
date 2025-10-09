# Read the marks of three internal tests
t1 = int(input("Enter marks of Test 1:"))
t2 = int(input("Enter marks of Test 2:"))
t3 = int(input("Enter marks of Test 3:"))
# Store in list and sort
marks = [t1, t2, t3]
marks.sort(reverse=True)
# Take best two and calculate average
average = (marks[0] + marks[1]) / 2
print("Best two test average in Mathematics:", average)
