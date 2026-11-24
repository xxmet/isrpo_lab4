import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_standard(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)
        
    def test_perimeter_standard(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test_area_unit(self):
        self.assertAlmostEqual(area(1), math.pi)
        
    def test_perimeter_unit(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        



    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        



    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25 * math.pi)
        
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)

    def test_area_small_float(self):
        self.assertAlmostEqual(area(0.5), 0.25 * math.pi)
        
    def test_perimeter_small_float(self):
        self.assertAlmostEqual(perimeter(0.5), 1 * math.pi)




    def test_area_large(self):
        self.assertAlmostEqual(area(10000), 100000000 * math.pi, places=4)
        
    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(10000), 20000 * math.pi, places=4)




    def test_area_negative(self):
        self.assertAlmostEqual(area(-5), 25 * math.pi)
        
    def test_perimeter_negative(self):
        self.assertAlmostEqual(perimeter(-5), -10 * math.pi)


if __name__ == '__main__':
    unittest.main()