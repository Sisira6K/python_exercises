p1wins=0
p2wins=0
draws=0
choice_of_player1 = []
choice_of_player2=[]

with open ("player1.txt","r") as file1:
    choice_of_player1=[line.strip() for line in file1]
with open ("player2.txt","r") as file2:        
    choice_of_player2=[line.strip() for line in file2]

for i in range(100):
    if choice_of_player1[i]=="P":
        if choice_of_player2[i]=="R":
            p1wins+=1
        elif choice_of_player2[i]=="S":
            p2wins+=1
        else:
            draws+=1

    if choice_of_player1[i]=="R":
        if choice_of_player2[i]=="S":
            p1wins+=1
        elif choice_of_player2[i]=="P":
            p2wins+=1
        else:
            draws+=1

    if choice_of_player1[i]=="S":
        if choice_of_player2[i]=="P":
            p1wins+=1
        elif choice_of_player2[i]=="R":
            p2wins+=1
        else:
            draws+=1

print("Player1 wins:",p1wins)
print("Player2 wins:",p2wins)
print("Draw:",draws)