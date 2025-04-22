receipt = int(input("Enter the the total amount of your purchase: "))

tip = int(input("How much tip percentage would you like to give? 10,15 or 20% "))

if tip == 10:
    tip = 0.10
elif tip == 15:
    tip = 0.15
elif tip == 20:
    tip = 0.20
else:
    print("Please enter a valid tip percentage")

totaltip = receipt * tip

print("Your total tip is $" + str(totaltip))

