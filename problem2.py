'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Find the average amount of chicken to be distributed to the students in Mr Fabroa's class and the remainder of the chicken which will go to Mr Fabroa himself 

Author:	Young.A

Created:	7/12/2020
-----------------------------------------------------------------------------
'''

print("****Welcome to the Popeyes Chicken Distrubator Program****")

# Input the amount of chicken and students
students = int(input("How many students are in Mr. Fabroa's class: ")) 
chicken = int(input("How many Popeyes chicken are there: "))

# Calculate the average amount of chicken and remainder
average_chicken = chicken//students
remainder_chicken = chicken%students

# Output the chicken each student and Mr Fabroa will get
print("Each student in the class will get " +str(average_chicken)+ " Popeye(s) chicken and Mr Fabroa will get " +str(remainder_chicken)+ " Popeye(s) chicken") 
