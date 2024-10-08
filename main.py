import turtle
import math
import random
import time

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.setup(width=600, height=600)

# Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-290, -290)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(580)
    border_pen.lt(90)
border_pen.hideturtle()

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 260)
score_string = f"Score: {score}"
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player_speed = 15

# Player movement
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemy_speed = 2

# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20

# Bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Move the enemy
def move_enemy():
    global enemy_speed
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Reverse direction and move down
    if x > 280 or x < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

# Fire the bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move the bullet above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Move the bullet
def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

# Check for collision between the bullet and the enemy
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 15

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    move_enemy()
    move_bullet()

    # Check for bullet-enemy collision
    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)  # Reset bullet position
        enemy.setposition(random.randint(-200, 200), 250)  # Respawn the enemy
        score += 10
        score_pen.clear()
        score_string = f"Score: {score}"
        score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

    # Check if enemy reaches the player (end game logic)
    if enemy.ycor() < -250:
        enemy.hideturtle()
        player.hideturtle()
        print("Game Over")
        break

turtle.done()
