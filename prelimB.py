import unittest
class Temperature:

    def __init__(self, kelvin = None, celsius = None, fahrenheit = None):

        values = [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need argument')

        if len(values) > 1:
            raise ValueError('Only one argument')

        if celsius is not None:
            self.kelvin = celsius + 273.15

        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5/9 + 273.15

        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'

#Creating Unittest
class LearnTest(unittest.TestCase):

#Creating 4 Test Case Function
    def test_function1(self):

        test1 = Temperature(celsius = 50)
        self.assert_(test1)
        print('Test 1 = ' + str(test1.kelvin))

    def test_function2(self):

        test2 = Temperature(kelvin = 5)
        self.assert_(test2)
        print('Test 2 = ' + str(test2.kelvin))

    def test_function3(self):

        test3 = Temperature(fahrenheit = 100)
        self.assert_(test3)
        print('Test 3 = ' + str(test3.kelvin))

    def test_function4(self):

        test4 = Temperature(celsius = 32+5)
        self.assert_(test4)
        print('Test 4 = ' + str(test4.kelvin))
if __name__ == "__main__":
    unittest.main()
