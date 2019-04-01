
def Fibonacci_recursive(list_size):
    
    if list_size <= 1:
        return list_size
    else:
        return Fibonacci_recursive(list_size-1) + Fibonacci_recursive(list_size-2)
    
    
print(Fibonacci_recursive(10))
