# Input student details
name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

# Validate marks
if (mark1 < 0 or mark1 > 100 or
    mark2 < 0 or mark2 > 100 or
    mark3 < 0 or mark3 > 100):
    print("Error: Marks must be between 0 and 100")
    exit()

# Calculate total and percentage
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Determine grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Display results
print("\nStudent Name:", name)
print("Total:", total, "/300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

