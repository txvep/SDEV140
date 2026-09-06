"""
Write a program that inputs a score from zero to 100.  Use If statements to calculate grade on a ten point scale.

90-100   A

80-89     B

70-79     C

60-69     D

<60         F

"""

score = float(input("Enter the score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade is {grade}.")
