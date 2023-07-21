# A right triangle has one angle of 90°
#A obtuse triangle has one angle of more than 90°
#A triangle is acute if all three angles are less than 90°
#Write a program that asks the user for the values of three angles in degrees.
#First check if the entered values are valid. The values are only valid if they are >0 and if their sum is 180°. 
#If the entered values are valid, classify the triangle as right, acute or obtuse.


fangle =int(input("Please enter the first angle: "))
sangle =int(input("Please enter the second angle: "))
tangle =int(input("Please enter the third angle: "))

if ((fangle > 0) and ( sangle >0) and (tangle >0)) and ((fangle + sangle + tangle )==180) :
        print("The entered values are valid")
        if fangle ==90 or sangle ==90 or tangle==90  :
            print("The Triangle is a Right triangle")
        elif fangle >90 or sangle>90 or tangle>90 :
            print("This Triangle is an Obtuse Triangle")
        else :
            print("This Triangle is Acute Triangle")
elif ((fangle < 0) or ( sangle <0) or (tangle <0))  :
        print("Angles smaller than 0 are not valid")
else :
        print("The entered values are not valid")
        