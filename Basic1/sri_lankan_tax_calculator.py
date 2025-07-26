while True:
    salary = float(input("Enter Annual Your Salary : "))

    if(salary <= 1200000):
        print("YOu Don't need to pay tax")
    else:
        taxable = salary - 1200000
        if(taxable <= 500000):
            tax = taxable*0.06
            print("Tax :",tax)
            
        elif(taxable <= 1000000):
            tax = taxable * 0.06 + (taxable-500000)*0.12
            print("Tax :",tax)
        elif(taxable <= 1500000):
            tax = 500000 * 0.06 + 500000 * 0.12 + (taxable-500000)*0.18
            print("Tax :",tax)
        elif(taxable <= 2000000):
            tax = 500000 * 0.06 + 500000 * 0.12 + 500000*0.18 + (taxable-500000)*0.24
            print("Tax :",tax)
        elif(taxable <= 2500000):
            tax = 500000 * 0.06 + 500000 * 0.12 + 500000*0.18 + 500000*0.24 + (taxable-500000)*0.30
            print("Tax :",tax)
        elif(taxable <= 2500000):
            tax = 500000 * 0.06 + 500000 * 0.12 + 500000*0.18 +  500000*0.24 + 500000*0.30 + (taxable-500000)*0.36
            print("Tax :",tax)
        elif(taxable <= 3000000):
            tax = 500000 * 0.06 + 500000 * 0.12 + 500000*0.18 +  500000*0.24 + 500000*0.30 + 500000*0.36 + (taxable-500000)*0.36
            print("Tax :",tax)
        else:
            tax = 500000 * 0.06 + 500000 * 0.12 + 500000*0.18 +  500000*0.24 + 500000*0.30 + 500000*0.36 + (taxable-500000)*0.36
            print("Tax :",tax)
        
        
        