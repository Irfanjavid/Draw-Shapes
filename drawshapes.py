import turtle
import random

dict1={"Shape1":"square","Shape2":"triangle","Shape3":"circle"}
colors=["orange","red","green","blue","yellow"]
user_input=(input("Enter shape you want to draw"))

#Take user input for the shape and use variable name as user_input

#Fill colors using random function
color=random.choice(colors)
turtle.fillcolor(color)
turtle.begin_fill()

if dict1.get("Shape1")==user_input:
    user_inputa=int(input("Enter side of square"))
    for i in range(4):
        turtle.forward(user_inputa)
        turtle.left(90)
    #Write the code for drawing a square having side = 100
elif dict1.get("Shape2")==user_input:
    user_inputb=int(input("Enter side of triangle"))
    for i in range(3):
        turtle.forward(user_inputb)
        turtle.left(120)
  
    #use the get function using key==user_input:
    #Write the code for drawing a triangle having side = 100
elif dict1.get("Shape3")==user_input:
    user_inoutc=int(input("Enter radius of circle"))
#use the get function using key==user_input:
    #Draw a square of radius = 100
else:
    print("Enter a value between square, triangle and circle")
    
turtle.end_fill()
