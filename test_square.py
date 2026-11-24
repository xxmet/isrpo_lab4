import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_standard(self):
        self.assertEqual(area(5), 25)
        
    def test_perimeter_standard(self):
        self.assertEqual(perimeter(5), 20)

    def test_area_unit(self):
        self.assertEqual(area(1), 1)
        
    def test_perimeter_unit(self):
        self.assertEqual(perimeter(1), 4)

        

    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        



    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25)
        
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_area_small_float(self):
        self.assertAlmostEqual(area(0.5), 0.25)
        
    def test_perimeter_small_float(self):
        self.assertAlmostEqual(perimeter(0.5), 2.0)




    def test_area_large(self):
        self.assertEqual(area(10000), 100000000)
        
    def test_perimeter_large(self):
        self.assertEqual(perimeter(10000), 40000)



    def test_area_negative(self):
        self.assertEqual(area(-5), 25)
        
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5), -20)



if __name__ == '__main__':
    unittest.main()