import unittest
from Sum import sum

class test_sum(unittest.TestCase):
  
  def test_sum(self):
    self.assertEquals(sum(2,3),5)
    

if __name__ == "__main__":
    unittest.main()