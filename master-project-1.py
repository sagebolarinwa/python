"""
1. Read the project directions before getting started: https://docs.google.com/document/d/178gHKwryzf3crh0cjsYc97gSzMevd7IGi0BDtd7l-WI/edit?usp=sharing

2. Ask Ms. Lawrence for any clarifications or about anything that is confusing.

3. Sign the honor pledge in the comment below.

4. Get started on your project!

5. When you're finished, you need to share your screencast with Ms. Lawrence, but you do not need to click the submit button on repl.it.
"""

#choose you own adventure
#Sage Bolarinwa
#Monday, September 16th
#it is a story about going camping
#Honor Code Pledge:Sage Bolarinwa
option = 1
while option != 2:
  hair = input("choose your hair color:")
  skin = input("choose your skin color:")
  eyes = input("choose your eye color:")
  name = input("choose your name:")
  print("Welcome, " + name)

  print("On a random night while you're going camping you hear a noise in the darkness of the woods.")
  option = int(input("Would you like to: \n(1) go looking for what's making the noise? or \n(2) try and ignore the noise and sleep?"))
  if option == 1:
    print("You and would look for the noise all night and you think you heard someone say " + name + " in the distance.")
    option = int(input("Would you like to: \n(1) go back to camp? or \n(2) keep searching?"))
    if option == 1:
      print("On your way back to camp you here the noise getting loader and loader when you reach the camp you find that the strange noise was just a stray dogs barking that sounded like " + name + " so you go back to sleep.")
    elif option == 2:
      print("As you keep searching the woods you come across a nest of a strange creature and when you turn around you realize this creature was not saying " + name + " so you try to run but it quickly grabs you and eats you whole.")

  elif option == 2:
    print("You stay in your tent but the noise keeps getting louder and louder until you just can’t bear it anymore.")
    option = int(input("Would you like to: \n(1) go looking for the strange noise? or \n(2) keep trying to sleep through the noise?"))
    if option == 1:
      print("You get out of your tent angry and annoyed and go looking the noise, as you get closer a bucket of slime dumps on you and you realize it was some nearby campers playing a prank on you.")
    elif option == 2:
      print("You try your hardest to sleep through the noise and finally you fall asleep but when you wake up you realize that someone had but your tent on a nearby river that has a waterfall at the end but luckily you tent gets caught on a rock and you manage to get onto land and make it safely home never finding out who or what put you on that river.")

  print("would you like to resart")
  option = int(input("\n(1) Yes \n(2) No"))
  if option == 1:
    print("Play again!")
  elif option == 2:
    print("Goodbye " + name +"!")