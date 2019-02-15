import unittest
import ccolors

class CcolorsTest(unittest.TestCase):
    def test_complete_hex_to_rgb(self):
        hex = "000000"
        (r, g, b) = ccolors.hex_to_rgb(hex)
        self.assertEquals((r, g, b), (0, 0, 0))
        hex = "FF0000"
        (r, g, b) = ccolors.hex_to_rgb(hex)
        self.assertEquals((r, g, b), (255, 0, 0))
        hex = "00FF00"
        (r, g, b) = ccolors.hex_to_rgb(hex)
        self.assertEquals((r, g, b), (0, 255, 0))
        hex = "0000FF"
        (r, g, b) = ccolors.hex_to_rgb(hex)
        self.assertEquals((r, g, b), (0, 0, 255))

if __name__ == "__main__":
    unittest.main()