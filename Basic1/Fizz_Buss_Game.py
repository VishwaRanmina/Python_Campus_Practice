num = 1
while (num <= 100):
    
    if (num % 5 == 0 and num % 3 == 0):
        print("FizzBuss")
    
    if(num % 5 == 0):
        print("Buss")
    if(num % 3 == 0):
        print("Fizz")
    else:
        print(num)
        
    num = num + 1