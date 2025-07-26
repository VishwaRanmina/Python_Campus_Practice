while True:
    height = float(input("Enter Your Height (Meters) : "))
    if(height < 1.2):
        print("Not Eligible")
        break
    elif(height >= 300):
        print("Enter valid Height")
    
    age = int(input("Enter Your Age : "))
    ticket_price = 1000
  
    if (age < 18 ):
        price = ticket_price - ticket_price * (20 / 100)
        print(f"Ticket Price is {price}") 

                
    elif(age <= 0 or age >= 120):
        print("Enter Valid Age!")
        
    elif(age >= 60):
        price = ticket_price - ticket_price * (60 / 100)
        print(f"Ticket Price is {price}")

        
    else:
        print(f"Your Ticket price is {ticket_price}")
        price = ticket_price
        
    to_continue = input("Do you Want to continue? (y/n)")
    
    if(to_continue == "n"):
        print("Programme Exited")
        exit()