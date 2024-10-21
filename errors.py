# SyntaxError - forgot to close parenthesis
print("Hello, world"      

      
# IndexError - there is no value in the list L at index 4
L = [42, 50, 58, 66]
val = L[4]                


# KeyError - "Hermione" is not in the dictionary of houses
houses = {"Harry" : "Gryffindor", 
          "Draco" : "Slyterhin", 
          "Ron" : "Gryffindor", 
          "Luna" : "Ravenclaw"}
print(houses["Hermione"])      


# TypeError - cannot add / concatenate an int with a str
print("I am " + 5 + "Years old")


# ValueError - cannot use a str in int.
num = int("cat")

