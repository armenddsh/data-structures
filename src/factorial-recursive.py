import sys

sys.setrecursionlimit(1500)

class Factorial:
    """_summary_
    Calculate Factorial of a number
    """    
    def calculate(self, number):
        if number == 1:
            return number
        return number * self.calculate(number - 1)
