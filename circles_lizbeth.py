#initialization
import turtle
import random
lizbeth=turtle.Turtle()
turtle.colormode(255)

#functions
def randomDot():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    lizbeth.color(r,g,b)
    lizbeth.begin_fill()
    s=random.randint(0,255)
    lizbeth.circle(s)
    lizbeth.end_fill()
   
  
#main
randomDot()
