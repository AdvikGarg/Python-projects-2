import turtle

turtle.Screen().bgcolor("#B5F505")
turtle.Screen().setup(400,500)
square=turtle.Turtle()

num_sides=4
side_len=70
angle=360/num_sides

for i in range(num_sides):
    square.forward(side_len)
    square.left(angle)
    
    square.forward(side_len)
    square.left(angle)

turtle.done()  


