import turtle
import random
dict1={"Shape1":"square","Shape2":"triangle","Shape3":"circle"}
colors=["orange","red","green","blue","yellow"]
user_input=(input("Enter shape you want to draw")) 
color=random.choice(colors)
turtle.fillcolor(color)
#Fill colors using random function
turtle.begin_fill()
if dict1.get("Shape1")==user_input:
    user_input1=int(input("Enter side of square"))
    for i in range(4):
        turtle.forward(user_input1)
        turtle.left(90)
elif dict1.get("Shape2")==user_input:
    user_input2=int(input("Enter side of triangle")) 
    for i in range(3):
        turtle.forward(user_input2)
        turtle.left(120)
elif dict1.get("Shape3")==user_input:
    user_input=int(input("Enter radius of circle")) 
    turtle.cirle(user_input) 
else:
    print("Enter a value between square, circle and triangle")
    
turtle.end_fill()
