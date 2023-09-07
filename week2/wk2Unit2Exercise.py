#A list containing the titles of the prequel trilogy: The Phantom Menace, Attack of the Clones, Revenge of the Sith
#A list containing the titles of the original trilogy: A New Hope, The Empire Strikes Back, Return of the Jedi,
#A list containing the titles of the sequel trilogy: The Force Awakens, The Last Jedi, The Rise of Skywalker.
# Write a program that asks the user for a number of the trilogy (1, 2 or 3) and the number of the film in this trilogy (1, 2 or 3). 
#Print the title of the film corresponding to the user selection.

star_wars_movies = [  
["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],  
["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],   
["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]
trilogyNo =int(input("Enter Trialogy Number(1,2,3): "))
filmNo =int(input("Enter the Film Number(1,2,3): "))
x=star_wars_movies[trilogyNo][filmNo]
print("The Title of the Film is : ", x)