#Elise Ward and Sam Patin

import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)

#modified
    import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    jack.forward(100)
    jack.right(90)
    if side==3:
        jack.color("blue")

#modified
import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
