#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

#Edwards Meliton IS-211

def convertCelsiusToKelvin(number):
    "This is a function that will convert Celcius to Kelvin"
    given_number = float(number)
    default_kelvin = float(273.15)
    c_value = round(given_number + default_kelvin, 5)
    return c_value
    
def convertCelciusToFahrenheit(number):
    "This is a function that will convert Celcius to Fahrenheit"
    given_number = float(number)
    default_fahrenheit = float(32)
    c_value = round((given_number * 9/5) + default_fahrenheit, 5)
    return c_value

def convertFahrenheitToCelcius(number): 
    "This is a function that will convert Fahrenheit to Celcius"
    given_number = float(number)
    default_Celcius = float(32)
    c_value = round((given_number - default_Celcius) * 5/9, 5)
    return c_value

def convertFahrenheitToKelvin(number):
    "This is a function that will convert Fahrenheit to Kelvin"
    given_number = float(number)
    default_Kelvin = float(459.67)
    c_value = round((given_number + default_Kelvin) * 5/9, 5)
    return c_value

def convertKelvinToCelcius(number):
    "This is a function that will convert Kelvin To Celcius"
    given_number = float(number)
    default_Celcius = float(32)
    c_value = round((given_number - default_Celcius), 5)
    return c_value

def convertKelvinToFahrenheit(number):
    "This is a function that will convert Kelvin To Fahrenheit"
    given_number = float(number)
    default_Fahrenheit = float(459.67)
    c_value = round ((given_number - default_Fahrenheit), 5)
    return c_value 



