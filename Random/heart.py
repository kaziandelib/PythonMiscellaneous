import turtle  # Import the turtle graphics module

pen = turtle.Turtle()  # Create a turtle object named 'pen'

def curve():
    # Draw a smooth curve by turning right 1 degree and moving forward 1 unit,
    # repeated 200 times to create a curved shape
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    # Set the fill color to red for the heart shape
    pen.fillcolor('red')
    pen.begin_fill()  # Start filling the shape with the fill color
    
    pen.left(140)     # Turn the pen left by 140 degrees to start the heart shape
    pen.forward(113)  # Draw the first line
    
    curve()           # Draw the first curved side of the heart
    
    pen.left(120)     # Turn left 120 degrees to draw the other side
    
    curve()           # Draw the second curved side
    
    pen.forward(112)  # Complete the heart shape by drawing the bottom line
    
    pen.end_fill()    # Fill the drawn heart shape with red color

if __name__ == '__main__':
    heart()       # Call the heart function to draw the heart when script runs
    turtle.done() # Finish turtle graphics and keep the window open
