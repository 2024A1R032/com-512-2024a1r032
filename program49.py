# write a pyhton  program to calculate the final bill amount after applying a discount. the program should take the total bill amount as input from the user and apply the dicount according to the following rules . after calculating the discount , the program should display the discount amount and the final bill amount payable by customer 

total_bill=float(input("enter the total bill: "))

if total_bill>5000:
    discount=bill*20/100
elif total_bill>=3000 and total_bill<=5000:
    discount=bill * 10/100
else:
    discount=0
    final_bill=total_bill-discount
    print("Discount: ",discount)
    print("Final bill: ",final_bill)
   