while True:
    num_1 = int(input("Enter First Number :"))
    num_2 = int(input("Enter Second Number :"))
    operator = input("Enter Operator :")

    if(operator == "+"):
        print("Result :",(num_1 + num_2))
        
    elif(operator == "-"):
        print("Result :",(num_1 - num_2))
        
    elif(operator == "*"):
        print("Result :",(num_1 * num_2))
        
    elif(operator == "/"):
        if(num_2 == 0):
            print("Can't be devide by 0")
        else:
            print("Result :",(num_1 / num_2))
        
    elif(operator == "%"):
        print("Result :",(num_1 % num_2)) 
    
    elif(operator == "**"):
        print("Result :",(num_1 ** num_2)) 
    
    elif(operator == "//"):
        if(num_2 == 0):
            print("Can't be devide by 0")
        else:
            print("Result :",(num_1 // num_2))  
        
    else:
        print("Enter Valid numbers Or Operator")
        

    