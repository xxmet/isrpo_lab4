import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)
        
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(1000), 2000 * math.pi)

if __name__ == '__main__':
    unittest.main()