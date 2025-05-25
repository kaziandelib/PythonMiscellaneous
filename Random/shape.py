# Import the Screen and Turtle classes from the turtle module
from turtle import Screen, Turtle

# List of colors to use for drawing each layer
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black']

# Create a window for drawing and set its background color to light blue
screen = Screen()
screen.bgcolor("lightblue")

# Create a turtle object that will do the drawing
turtle = Turtle()

# Set the thickness of the turtle's pen (drawing line) to 3 pixels
turtle.width(3)

# Set the turtle's speed to 25 (this controls how fast it draws)
turtle.speed(25)

# Loop through each color in the colors list to draw multiple layers
for c in colors:
    # Set the fill color of the shape to the current color from the list
    turtle.fillcolor(c)
    
    # Set the pen (outline) color to match the fill color
    turtle.pencolor(c)
    
    # Start filling the shape drawn after this command
    turtle.begin_fill()
    
    # Draw a circle with radius 145 units
    turtle.circle(145)
    
    # Draw a circle with radius 130 units but only draw a full circle backwards (counter-clockwise)
    turtle.circle(130, -360)
    
    # Draw a circle with radius 115 units
    turtle.circle(115)
    
    # Draw a circle with radius 100 units backwards (counter-clockwise)
    turtle.circle(100, -360)
    
    # Complete filling the shape with the fill color set earlier
    turtle.end_fill()
    
    # Turn the turtle right by 45 degrees to angle the next shape differently
    turtle.right(45)
    
    # Move the turtle forward by 30 units to separate the layers slightly
    turtle.forward(30)

# Hide the turtle cursor once drawing is finished so it doesn't show on screen
turtle.hideturtle()

# Keep the window open until the user clicks inside the window to close it
screen.exitonclick()
