n = int(input("Enter Upto which no. you want Fibonacci Series : "))
def fib(x):
    if x == 1:
        print(0)
        return 0
    elif x == 2:
        print(1)
        return 1
    else:
        return fib(x-2)+fib(x-1)
    
print(fib(n))