import unittest
from Area import Area

class TestArea(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(Area.circle(1), 3.141592653589793)
        self.assertAlmostEqual(Area.circle(0), 0)
        with self.assertRaises(ValueError):
            Area.circle(-1)

    def test_rectangle(self):
        self.assertEqual(Area.rectangle(2, 3), 6)
        self.assertEqual(Area.rectangle(0, 5), 0)
        with self.assertRaises(ValueError):
            Area.rectangle(-1, 2)

    def test_square(self):
        self.assertEqual(Area.square(4), 16)
        self.assertEqual(Area.square(0), 0)
        with self.assertRaises(ValueError):
            Area.square(-1)

    def test_triangle(self):
        self.assertEqual(Area.triangle(3, 4), 6)
        self.assertEqual(Area.triangle(0, 5), 0)
        with self.assertRaises(ValueError):
            Area.triangle(-1, 4)
        with self.assertRaises(ValueError):
            Area.triangle(3, -1)

if __name__ == "__main__":
    unittest.main()
