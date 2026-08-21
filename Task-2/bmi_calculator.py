def calculate_bmi(weight, height_m):
    """Calculates BMI and returns the value and category."""
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
        
    return bmi, category

def main():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height_cm = float(input("Enter your height in centimeters (cm): "))
        
        if weight <= 0 or height_cm <= 0:
            print("Weight and height must be positive numbers!")
            return
            
        height_m = height_cm / 100
        bmi, category = calculate_bmi(weight, height_m)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Health Category: {category}")
        
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()
