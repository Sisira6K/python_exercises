"""Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift. 
The program should ask the user for a number of characters for the shift first. Next the program should ask the user 
for a plain text sentence and print the encrypted text."""
abc = "abcdefghijklmnopqrstuvwxyz"
shiftNumber=int(input("Please enter the number of places to shift: "))
if shiftNumber>25 :
    print("You need to enter a number between 0 and 25!" )
else:
    plaintext=input("Please enter a plaintext: ")
    encrypted_char=""
    plaintext=plaintext.lower()
    for letter in plaintext :
        char_index =abc.find(letter)
        if char_index >=0 and char_index<26:
            encrypted_char =encrypted_char+ abc[(char_index + shiftNumber)%26] 
        else :
            encrypted_char =encrypted_char + letter 
    print(encrypted_char)






