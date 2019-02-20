# classic snake game by @Micah-Scott

import turtle
import time
import random
import winsound

delay = 0.1
score = int(0)
high_score = int(0)
pause = False

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Micah-Scott")
wn.bgpic("Grass_Mirror.png")
wn.addshape("apple1.gif") 
wn.setup(width=600, height=600)
wn.tracer(0)

# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# create snake food
food = turtle.Turtle()
food.turtlesize(3,3,3)
food.speed(0)
food.shape("apple1.gif") 
#food.color("red") # color null when shape is a .gif
food.penup()
food.goto(0, 150)
food.direction = "stop"

# lists
segments = []

colors = ["red", "black", "white"]

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# pause menu
def toggle_pause(pause):
    if pause == True:
        pause = False
    if pause == False:
        pause = True


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')
wn.onkeypress(toggle_pause, 'p')

# MAIN GAME LOOP
while True and pause == False:
    wn.update()
    # keep score up to date
    if score > 0:
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        winsound.PlaySound("peeeooop_x.wav", winsound.SND_FILENAME)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments after collision (border)
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment list after collision (border)
        segments.clear()
        pen.clear()
        score = int(0)
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
        delay = .1

    # check for collision with food
    if head.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add a segment when eating food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(random.choice(colors))
        new_segment.penup()
        segments.append(new_segment)
        winsound.PlaySound("bloop_x.wav", winsound.SND_ASYNC)
        # add score when eating food
        score += 10
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
        # shorten delay to make game faster
        delay -= .002

    # move the end segments first ( in reverse order )
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            winsound.PlaySound("quick_fart_x.wav", winsound.SND_FILENAME)
            # hide the segments after body collision
            for segment in segments:
                segment.goto(1000, 1000)
            # clear the segment list
            segments.clear()
            score = int(0)
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
            delay = .1

    time.sleep(delay)

wn.mainloop()
