# Project 2 - Moonlander
# Author: Al Gillani
# Version: 3
# Instructor: Workman

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n\n   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.\n")
   print("   Good luck and may the force be with you!\n")
   
def getFuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   while fuel<1:
      fuel = int(input("ERROR: Amount of fuel must be positive, please try again\nEnter the initial amount of fuel on board the LM (in liters): "))   
   return fuel

def getAltitude():
   altitude = int(input("Enter the initial altitude of the LM (in meters): "))
   while altitude<1 or altitude>9999:
      altitude = int(input("ERROR: Altitude must be between 1 and 9999, inclusive, please try again\nEnter the initial altitude of the LM (in meters): "))
   return altitude

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print("Elapsed Time:" + "%5d" % elapsedTime + " s")
   print("        Fuel:" + "%5d" % fuelAmount + " l")
   print("        Rate:" + "%5d" % fuelRate + " l/s")
   print("    Altitude:" + "%8.2f" % altitude + " m")
   print("    Velocity:" + "%8.2f" % velocity + " m/s\n")

def getFuelRate(currentFuel):
   newFuel = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while newFuel<0 or newFuel>9:
      newFuel = int(input("ERROR: Fuel rate must be between 0 and 9, inclusive\n\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if currentFuel<newFuel:
      return currentFuel

   return newFuel

def updateAcceleration(gravity, fuelRate):
   acceleration = gravity*((fuelRate/5)-1)
   return acceleration
#round 
def updateAltitude(altitude, velocity, acceleration):
   float(altitude)
   float(velocity)
   float(acceleration)
   altitude = altitude + velocity + (acceleration/2)
   return float(altitude)
#round
def updateVelocity(velocity, acceleration):
   float(velocity)
   float(acceleration)
   velocity = velocity + acceleration
   return float(velocity)
#round
def updateFuel(fuel, fuelRate):
   fuel = fuel - fuelRate
   if fuel<0:
      return 0
   else:
      return fuel

def displayLMLandingStatus(velocity):
   float(velocity)
   if velocity<=0 and velocity>=-1:
      print("Status at landing - The eagle has landed!")
   elif velocity<-1 and velocity>-10:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   else :
      print("Status at landing - Ouch - that hurt!")


