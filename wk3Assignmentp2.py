"""A Caesar cipher is a simple encryption technique. The encryption using a Ceasar cipher replaces a letter in the plain text 
with a letter that is a fixed number down in the alphabet. For example, with a shift of 5 the following substitutions 
would take place:
a → f
b → g
c → h
…
v → a
w → b
…
z → e
Using this substitutions, a plain text can be encrypted:

Plaintext: programming python is fun!
Encrypted text: uwtlwfrrnsl udymts nx kzs!
Your task for the assignment is to implement a Caesar cipher with a shift of 5. The program should ask the user for a plain text
 sentence and print the encrypted text."""
plaintext=input("Please enter a plaintext: ")
plaintext=plaintext.lower()
encryptedText=""
cipher ={
    "a" : "f","b":"g","c" : "h","d":"i","e":"j","f":"k","g":"l","h":"m","i":"n","j":"o",
    "k":"p","l":"q","m":"r","n":"s","o":"t","p":"u","q":"v","r":"w","s":"x","t":"y","u":"z",
    "v":"a","w":"b","x":"c","y":"d","z":"e"
}
for i in plaintext:
    if i in cipher :
        encryptedText=encryptedText + cipher[i]
    else :
        encryptedText=encryptedText + i
      
print("The Encrypted Text is : ",encryptedText)

        