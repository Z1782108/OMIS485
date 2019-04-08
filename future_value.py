#!/usr/bin/env python3
        
import validation as v
               
def calculate_future_value(monthly_investment, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    #FV Calculate
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # asking for inputs
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        choice = input("Would you like to continue? (y/n): ")
        print()

    print("See you later!!")
    
if __name__ == "__main__":
    main()
