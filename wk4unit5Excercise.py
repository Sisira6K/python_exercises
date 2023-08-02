"""The file invoice_data.txt contains raw data for an invoice. More precisely, each line contains
the name of an item
how many items are bought
the unit price of the item
The three values are separated by a single whitespace. Prepare a beautified output of the file which contains

the name of the item formatted with 15 characters
the number of units with 3 digits
the price per item with 7 digits, 2 digits after the decimal point
the total price (number of items * price per item) with 8 digits in total, 2 digits after the decimal point"""
#read the file
with open ("invoice_data.txt","r") as file:
    #create a list of tuple 
    itemslist = [tuple(line.split()) for line in file]
    print(itemslist)
    #iterate the list through each item using indices
for item in itemslist:
    print(
        f"{item[0]:15s} {int(item[1]):3d}  {float(item[2]):7.2f}  {int(item[1])*float(item[2]):8.2f}"
    )