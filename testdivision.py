import unittest
from division import divide

class test_division(unittest.TestCase):
    
    def test_division(self):
        self.assertEquals(divide(4,2),2)
        
    def test_negative_division(self):
        self.assertEquals(divide(-9,-3),3)
        
    def test_float_division(self):
        self.assertEquals(divide(6.25,2.5),2.5)
        
    def test_for_string(self):
        self.assertEqual(divide("one",2), "Has to be an integer")
        
    def test_division_by_zero(self):
      try:
        (4,0)
        
      except ZeroDivisionError:
          
          self.fail("Cannot divide by 0")
    
        

        
        
if __name__ == '__main__':
    unittest.main()