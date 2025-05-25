import turtle  # Import turtle module, which is used for drawing graphics and creating games
import winsound  # Import winsound module to play sound effects on Windows systems

# Set up the game window (the screen where the game happens)
wn = turtle.Screen()  # Create a window object called 'wn'
wn.title("Pong")  # Set the title of the window to "Pong"
wn.bgcolor("black")  # Set the background color of the window to black
wn.setup(width=800, height=600)  # Define the size of the window: 800 pixels wide and 600 pixels tall
wn.tracer(0)  # Turn off automatic screen updates to control when the screen refreshes manually (improves performance)

# Initialize the scores for Player A and Player B to zero at the start of the game
score_a = 0
score_b = 0
winning_score = 5  # The score a player must reach to win the game

# Create Paddle A (the left player's paddle)
paddle_a = turtle.Turtle()  # Create a "turtle" object, which can draw or move shapes
paddle_a.speed(0)  # Set the animation speed of the paddle to the maximum (no animation delay)
paddle_a.shape("square")  # Make the paddle's shape a square (which we'll stretch to look like a rectangle)
paddle_a.color("green")  # Color the paddle green
paddle_a.penup()  # Disable drawing while the paddle moves (we only want it to move, not draw lines)
paddle_a.goto(-350, 0)  # Position the paddle on the left side, centered vertically
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square shape vertically 5 times to make it a tall paddle

# Create Paddle B (the right player's paddle) with similar setup as Paddle A
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350, 0)  # Position it on the right side
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Same tall paddle shape

# Create the Ball, which will move around the screen bouncing off paddles and edges
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # Make the ball a circle shape
ball.color("white")  # Color it white to stand out against the black background
ball.penup()  # Disable drawing when the ball moves
ball.goto(0, 0)  # Start the ball in the center of the screen
ball.dx = 0.1  # Horizontal movement speed of the ball (small number for slow movement)
ball.dy = 0.1  # Vertical movement speed of the ball

# Create a Pen object for displaying the players' scores on the screen
pen = turtle.Turtle()
pen.speed(0)  # Set speed to max so the text appears instantly
pen.color("white")  # White color for the text so it's visible on black background
pen.penup()  # Do not draw lines when moving the pen
pen.hideturtle()  # Hide the turtle shape; we only want the text, not the turtle icon
pen.goto(0, 260)  # Position the pen near the top center of the window
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 26, "normal"))  # Display initial scores

# Define function to move Paddle A up by 20 pixels
def paddle_a_up():
    y = paddle_a.ycor()  # Get current vertical position of Paddle A
    y += 20  # Increase y position by 20 pixels (move paddle up)
    paddle_a.sety(y)  # Update Paddle A to the new vertical position

# Define function to move Paddle A down by 20 pixels
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # Decrease y position by 20 pixels (move paddle down)
    paddle_a.sety(y)

# Define function to move Paddle B up by 20 pixels
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Define function to move Paddle B down by 20 pixels
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Listen for keyboard input from the player
wn.listen()  # Tell the program to wait for keyboard events

# Bind keyboard keys to the paddle movement functions
# When 'w' is pressed, Paddle A moves up
wn.onkeypress(paddle_a_up, "w")
# When 's' is pressed, Paddle A moves down
wn.onkeypress(paddle_a_down, "s")
# When 'p' is pressed, Paddle B moves up
wn.onkeypress(paddle_b_up, "p")
# When 'l' is pressed, Paddle B moves down
wn.onkeypress(paddle_b_down, "l")

# Set a flag to control when the game ends
game_over = False

# The main game loop - this will run continuously until the game is over
while not game_over:
    wn.update()  # Refresh the screen and show all updated graphics

    # Update the ball's position by moving it slightly in x and y directions every frame
    ball.setx(ball.xcor() + ball.dx)  # Move ball horizontally by ball.dx
    ball.sety(ball.ycor() + ball.dy)  # Move ball vertically by ball.dy

    # Check if the ball hits the top edge of the window (y position greater than 290)
    if ball.ycor() > 290:
        ball.sety(290)  # Stop ball at the top edge so it doesn't go off-screen
        ball.dy *= -1  # Reverse vertical direction to simulate bouncing
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound asynchronously (without delay)

    # Check if the ball hits the bottom edge of the window
    if ball.ycor() < -290:
        ball.sety(-290)  # Stop ball at the bottom edge
        ball.dy *= -1  # Reverse vertical direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Check if the ball goes past the right edge (Player B misses)
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Reset ball position to center
        ball.dx *= -1  # Reverse horizontal direction so ball moves towards Player B again
        score_a += 1  # Player A scores a point
        pen.clear()  # Clear previous score text
        # Write new scores on the screen, centered at the top
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 26, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)  # Play scoring sound

    # Check if the ball goes past the left edge (Player A misses)
    if ball.xcor() < -390:
        ball.goto(0, 0)  # Reset ball to center
        ball.dx *= -1  # Reverse horizontal direction to move ball towards Player A again
        score_b += 1  # Player B scores a point
        pen.clear()  # Clear previous score text
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 26, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)  # Play scoring sound

    # Detect collision between ball and Paddle B
    # If ball is near Paddle B horizontally and vertically within paddle's height
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 40 < ball.ycor() < paddle_b.ycor() + 40):
        ball.setx(340)  # Prevent ball from overlapping paddle
        ball.dx *= -1  # Bounce ball back in opposite horizontal direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound

    # Detect collision between ball and Paddle A
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 40 < ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)  # Prevent ball overlapping paddle
        ball.dx *= -1  # Bounce ball back
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Check if any player has reached the winning score
    if score_a >= winning_score or score_b >= winning_score:
        game_over = True  # End the main game loop and stop the game

# After the game loop ends, show the end game screen

wn.bgcolor("white")  # Change background color to white for contrast on the final screen
pen.goto(0, 0)  # Position pen in the center of the screen to write the winner message
pen.color("black")  # Change pen color to black to stand out on white background

# Display which player won the game, based on who has the higher score
if score_a > score_b:
    pen.write("Player A Wins!", align="center", font=("Courier", 36, "bold"))
else:
    pen.write("Player B Wins!", align="center", font=("Courier", 36, "bold"))

winsound.PlaySound("win.wav", winsound.SND_ASYNC)  # Play a winning sound effect

wn.mainloop()  # Keep the game window open until the user closes it manually
