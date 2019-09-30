name1 = input("Enther a name:")
name2 = input("Enter another name:")
if name1 > name2:
  print(name1 + " comes after " + name2 + " alphabetically")
if name2 > name1:
  print(name2 + " comes after " + name1 + " alphabetically")
if name1 == name2:
  print("You entered the same name twice.")