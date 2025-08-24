def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    print("Your BMI:", bmi)
    print("Category:", bmi_category(bmi))
except ValueError:
    print("Please enter valid numbers")
