"""There is a file secret.txt, which contains one character per line. There is a second file key.txt,
which contains two lines with one number per line (the number could have several digits).
 The first number col represents the number of columns of a grid, the second number row represents 
 the number of rows of the grid.
The characters of the first file should now be filled into this grid. Take the characters one by one 
and fill them into a string until the string contains col characters. Append the string to a list. Then 
create a new string the same way. Continue, until the number of strings is equal to row. Now, write all 
the strings into a file public.txt. Open the the file and check the content."""
with open("key.txt","r") as file:
    
    tablelist= [line.strip() for line in file]
    column=tablelist[0]
    row=tablelist[1]
    #print(column,row)
    finallist=[]
    empstring=""
    with open("secret.txt","r") as file:
        for i in range(int(row)):
            for j in range(int(column)):
                empstring=empstring+file.readline().strip()
            finallist.append(empstring)   
            empstring=""
        with open ("public.txt","w") as file2:
            for x in finallist:
                file2.write(x+"\n")

        