#Kate Blunt
#COP2002
#Project 5
#November 23

from decimal import Decimal
from decimal import ROUND_HALF_UP


def title():    
    print("Aircraft Fuel Calculator")
    print()

def userInput():
    numMile = 0
    numMile = Decimal(input("Distance in nautical miles: "))
    return numMile

def flightTime(miles):
    flyTimeHour = miles//Decimal("120")
    #Because I'm using integer division, the decimal will be truncated so
    #No need for formatting below
    #flyTimeHour = flyTimeHour.quantize(Decimal("1.00")

    flyTimeMinutes = ((miles / Decimal("120") - flyTimeHour)) * 60
    flyTimeMinutes = flyTimeMinutes.quantize(Decimal("1"), ROUND_HALF_UP)

    print("Flight time: " + str(flyTimeHour) +" hour(s) and "
       + str(flyTimeMinutes) + " minute(s)")
    
def requiredFuel(miles):
    #required fuel is theflight time in hours times 8.4 and then add
    #4.2 for half an hour
    fuel = (((miles / Decimal("120")) * Decimal("8.4"))) + Decimal("4.2")
    fuel = fuel.quantize(Decimal("1.0"), ROUND_HALF_UP)
    print("Required fuel: " + str(fuel) + " gallons.")
    

def main ():

    title()
    choice = "y"
    while choice.lower() == "y":

        miles = userInput()
        flightTime(miles)
        requiredFuel(miles)
        print()
        choice = input("Continue? (y/n): ")
        print()
        
    print("Thanks for using this program! Good bye!")









main()
