class Factorial:
    """_summary_
    Calculate Factorial of a number
    """    
    def calculate(self, number):
        if number == 1:
            return number
    
        result = 1
        for n in range(1,number + 1):
            result = result * n
        return result
