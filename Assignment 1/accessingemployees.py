# Name: Luke Bowden
# Student Number: t00040951
# Lab Number: 1
# Date: 2020-09-17
# Description: Takes in input from a user which rates an employee
#              and calcualtes total raise based on rating.

#Setting constants and variables.
RAISE_FACTOR = 2400.00;
UNACCEPT_RATING = 0.0;
ACCEPT_RATING = 0.4;
MERIT_RATING = 0.6;
employeeRaise = 0.00;

#Collecting input from user.
userInput = eval(input("Enter the rating:"));

#While user doesn't provide a valid input, shows error and prompts for input again.
while userInput != UNACCEPT_RATING and userInput != ACCEPT_RATING and userInput != MERIT_RATING:
    print("Invalid rating. Try again.");
    userInput = float(input("Enter the rating:"));

#Calcualtes how much of a raise an employee will get based on the rating.
employeeRaise = userInput * RAISE_FACTOR;
    
#Checks rating and prints if they're Unacceptable, Acceptable, or Meritorious based on that rating.    
if userInput == UNACCEPT_RATING:
    print("Based on that rating, the performance is: Unacceptable.");
        
if userInput == ACCEPT_RATING:
    print("Based on that rating, the performance is: Acceptable.");
        
if userInput == MERIT_RATING:
    print("Based on that rating, the performance is: Meritorius.");
    
#Prints out the total raise the employee will recieve and formats the result to 2 decimal places.    
print("You recieve a raise of $" + "{:.2f}".format(employeeRaise));  
    