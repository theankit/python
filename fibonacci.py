# Fibonacci series for printing the values until "100"

def fib(n):     # defining the function
    a=0         # initially first value=1
    b=1         # initially first value=2

    if n<=0:    # checking for positive integer value of n
        print("Please enter positive integer value...!!!")

    elif n==1:  # if n=1 only
        print(a)

    else:       # if n>1
        print(a)
        print(b)

        for i in range(3,n+1):      # when n>2
            c=a+b
            a=b
            b=c
            if c<=100:              # when we want value of c<=100 otherwise just "print(c), avoid if-esle here"
                print(c)
            else:
                break               # when value of c>100, stop printing


x=int(input("enter the desired value= "))       # asking the no of values in the series
fib(x)                                          # calling function fib()