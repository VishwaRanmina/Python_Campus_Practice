num = 1
while (num <= 100):
    
    if (num % 5 == 0 and num % 3 == 0):
        print("FizzBuss")
    
    elif(num % 5 == 0):
        print("Buss")
        
    elif(num % 3 == 0):
        print("Fizz")
        
    else:
        print(num)
        
    num = num + 1