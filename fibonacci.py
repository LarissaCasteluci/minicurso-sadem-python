

def Fibonacci_append(list_size):
    
    if list_size == 1:
        return 1
    
    sequence =[1, 1]
    
    for k in range(list_size - 2):
        sequence.append(sequence[-1] + sequence[-2])
        
    return sequence


def Fibonacci_recursive(list_size):
    
    if list_size <= 1:
        return list_size
    else:
        return Fibonacci_recursive(list_size-1) + Fibonacci_recursive(list_size-2)
    
    
print(Fibonacci_recursive(10))