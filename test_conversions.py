import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestConversions(unittest.TestCase):
    
    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-273.15, 0),
            (25, 298.15),
            (300, 573.15)
        ]
        
        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"Testing {celsius}°C -> {result} K (Expected: {expected} K)")
            self.assertEqual(result, expected)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (25, 77),
            (300, 572)
        ]
        
        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Testing {celsius}°C -> {result} F (Expected: {expected} F)")
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
