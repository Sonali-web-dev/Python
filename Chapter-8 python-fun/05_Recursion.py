#Recursion-->
''' Factorial(0) = 1
    Factorial(1) = 1
    Factorial(2) = 1 x 2
    Factorial(3) = 1 X 2 X 3
    Factorial(4) = 1 x 2 x 3 x 4
    Factorial(5) = 1 x 2 x 3 x 4 x 5
    factorial(n) = n X n-1 X.....3 X 2 x 1
    factorial(n) = n * factorial(n-1)
    
    '''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number:"))
print(f"The factorial of this number is :{factorial(n)}") 