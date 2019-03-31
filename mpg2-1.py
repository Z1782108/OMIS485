#!/usr/bin/env python3

print("The Miles Per Gallon application")
print()

miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

#mpg = miles_driven / gallons_used
#mpg = round(mpg, 2)
mpg = round((miles_driven / gallons_used), 1)
total_gas_cost = round(gallons_used * cost_per_gallon, 1)
cost_per_mile = round(total_gas_cost / miles_driven, 1)
                
print()
print("Miles Per Gallon:\t", mpg,
      "\nTotal Gas Cost:\t\t", total_gas_cost,
      "\nCost Per Mile:\t\t", cost_per_mile)
print()
print("See you later!")


