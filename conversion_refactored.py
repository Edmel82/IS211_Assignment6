class ConversionNotPossible(Exception):
    pass

def convert(from_unit: str, to_unit: str, value: float) -> float:
    conversions = {
        'celsius': {'fahrenheit': lambda x: x * 9/5 + 32, 'kelvin': lambda x: x + 273.15, 'celsius': lambda x: x},
        'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15, 'fahrenheit': lambda x: x},
        'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32, 'kelvin': lambda x: x},
        'miles': {'meters': lambda x: x * 1609.34, 'yards': lambda x: x * 1760, 'miles': lambda x: x},
        'yards': {'meters': lambda x: x * 0.9144, 'miles': lambda x: x / 1760, 'yards': lambda x: x},
        'meters': {'yards': lambda x: x / 0.9144, 'miles': lambda x: x / 1609.34, 'meters': lambda x: x}
    }
    
    try:
        return conversions[from_unit][to_unit](value)
    except KeyError:
        raise ConversionNotPossible(f"Conversion from {from_unit} to {to_unit} is not possible")

