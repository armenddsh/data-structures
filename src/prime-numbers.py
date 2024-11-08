

def is_prime(number):
    if number <= 1:
        return False
        
    for n in range(2, number):
        if number % n == 0:
            return False
            
    return True
    
    
for i in range(10000):
    result = is_prime(i)
    if result:
        print(f"Number {i} Is Prime Number")
    else:
        print(f"Number {i} Is Not Prime Number")
    
