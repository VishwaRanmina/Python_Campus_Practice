number_of_eggs = int(input("Enter Number Of Eggs :"))
capacity_of_one_box = 12

print("Number of Full Boxes : ",number_of_eggs // capacity_of_one_box)
print("Remaining Eggs :",number_of_eggs % capacity_of_one_box)