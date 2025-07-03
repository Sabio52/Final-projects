workingDays = 365
absentDays = int(input("Enter the number of absent days: "))

AttendedDays = workingDays - absentDays
attendancePercentage = (AttendedDays / workingDays) * 100
print(f"You attended {attendancePercentage:.2f} % of the days.")

if attendancePercentage >= 75:
    print("You are eligible for the exam.")

else:
    print("You are not eligible for the exam.")