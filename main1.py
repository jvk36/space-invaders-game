import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def move_bullet():
    global bulletstate
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

# Create keyboard binding for firing the bullet
turtle.onkey(fire_bullet, "space")

# Create the aliens
number_of_aliens = 5
aliens = []

for i in range(number_of_aliens):
    aliens.append(turtle.Turtle())

for alien in aliens:
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    x = -200 + (i * 100)
    y = 250
    alien.setposition(x, y)

alienspeed = 2

def move_aliens():
    global alienspeed  # Declare alienspeed as global
    for alien in aliens:
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)

        if alien.xcor() > 280 or alien.xcor() < -280:
            for a in aliens:
                y = a.ycor()
                y -= 40
                a.sety(y)
            alienspeed *= -1

def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    return distance < 15

def check_collisions():
    global bulletstate
    for alien in aliens:
        if is_collision(bullet, alien):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            alien.setposition(0, 10000)  # Move the alien off screen
            update_score()
        if is_collision(player, alien):
            player.hideturtle()
            alien.hideturtle()
            print("Game Over")
            break

# Create barriers
number_of_barriers = 3
barriers = []

for i in range(number_of_barriers):
    barrier = turtle.Turtle()
    barrier.color("green")
    barrier.shape("square")
    barrier.penup()
    barrier.speed(0)
    barrier.shapesize(stretch_wid=1, stretch_len=5)
    x = -200 + (i * 200)
    y = -200
    barrier.setposition(x, y)
    barriers.append(barrier)

# Create the score display
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

def update_score():
    global score
    score += 10
    score_pen.clear()
    score_string = "Score: %s" % score
    score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

level = 1

def next_level():
    global level, alienspeed, number_of_aliens
    level += 1
    alienspeed += 1
    number_of_aliens += 2
    for i in range(number_of_aliens):
        alien = turtle.Turtle()
        alien.color("red")
        alien.shape("circle")
        alien.penup()
        alien.speed(0)
        x = -200 + (i * 100)
        y = 250
        alien.setposition(x, y)
        aliens.append(alien)

# Main game loop
while True:
    move_aliens()
    move_bullet()
    check_collisions()
    wn.update()
    