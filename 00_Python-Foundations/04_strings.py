# Day 4 - 30DaysOfPython Challenge
# Strings & Text Parsing

# 1. Concatenate the strings 'Exposomics', 'And', 'Cancer', 'Epidemiology' to a single string.
print('Exposomics'+'And'+'Cancer'+'Epidemiology')
# 2. Concatenate the strings 'Environmental', 'Health', 'Data' to a single string.
print('Environmental'+'Health'+'Data')
# 3. Declare a variable named research_center and assign it the initial value "Swiss Institute of Environmental Health".
research_center='Swiss Institute of Environmental Health'
# 4. Print the variable research_center using print().
print(research_center)
# 5. Print the length of the research_center string using len() and print().
print(len(research_center))
# 6. Change all characters in research_center to uppercase letters using upper().
print(research_center.upper())
# 7. Change all characters in research_center to lowercase letters using lower().
print(research_center.lower())
# 8. Use capitalize(), title(), and swapcase() methods to format the value "exposomics and cancer research".
text_8="exposomics and cancer research"
print(f"{text_8.capitalize()}\n"f"{text_8.title()}\n"f"{text_8.swapcase()}")
# 9. Slice out the first word of the string "Environmental Exposure Pathways".
text_9="Environmental Exposure Pathways"
first_word = text_9[0:13]
# 10. Check if the string "Environmental Exposure Pathways" contains the word "Exposure" using index() or find().
print(text_9.find("Exposure"))
# 11. Replace the word "Toxicology" with "Exposomics" in the string "Environmental Toxicology Framework".
text_11="Environmental Toxicology Framework"
print(text_11.replace("Toxicology","Exposomics"))
# 12. Change "Analysis of Legacy Pollutants" to "Analysis of Emerging Contaminants" using the replace() method.
text_12="Analysis of Legacy Pollutants"
print(text_12.replace("Legacy Pollutants","Emerging Contaminants"))
# 13. Split the string "Swiss Tropical and Public Health Institute" using space as the separator.
text_13="Swiss Tropical and Public Health Institute"
print(text_13.split(" "))
# 14. Split the string "PFAS, Microplastics, Heavy_Metals, Pesticides, Phthalates, Benzene" at the comma.
text_14="PFAS, Microplastics, Heavy_Metals, Pesticides, Phthalates, Benzene"
print(text_14.split(","))
# 15. What is the character at index 0 in the string "Exposomics"?
print("Exposomics"[0])
# 16. What is the last index of the string "Environmental Health Science"?
print("Environmental Health Science"[-1])
# 17. What character is at index 10 in the string "Biomonitoring Cohort"?
print("Biomonitoring Cohort"[10])
# 18. Create an acronym/abbreviation for "Swiss Tropical Public Health".
text_18="Swiss Tropical Public Health".split()
a,b,c,d=text_18
print(f"{a[0]},{b[0]},{c[0]},{d[0]}")
# 19. Create an acronym/abbreviation for "Environmental Health Data Science".
text_19="Environmental Health Data Science".split()
print(f"{text_19[0][0]},{text_19[1][0]},{text_19[2][0]},{text_19[3][0]}")
# 20. Use index to determine the position of the first occurrence of 'E' in "Environmental Exposomics".
print("Environmental Exposomics".index("E"))
# 21. Use index to determine the position of the first occurrence of 'P' in "PFAS Contamination".
print("PFAS Contamination".index("P"))
# 22. Use rfind to determine the position of the last occurrence of 'a' in "Public Health Data Analysis".
print("Public Health Data Analysis".rfind("a"))
# 23. Use find() to locate the position of the first occurrence of the word 'exposure' in:
#     "High risk exposure occurs when exposure levels exceed safety limits because exposure is persistent"
print("High risk exposure occurs when exposure levels exceed safety limits because exposure is persistent".find("exposure"))
# 24. Use rindex() to find the position of the last occurrence of the word 'exposure' in the sentence above.
print("High risk exposure occurs when exposure levels exceed safety limits because exposure is persistent".rindex("exposure"))
# 25. Slice out the phrase 'exposure levels exceed safety limits' from the sentence above.
phrase_to_remove = "exposure levels exceed safety limits"
start_pos = sentence.find(phrase_to_remove)
end_pos = start_pos + len(phrase_to_remove)
sentence_sliced = sentence[:start_pos].strip() + " " + sentence[end_pos:].strip()
print("25. Sliced sentence:", sentence_sliced)# 26. Does the string "Exposomics Data Science" start with the substring "Exposomics"?
# 26. Does the string "Exposomics Data Science" end with the substring "science"?
text_26 = "Exposomics Data Science"
print(text_26.endswith("science"))
# 27. Strip left and right trailing spaces from the string: '   Toxicological Screening Unit     '.
text_27 = '   Toxicological Screening Unit     '
print(text_27.strip())
# 28. Join the list ['PFAS', 'BPA', 'Phthalates', 'Lead', 'Arsenic'] into a single string separated by '# '.
list_28=['PFAS', 'BPA', 'Phthalates', 'Lead', 'Arsenic']
print('# '.join(list_28))
# 29. Use the tab escape sequence (\t) to format a multi-column table containing: 
# Sample_ID, Biomarker, Concentration, and Status.
print("Sample_ID\tBiomarker\tConcentration\tStatus")
print("1\t25\t234\t45")
print("2\t45\t424\t53")
# 30. Use f-string formatting to display the circle area / exposure boundary formula:
radius = 15
area = 3.14159 * radius ** 2
print(f"The exposure risk zone radius is {radius} meters with an area of {area:.2f} square meters.")
