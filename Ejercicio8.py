weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

imc = weight / height**2

if imc < 18.5:
    print(f"Underweight, your imc is: {imc}")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Ideal weight, your imc is: {imc}")
elif imc >= 25 and imc <= 29.9:
    print(f"Overweight, your imc is: {imc}")
else:
    print(f"Obese, your imc is: {imc}")