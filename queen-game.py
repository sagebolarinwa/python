X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
if Y2 > Y1:
  print("Moves up")
if Y2 < Y1:
  print("Moves Down")
if X2 > X1:
  print("Moves to the right")
if X2 < X1:
  print("Moves to the left")
if X2 > X1 or X2 < X1