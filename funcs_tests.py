# Project 2 - Moonlander
# Author: Al Gillani
# Version: 3
# Instructor: Workman
import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 5), 0.00)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 9), 1.296)
      
   def test_update_alt1(self):
      self.assertEqual(updateAltitude(1000, -5, -6), 992)
   def test_update_alt2(self):
      self.assertEqual(updateAltitude(1, -5, -6), -7.00)

   def test_update_vel1(self):
      self.assertEqual(updateVelocity(-5, -3), -8.00)
   def test_update_vel2(self):
      self.assertEqual(updateVelocity(3, 5), 8.00)
   
   def test_update_fue1(self):
      self.assertEqual(updateFuel(7, 3), 4)
   def test_update_fue2(self):
      self.assertEqual(updateFuel(5, 6), 0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

