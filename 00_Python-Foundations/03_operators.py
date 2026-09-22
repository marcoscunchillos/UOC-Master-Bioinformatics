# Day 3 - 30DaysOfPython Challenge
# Operators
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
#Use a logical negation (not) to check that the substring 'gen' is NOT present in both words simultaneously.
print("gen"not in "carcinogen" and "gen" not in "mutagen")
#Find the length of the word 'biomarker', convert that numeric value to a float, and subsequently convert it to a string.
print(str(float(len("biomarker"))))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a laboratory sample ID (e.g., 142) is even or odd using Python?
print("Even" if int(input("Enter integer: ")) % 2 == 0 else "Odd")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3==int(2.7))
#Check if the type of '10' is equal to the type of 10.
print(type("10")==type(10))
#Check if converting the string '9.8' to a float and then to an integer results in 10.
print(int(float("9.8"))==10)
#Write a script that prompts the user to enter the hours of exposure to an agent and the cumulative 
# dose rate (µg/hour). Calculate the total biological dose received.
hours_exposure = float(input("Enter hours of exposure to BPA: "))
dose_rate = float(input("Enter cumulative dose rate (µg/hour): "))
total_biological_dose = hours_exposure * dose_rate
print(f"Total biological dose received: {total_biological_dose} µg")
#Write a script that prompts the user to enter the number of years residing near a chronic pollution 
# source. Calculate the total number of seconds of exposure (assuming a 100-year lifespan for the model).
print(f"You have been exposed for {int(input("Enter number of years you have lived here: ")) * 365 *  24 *  60 *  60} seconds")
#Write a Python script that displays the following multiplicative cell growth table:
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
for n in range(1, 6): print(n, 1, n, n**2, n**3)
