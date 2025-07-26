while True:
    salary = float(input("Enter Your Mothly Salary : "))*12

    if(salary <= 1200000):
        tax = 0
        print("YOu Don't need to pay Tax..")
    else:
        if(salary <= 1700000):
            tax = salary - 1200000 * 0.06

        elif(salary <= 2200000):
            tax = 500000 * 0.06 + salary - 1700000 * 0.12

        elif(salary <= 2700000):
            tax = 500000 * 0.06 + 500000 * 0.12 + (salary - 2200000) * 0.18

        elif(salary <= 3200000):
            tax = 500000 * 0.06 + 500000 * 0.18 + 500000*  0.12 + (salary - 2700000) * 0.24
            
        elif(salary <= 3700000):
            tax = 500000 * 0.06 + 500000 * 0.18 + 500000 * 0.12 + 500000 * 0.24 + (salary - 3200000) * 0.30
            
        else:
            tax = 500000 * 0.06 + 500000 * 0.18 + 500000 * 0.12 + 500000 * 0.24 + 500000 * 0.30 + (salary - 3700000) * 0.36

        print("Your Monthly Tax : ",tax/12)
        print("Your Annual Tax : ",tax)