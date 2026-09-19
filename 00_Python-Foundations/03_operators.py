#Declare a patient_age as an integer variable.
patient_age = 65
#Declare a patient_height_m as a float variable.
patient_height_m = 1.78
#Declare a variable tissue_impedance that stores a complex number to represent the electrical resistance of a cellular tissue.
tissue_impendance = 150 + 50j
#Write a script that prompts the user to enter the base and height of an environmental exposure zone (triangle) 
# and calculate its impact area (area = 0.5 x b x h).
base = float(input("Enter the base of the exposure zone (in meters/units): "))
height = float(input("Enter the height of the exposure zone (in meters/units): "))
area = 0.5*base*height
print(f"\nThe total impact area of the exposure zone is: {area} square units")
#Write a script that prompts the user to enter side a, side b, and side c of a tissue biopsy (triangle). 
# Calculate the perimeter of the sample (perimeter = a + b + c).
side_a = float(input("Enter the length of the side A of the tissue"))
side_b = float(input("Enter the length of the side B of the tissue"))
side_c = float(input("Enter the length of the side C of the tissue"))
perimeter=side_a+side_b+side_c
print(f"The perimeter of the tissue biopsy is {perimeter}cm")
# Calculate the value of a toxicity threshold y using the formula y = x^2 + 6x + 9. 
# Try different x values to figure out at what x value the toxicity level y is 0.
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    if y == 0:
        print("Solution: y is 0 when x =", x)
else:
    print("No solution in tested range.")
#Find the length of the strings 'carcinogen' and 'mutagen' and make a falsy comparison statement between them.
len("carcinogen") == len("mutagen")
#Use the and operator to check if the substring 'gen' is found simultaneously in both 'carcinogen' and 'mutagen'.
print("gen" in "carcinogen" and "gen" in "mutagen")
#Given the sentence "The exposure to heavy metals causes severe toxicity.", use the in operator to check if the 
# word 'toxicity' is in the sentence.
print('toxicity'in'The exposure to heavy metals causes severetoxicity')
