"""You will need to set the following variables
Set variable c to "cats."
Set variable d to "dogs."
Using the variables c and d, set variable s to the value "It is raining cats and dogs."
Your last command in the program should be print(s)"""
## Set variables
c = "cats." ## is the instructions wrong by placing a period in the variable name string?
d = "dogs." 
s = "It is raining " + c[:-1] + " and " + d ## stip the period from cats. 
print (s)
