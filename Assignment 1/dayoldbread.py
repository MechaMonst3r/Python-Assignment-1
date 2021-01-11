# Name: Luke Bowden
# Student Number: t00040951
# Lab Number: 1
# Date: 2020-09-16
# Description: Takes in input from a user who wishes to buy old
#              bread at a discount price and produces the total.


#Defining Constants and variables.
BREADCOST = 3.49;
DISCOUNT = 0.6;
totalBread = 0.0;
totalDiscount = 0.0;
totalSale = 0.0;

#Gets input from user.
userInput = float(input("Enter number of loaves of old bread you want to buy:\n"));

#Does caluclations to get the total cost of bread, the discount, and applies the proper amount to the sale total.
totalBread = userInput * BREADCOST;
totalDiscount = totalBread * DISCOUNT;
totalSale = totalBread - totalDiscount;

#Prints the results to the user and formats it to the second decimal.
print("Cost per loaf: $" + "{:.2f}".format(totalBread));
print("Amount you save: $" + "{:.2f}".format(totalDiscount));
print("Total price: $" + "{:.2f}".format(totalSale));


