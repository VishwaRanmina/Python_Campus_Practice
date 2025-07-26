while True:
    number_of_eggs = int(input("Enter Number Of Eggs :"))
    capacity_of_one_box = 12

    print("Number of Full Boxes : ",number_of_eggs // capacity_of_one_box)
    print("Remaining Eggs :",number_of_eggs % capacity_of_one_box)
    
    loop_or_not = input("Do You Want To Continue? (y/n)")
    if(loop_or_not == "n"):
        break