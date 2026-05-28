print("=== BMI Calculator ===")

# User input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# BMI Formula
bmi = weight / (height ** 2)

# Display BMI
print(f"\nYour BMI is: {bmi:.2f}")

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")