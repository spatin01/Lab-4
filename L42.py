#Samantha Patin and Elise Ward
import turtle
greg=turtle.Turtle()
greg.color("yellow")

for side in range(4):
    greg.forward(100)
    greg.right(90)

#Part 1
mary=turtle.Turtle()
mary.color("blue")

for side in range(4):
    if side ==2:
        mary.color("red")
    if side==3:
        mary.color("cyan")
    mary.forward(100)
    mary.right(90)
#Part 2
fred=turtle.Turtle()
fred.color("blue")

for side in range(4):
    if side==1:
        fred.color("yellow")
    if side ==2:
        fred.color("red")
    if side==3:
        fred.color("cyan")
    fred.forward(100)
    fred.right(90)
