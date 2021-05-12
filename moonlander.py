# Project 2 - Moonlander
# Author: Al Gillani
# Version: 3
# Instructor: Workman
from landerFuncs import *

def main():
   totalTime = 0
   curVelocity = 0.0
   curFuelRate = 0
   curAcceleration = 0.0
   showWelcome()
   curAltitude = getAltitude()
   curFuel = getFuel()
   print('\nLM state at retrorocket cutoff')
   displayLMState(totalTime, curAltitude, curVelocity, curFuel, curFuelRate)
   while(curAltitude > 0):
      totalTime += 1
      if curFuel != 0:
         curFuelRate = getFuelRate(curFuel)
         curFuel = updateFuel(curFuel, curFuelRate)
      else:
         curFuelRate = 0
         curFuel = 0
      curAcceleration = updateAcceleration(1.62, curFuelRate)
      curAltitude = updateAltitude(curAltitude, curVelocity, curAcceleration)
      if (curAltitude<0):
         curVelocity = updateVelocity(curVelocity, curAcceleration)   
         break
      curVelocity = updateVelocity(curVelocity, curAcceleration)   
      if curFuel != 0:
         displayLMState(totalTime, round(curAltitude, 2), round(curVelocity, 2), curFuel, curFuelRate)
      else:
         print("OUT OF FUEL - Elapsed Time:" + "%4d" % totalTime + " Altitude:" + "%8.2f" % float(curAltitude) + " Velocity" + "%9.2f" % float(curVelocity))

   print("\nLM state at landing/impact")
   displayLMState(totalTime, 0.00, round(curVelocity, 2), curFuel, curFuelRate)
   print(displayLMLandingStatus(curVelocity))



if __name__ == '__main__':
   main()
   
   