#!/usr/bin/env python
# coding: utf-8

# In[26]:



#Edwards Meliton IS_211

def convert(fromUnit, toUnit, value):

    fromTemperatureUnit = False
    fromDistanceUnit = False
    toTemperatureUnit = False
    toDistanceUnit = False

    if fromUnit == "Fahrenheit" or fromUnit == "Kelvin" or fromUnit == "Celcius":
        fromTemperatureUnit = True
    if fromUnit == "Meters" or fromUnit == "Yards" or fromUnit == "Miles":
        fromDistanceUnit = True
    if toUnit == "Fahrenheit" or toUnit == "Kelvin" or toUnit == "Celcius":
        toTemperatureUnit = True
    if toUnit == "Meters" or toUnit == "Yards" or toUnit == "Miles":
        toDistanceUnit = True


    if fromTemperatureUnit and toTemperatureUnit:
        celcius = value
        if fromUnit == "Kelvin":
            celcius = value - 273.15
        if fromUnit == "Fahrenheit":
            celcius = ((value-32.0)*(5.0/9.0))

        kelvin = celcius + 273.15
        fahrenheit = (celcius*(9.0/5.0))+32

        if toUnit == "Fahrenheit": return fahrenheit
        if toUnit == "Celcius": return celcius
        if toUnit == "Kelvin": return kelvin

    elif fromDistanceUnit and toDistanceUnit:
        miles = value
        if fromUnit == "Yards":
            miles = value/1760.0
        if fromUnit == "Meters":
            miles = value/1609.344

        yards = miles*1760.0
        meters = miles*1609.344

        if toUnit == "Miles": return miles
        if toUnit == "Yards": return yards
        if toUnit == "Meters": return meters

    else:
        raise ConversionNotPossibleException("Conversion not possible please check your units")

convert('Celcius', 'Fahrenheit', 10)


# In[ ]:





# In[ ]:





# In[ ]:




