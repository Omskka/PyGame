import pygame
import random
import math
from pygame import mixer

# initialise the pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# background image
background = pygame.image.load('img/bg.jpg')

# background sound
mixer.music.load('sound/background.wav')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/wizard.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('img/space.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
EnemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('img/alien.png'))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(20)

# bullet
bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.9
bullet_state = "ready"

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def game_over():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = font.render("GAME OVER!" , True, (255, 255, 255))
    screen.blit(over_text, (290, 250))

def show_score(x, y):
    score2 = font.render("SCORE : " + str(score), True, (255, 255, 255))
    screen.blit(score2, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x + 16, y + 16))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if dist < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    # rgb
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                playerX_change = -0.4
            if event.key == pygame.K_d:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    laser_sound = mixer.Sound("sound/laser.wav")
                    laser_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("sound/explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
