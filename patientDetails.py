"""
This program is mesnt to accept patient details to help in social distancing
"""
print("Welcome to our health care facility ")
print("Please enter the following details, a nurse will attend to you shortly")


#Accepting inputs from patient
pName = input("Please enter your name: ")

pAge = input("Please enter your age: ")

pResidence = input("Please enter your place of residence: ")

pSymptoms = input("Please enter all observed symptoms with each separated from the other with a comma: ")


#Displaying inputs from patient
print("Patient name: " + pName)
print("Patient's age: " + pAge)
print("Patient's place of residence: " + pResidence)
print("Symptoms: " +"( " + pSymptoms +" )")