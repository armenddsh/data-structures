
class Fibonacci:
    """_summary_
        Calculate Fibonacci
        F(n) = F(n-2)+F(n-1)
    """    
    def calculate(self, number):
        if number == 0 or number == 1:
            return number

        return self.calculate(number - 2) + self.calculate(number - 1)
