'''
This file contains the BMICalculator class.
'''
class BMICalculator:
    def calculate_bmi(self, weight, height):
        if height <= 0:
            raise ValueError("Height cannot be zero or negative.")
        return weight / (height ** 2)