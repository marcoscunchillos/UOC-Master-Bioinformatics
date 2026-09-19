# Day 2 - 30DaysOfPython Challenge
# Variables & Built-in functions

# --- Exercises: Level 1 --- 
# #Declare a cancer_type variable and assign a value to it 
cancer_type = "Lung Cancer"
#Declare a primary_gene variable and assign a value to it 
primary_gene= "TP53"
#Declare a full_disease_name variable and assign a value to it.
full_disease_name = "Lung Cancer with TP53 mutation"
#Declare a research_country variable and assign a value to it.
research_country = "Spain"
#Declare a cohort_city variable and assign a value to it.
cohort_city = "Alicante"
#Declare a patient_age variable and assign a value to it.
patient_age = 65
#Declare a diagnosis_year variable and assign a value to it.
diagnosis_year = 2020
#Declare a variable is_carcinogenic and assign a boolean value to it.
is_carcinogenic = True
#Declare a variable is_metastatic and assign a boolean value to it.
is_metastatic = True
#Declare a variable is_treatment_active and assign a boolean value to it.
is_treatment_active = True
#Declare multiple variables on one line for environmental risk factors 
# (carcinogen_name, exposure_level_ppm, pH_level).
carcinogen_name,exposure_level_ppm,pH_level = 'Benzo[a]pyrene', 0.082, 7.35


# --- Exercises: Level 2 ---
#Check the data type of two of your variables using the type() built-in function.
print(type(cancer_type))
print(type(primary_gene))
#Using the len() built-in function, find the length of your cancer_type.
print(len(cancer_type))
#Compare the length of your cancer_type and your primary_gene.
print(len(cancer_type)>len(primary_gene))
#Declare 5 as num_one and 4 as num_two.
num_one,num_two=5,4
#Subtract num_two from num_one and assign the value to a variable diff.
diff = num_two-num_one
#Multiply num_two and num_one and assign the value to a variable product.
product = num_two*num_one
#Divide num_one by num_two and assign the value to a variable division.
division = num_one/num_two
#Calculate num_one to the power of num_two and assign the value to a variable exp.
exp = num_one**num_two
#The radius of a tumor dispersion model or cell colony area is 30cm. 
# Calculate the area and assign the value to area_of_circle
import math
area_of_circle = math.pi*(30**2)
#Use the built-in input() function to get cancer_type, primary_gene, research_country, and patient_age from a user 
# and store the values to their corresponding variable names.
cancer_type = input('Enter cancer type: ')
primary_gene = input('Enter primary gene mutation: ')
research_country = input('Enter country of cohort: ')
patient_age = input('Enter patient age: ')