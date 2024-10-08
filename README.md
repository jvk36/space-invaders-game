# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## Key Components:

Player: Controlled by the left and right arrow keys.

Enemy Invaders: Move back and forth across the screen, dropping down after reaching the screen edges.

Bullet: Fired by the player, capable of hitting enemies.

Score Tracking: Updates as enemies are hit.

## How It Works:

Player Movement: The player moves left and right using the arrow keys.

Enemy Movement: The enemy moves horizontally and reverses direction when reaching the screen edge, then moves down a row.

Shooting: The player fires a bullet using the space bar, and the bullet moves upwards.

Collision Detection: If the bullet hits the enemy, the enemy is repositioned randomly, and the score increases.

## Features to Expand:

Add multiple enemies in a grid formation.

Increase enemy speed as more are defeated.

Introduce game levels and different difficulty stages.
