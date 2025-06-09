def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = weight / (height ** 2)
    elif unit == 'imperial':
        bmi = 703 * weight / (height ** 2)
    else:
        raise ValueError('Unsupported unit. Use metric or imperial.')
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal Weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    print("Welcome to the BMI Calculator")
    unit = input("Choose unit system (metric/imperial): ").strip().lower()

    if unit == "metric":
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    elif unit == "imperial":
        weight = float(input("Enter your weight in pounds: "))
        height_ft = float(input("Enter your height (feet): "))
        height_in = float(input("Enter your height (inches): "))
        height = (height_ft * 12) + height_in
    else:
        print("Invalid unit. Please restart the program")
        return

    bmi = calculate_bmi(weight, height, unit)
    classification = classify_bmi(bmi)

    print(f"\n Your BMI Is: {bmi:.2f}")
    print(f"Health Classification: {classification}")

main()