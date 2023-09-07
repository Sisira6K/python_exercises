#Write a program that lets the user input a two-dimensional matrix (Hint: you could use a list of lists to store the matrix).
#The program should first ask the user how many rows and columns the matrix should contain. Next, the program should ask the user
#for the elements of the matrix. Your program should read the values from the user row by row. If, for example, the matrix has the 
#dimension 2 by 3, the values should be read as follows:

#First row, first value
#First row, second value
#First row, third value
#Second row, first value
#Second row, second value
#Second row, third value
#Finally, the program should calculate and print the sums of the values in each row.
rows= int(input("Enter the number of Rows: "))
columns= int(input("Enter the number of columns: "))
row=[]
column=[]
for r in range(rows):
    for c in range(columns):
        element= int(input("Value: "))
        row.append(element)
    column.append(row)
    row=[]
    print(column)
for r in column:
    print("Sum of rows: ", r, " is", sum(r))


        
        