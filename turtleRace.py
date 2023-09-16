import turtle
import time
import random

# Setup values and turtle variables
xSetup = 1200
ySetup = 650
movementDelay = 0.001

wn = turtle.Screen()
wn.title("Racing Game")
wn.setup(xSetup, ySetup)
wn.bgcolor("black")
wn.tracer(0)
delay = 0.15

p1_segments = []
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.up()
p1.setpos(-565, 150)
p1.direction = "stop"

p2_segments = []
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.up()
p2.setpos(-565, -150)
p2.direction = "stop"

foodX = (xSetup / 2) - 30
foodY = (ySetup / 2) - 30
x = random.randint(foodX * -1, foodX)
y = random.randint(foodY * -1, foodY)
food1 = turtle.Turtle()
food1.shape("turtle")
food1.speed(0)
food1.up()
food1.color("green yellow")
food1.setpos(x, y)

text = turtle.Turtle()
text.speed(0)
text.up()
text.shape("square")
text.color("white")
text.hideturtle()

p1Score = 0
p2Score = 0
score = turtle.Turtle()
score.speed(0)
score.up()
score.color("white")
score.shape("square")
score.hideturtle()
score.setpos(0, -300)
score.write(f"Red: {p1Score}  Blue: {p2Score}", align = "center", font = ("Verdana", 16, "bold"))

# for keyboard bindings
def p1_go_up():
    if p1.direction != "down":
        time.sleep(movementDelay)
        p1.direction = "up"
def p2_go_up():
    if p2.direction != "down":
        time.sleep(movementDelay)
        p2.direction = "up"
def p1_go_down():
    if p1.direction != "up":
        time.sleep(movementDelay)
        p1.direction = "down"
def p2_go_down():    
    if p2.direction != "up":
        time.sleep(movementDelay)
        p2.direction = "down"
def p1_go_right():
    if p1.direction != "left":
        time.sleep(movementDelay)
        p1.direction = "right"
def p2_go_right():
    if p2.direction != "left":
        time.sleep(movementDelay)
        p2.direction = "right"
def p1_go_left():
    if p1.direction != "right":
        time.sleep(movementDelay)
        p1.direction = "left"
def p2_go_left():    
    if p2.direction != "right":
        time.sleep(movementDelay)
        p2.direction = "left"
        
def reset_game():
    time.sleep(0.5)
    p1.setpos(-565, 150)
    p1.direction = "stop"
    p2.setpos(-565, -150)
    p2.direction = "stop"
    score.clear()
    score.write(f"Red: {p1Score}  Blue: {p2Score}", align = "center", font = ("Verdana", 16, "bold"))
    for segment in p1_segments:
        segment.setpos(1000, 1000)
    p1_segments.clear()
    for segment in p2_segments:
        segment.setpos(1000, 1000)
    p2_segments.clear()

# to check for change of directions
def move():
    if p1.direction == "up":
        text.clear()
        p1y = p1.ycor()
        p1.sety(p1y + 20)
    if p1.direction == "down":
        text.clear()
        p1y = p1.ycor()
        p1.sety(p1y - 20)
    if p1.direction == "right":
        text.clear()
        p1x = p1.xcor()
        p1.setx(p1x + 20)
    if p1.direction == "left":
        text.clear()
        p1x = p1.xcor()
        p1.setx(p1x - 20)

    if p2.direction == "up":
        text.clear()
        p2y = p2.ycor()
        p2.sety(p2y + 20)
    if p2.direction == "down":
        text.clear()
        p2y = p2.ycor()
        p2.sety(p2y - 20)
    if p2.direction == "right":
        text.clear()
        p2x = p2.xcor()
        p2.setx(p2x + 20)
    if p2.direction == "left":
        text.clear()
        p2x = p2.xcor()
        p2.setx(p2x - 20)
    

def buttonClick(x, y):
    print(f"Coordinate ({x}, {y})")

# listen to keyboard clicks for movement of player
wn.listen()
wn.onkeypress(p1_go_up, "w")
wn.onkeypress(p2_go_up, "Up")
wn.onkeypress(p1_go_down, "s")
wn.onkeypress(p2_go_down, "Down")
wn.onkeypress(p1_go_right, "d")
wn.onkeypress(p2_go_right, "Right")
wn.onkeypress(p1_go_left, "a")
wn.onkeypress(p2_go_left, "Left")
wn.onscreenclick(buttonClick, 1)

while True:
    # update screen while loop is true
    wn.update()

    time.sleep(delay)

    if p1.distance(food1) < 20:
        x = random.randint(foodX * -1, foodX)
        y = random.randint(foodY * -1, foodY)
        food1.setpos(x, y)
        p1Score += 1
        score.clear()
        score.write(f"Red: {p1Score}  Blue: {p2Score}", align = "center", font = ("Verdana", 16, "bold"))

        p1_newSegment = turtle.Turtle()
        p1_newSegment.shape("square")
        p1_newSegment.color("dark red")
        p1_newSegment.up()
        p1_segments.append(p1_newSegment)
    
    for index in range(len(p1_segments) - 1, 0, -1):
        p1_xSegment = p1_segments[index - 1].xcor()
        p1_ySegment = p1_segments[index - 1].ycor()
        p1_segments[index].setpos(p1_xSegment, p1_ySegment)

    if len(p1_segments) > 0:
        p1_xhead = p1.xcor()
        p1_yhead = p1.ycor()
        p1_segments[0].setpos(p1_xhead, p1_yhead)

    if p2.distance(food1) < 20:
        x = random.randint(foodX * -1, foodX)
        y = random.randint(foodY * -1, foodY)
        food1.setpos(x, y)
        p2Score += 1
        score.clear()
        score.write(f"Red: {p1Score}  Blue: {p2Score}", align = "center", font = ("Verdana", 16, "bold"))

        p2_newSegment = turtle.Turtle()
        p2_newSegment.shape("square")
        p2_newSegment.color("midnight blue")
        p2_newSegment.up()
        p2_segments.append(p2_newSegment)
    
    for index in range(len(p2_segments) - 1, 0, -1):
        p2_xSegment = p2_segments[index - 1].xcor()
        p2_ySegment = p2_segments[index - 1].ycor()
        p2_segments[index].setpos(p2_xSegment, p2_ySegment)

    if len(p2_segments) > 0:
        p2_xhead = p2.xcor()
        p2_yhead = p2.ycor()
        p2_segments[0].setpos(p2_xhead, p2_yhead)

    if p1.ycor() < -305 or p1.ycor() > 320 or p1.xcor() > 587 or p1.xcor() < -597:
        text.write("Red went over the line!", align = "center", font = ("Verdana", 25, "bold"))
        p2Score +=1 
        reset_game()
        
        

    if p2.ycor() < -305 or p2.ycor() > 320 or p2.xcor() > 587 or p2.xcor() < -597:
        text.write("Blue went over the line!", align = "center", font = ("Verdana", 25, "bold"))
        p1Score += 1
        reset_game()
        
    move()

    # check for self collisions
    for p1_segment in p1_segments:
        if p1_segment.distance(p1) < 20:
            text.clear()
            text.write("Red ate his self!", align = "center", font = ("Verdana", 25, "bold"))
            p2Score += 1
            reset_game()
        # check for collisions with other players body
        if p2.distance(p1_segment) < 20:
            text.clear()
            text.write("Game Over! Red Won!", align = "center", font = ("Verdana", 25, "bold"))
            time.sleep(0.5)
            p1Score = 0
            p2Score = 0
            reset_game()
    for p2_segment in p2_segments:
        if p2_segment.distance(p2) < 20:
            text.clear()
            text.write("Blue ate his self!", align = "center", font = ("Verdana", 25, "bold"))
            p1Score += 1
            reset_game()
        # check for collisions with other players body
        if p1.distance(p2_segment) < 20:
            text.clear()
            text.write("Game Over! Red Won!", align = "center", font = ("Verdana", 25, "bold"))
            time.sleep(0.5)
            p1Score = 0
            p2Score = 0
            reset_game()

    
    

    

wn.mainloop()
