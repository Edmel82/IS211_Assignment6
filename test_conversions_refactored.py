import unittest
from conversion_refactored import convert, ConversionNotPossible

class TestConversionsRefactored(unittest.TestCase):
    
    def test_temperature_conversions(self):
        self.assertEqual(convert('celsius', 'fahrenheit', 100), 212)
        self.assertEqual(convert('celsius', 'kelvin', 100), 373.15)
        self.assertEqual(convert('fahrenheit', 'celsius', 212), 100)
        self.assertEqual(convert('fahrenheit', 'kelvin', 32), 273.15)
        self.assertEqual(convert('kelvin', 'celsius', 273.15), 0)
        self.assertEqual(convert('kelvin', 'fahrenheit', 273.15), 32)

    def test_distance_conversions(self):
        self.assertEqual(convert('miles', 'meters', 1), 1609.34)
        self.assertEqual(convert('miles', 'yards', 1), 1760)
        self.assertEqual(convert('yards', 'meters', 1), 0.9144)
        self.assertEqual(convert('yards', 'miles', 1760), 1)
        self.assertEqual(convert('meters', 'yards', 0.9144), 1)
        self.assertEqual(convert('meters', 'miles', 1609.34), 1)

    def test_identity_conversions(self):
        units = ['celsius', 'fahrenheit', 'kelvin', 'miles', 'yards', 'meters']
        for unit in units:
            self.assertEqual(convert(unit, unit, 123.456), 123.456)

    def test_invalid_conversions(self):
        with self.assertRaises(ConversionNotPossible):
            convert('celsius', 'meters', 100)
        with self.assertRaises(ConversionNotPossible):
            convert('miles', 'fahrenheit', 100)

if __name__ == '__main__':
    unittest.main()
