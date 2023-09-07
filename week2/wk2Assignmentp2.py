"""An initial stock level for a product
The number of month(s) to plan
The planned sales quantity for each month
Based on this data, calculate the required production quantity as follows:
If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference"""

initialStock=int(input("Please enter an initial stock level: "))
planningMonths = int(input("Please enter the number of month to plan: "))
plannedSales= [int(input("Please enter the planned sales quantity: ")) for l in range(planningMonths  )]
print("The resulting production quantities are:")
month = 1
for i in plannedSales:
    
    stockLevel= initialStock-i
    if stockLevel > 0:
        prodQuantity=0
        print("Production quantity month ", month, " - ", prodQuantity)
        initialStock=stockLevel
    else :
        prodQuantity=i-abs(initialStock)
        print("Production quantity month ", month, " - ", prodQuantity)
        initialStock=0
    month += 1