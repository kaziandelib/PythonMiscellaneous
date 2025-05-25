# Import the Screen and Turtle classes from the turtle module
# Screen is used to create and manage the window where drawing happens
# Turtle is the drawing pen or cursor that moves around to create shapes and lines
from turtle import Screen, Turtle

# Import the time module to use time-related functions like pauses/delays
import time

# List of colors for each lantern corps
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black']

# Corresponding oath texts for each color segment
oaths = [
    "With blood and rage of crimson red, ripped from a corpse so freshly dead, together with our hellish might, we scorch the universe on fire's light!",
    "What's mine is mine and mine and mine. And mine and mine and mine! You may try to take it, but you will find that mine, mine, mine, mine!",
    "In blackest day, in brightest night, beware your fears made into light. Let those who try to stop what's right, burn like my power — Sinestro's might!",
    "In brightest day, in blackest night, no evil shall escape my sight. Let those who worship evil's might, beware my power — Green Lantern's light!",
    "In fearful day, in raging night, with strong hearts full, our souls ignite. When all seems lost in hope's dark plight, we'll be the light — the Blue Lantern's light!",
    "Tor lorek san, bor nakka mur. Natromo faan tornek wot ur.",
    "For hearts long lost and full of fright, for those alone in blackest night, accept our ring, and join the fight, love conquers all, the Star Sapphire's light!",
    "The Blackest Night falls from the skies, the darkness grows as all light dies. We crave your hearts and your demise, by my hand, the dead shall rise!"
]

# White Lantern oath text to display at the end
white_lantern_oath = "In the brightest day, in the darkest night, no evil shall escape my sight. Let those who worship evil's might, beware my power — the White Lantern's light!"

# Setup the turtle graphics window with a light blue background
screen = Screen()
screen.bgcolor("lightblue")

# Main drawing turtle that will draw the colored shapes
turtle = Turtle()
turtle.width(3)   # Set the pen width to 3
turtle.speed(0)   # Set drawing speed to the fastest

# Turtle dedicated to writing the text; hide the turtle cursor and lift pen to avoid drawing lines
text_turtle = Turtle()
text_turtle.hideturtle()
text_turtle.penup()

def draw_text_with_outline(turtle, text, color, outline_color="black", font=("Arial", 12, "bold")):
    """Draw text with an outline by drawing the text multiple times with small offsets."""
    x, y = turtle.position()
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Positions around text for outline
    # Draw the outline by writing text in the outline color at each offset
    for dx, dy in offsets:
        turtle.goto(x + dx, y + dy)
        turtle.color(outline_color)
        turtle.write(text, align="center", font=font)
    # Draw the main text on top with the main color
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align="center", font=font)

# Function to position the text turtle near the bottom to avoid overlapping the drawing
def position_text_below():
    text_turtle.goto(0, -280)  # Position near the bottom of the screen

# Optionally, position the text near the top (not used here but ready for use)
def position_text_above():
    text_turtle.goto(0, 280)  # Position near the top of the screen

# Start with text positioned below the drawings
position_text_below()

# Loop through each color and its oath text
for i, color in enumerate(colors):
    # Set fill and pen color for the current segment
    turtle.fillcolor(color)
    turtle.pencolor(color)

    turtle.begin_fill()          # Start filling shape
    turtle.circle(145)           # Draw large circle
    turtle.circle(130, -360)     # Draw smaller circle counter-clockwise
    turtle.circle(115)           # Draw smaller circle clockwise
    turtle.circle(100, -360)     # Draw smallest circle counter-clockwise
    turtle.end_fill()            # Fill the drawn shape with current color

    # Clear previous text and write the current oath with an outline for readability
    text_turtle.clear()
    draw_text_with_outline(text_turtle, oaths[i], color)

    turtle.right(45)             # Rotate turtle by 45 degrees for next segment
    turtle.forward(30)           # Move forward slightly to offset next segment

    time.sleep(2)                # Pause for 2 seconds so user can read the oath

# After all segments, change background to black for the final white lantern oath
screen.bgcolor("black")
text_turtle.clear()
position_text_below()
draw_text_with_outline(text_turtle, white_lantern_oath, "white", outline_color="gray")

# Prepare to redraw the same design in white color on black background
turtle.color("white")
turtle.fillcolor("white")
turtle.penup()
turtle.home()
turtle.pendown()

# Draw 8 white segments matching the original design
for _ in range(8):
    turtle.begin_fill()
    turtle.circle(145)
    turtle.circle(130, -360)
    turtle.circle(115)
    turtle.circle(100, -360)
    turtle.end_fill()
    turtle.right(45)
    turtle.forward(30)

turtle.hideturtle()  # Hide the drawing turtle cursor

# Keep the window open until user clicks
screen.exitonclick()
