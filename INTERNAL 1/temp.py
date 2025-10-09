temps = [32, 34, 29, 31, 28, 33, 35, 36, 30, 27, 31, 32, 34, 37]
average_temp = sum(temps) / len(temps)
days_above_avg = len([temp for temp in temps if temp > average_temp])
temp_difference = max(temps) - min(temps)
# Display the results
print(f"Average Temperature: {average_temp:.1f}")
print(f"Days above average: {days_above_avg}")
print(f"Temperature difference: {temp_difference}")
