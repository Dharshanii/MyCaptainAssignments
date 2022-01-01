def fibonacci(n):
    a = 0
    b = 1
     

    if n < 0:
        print("Incorrect input")
         

    elif n == 0:
        return 0
       
    elif n == 1:
        return b
    else:
        print(a)
        print(b)
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(b)
n= int(input('Enter the number of terms: '))
print(fibonacci(n-1))