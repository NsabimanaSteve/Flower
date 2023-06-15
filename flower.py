import turtle

# Create the turtle screen and a turtle to draw with
wn = turtle.Screen()
wn.bgcolor("pink")
t = turtle.Turtle()

def draw_flower(petal_color, x, y):
    '''draws a flower at the given position with the given petal color'''
    flowert = turtle.Turtle()
    flowert.speed(0)
    flowert.hideturtle()
    
    # Set the flower position
    flowert.penup()
    flowert.goto(x, y)
    flowert.pendown()
    
    # Set the petal color
    flowert.color(petal_color)
    
    # Draw the petals
    for i in range(10):
        flowert.circle(50, 180)
        flowert.left(36)
    
    # Draw a stem
    flowert.pensize(5)
    flowert.color('green')
    flowert.right(90)
    flowert.forward(100)
    flowert.hideturtle()

# Draw some flowers at different positions
draw_flower("red", -300, 200)
draw_flower("yellow", 0, 100)
draw_flower("purple", 300, 200)
# Draw something else in the background
t.pensize(5)
t.penup()
t.color("green")
t.goto(-300, 100)
t.pendown()
t.lt(-19)
t.forward(318)
t.penup()
t.color("green")
t.goto(300, 100)
t.pendown()
t.lt(-142)
t.forward(318)
t.lt(71)
t.forward(150)
t.begin_fill()
t.color("brown")
for i in range(4):
    t.forward(100)
    t.rt(90)
for i in range(4):
    t.right(90)
    t.backward(100)
    
t.end_fill()

wn.exitonclick()