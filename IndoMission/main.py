import pygame
import random
import math
from pygame import mixer

# initialise the pygame
pygame.init()

# create a screen
Height = 1225
Width = 525
counter1 = 0
counter2 = 0
screen = pygame.display.set_mode((Height, Width))

# background sound
mixer.music.load('sound/background.mp3')
mixer.music.play(-1)

# Back Walk
player_img_back = [pygame.image.load('img/Murat/Murat_Back_Walking1.png'),
                   pygame.image.load('img/Murat/Murat_Back_Walking2.png')]

# Front Walk
player_img_front = [pygame.image.load('img/Murat/Murat_Front_Walking1.png'),
                    pygame.image.load('img/Murat/Murat_Front_Walking2.png')]

# Left Walk
player_img_left = [pygame.image.load('img/Murat/Murat_Left_Walking1.png'),
                   pygame.image.load('img/Murat/Murat_Left_Walking2.png')]

# Right Walk
player_img_right = [pygame.image.load('img/Murat/Murat_Right_Walking1.png'),
                    pygame.image.load('img/Murat/Murat_Right_Walking2.png')]

# background image
background = pygame.image.load('img/bg/bg3.jpeg')

# title and icon
pygame.display.set_caption("IndoMission")
icon = pygame.image.load('img/Murat/icon.png')
pygame.display.set_icon(icon)

# Front Facing Standing Murat
img_front_standing = pygame.image.load('img/Murat/Murat_Front_Standing.png')

# Backwards Facing Standing Murat
img_back_standing = pygame.image.load('img/Murat/Murat_Back_Standing.png')

# Left Facing Standing Murat
img_left_standing = pygame.image.load('img/Murat/Murat_Left_Walking2.png')

# Right Facing Standing Murat
img_right_standing = pygame.image.load('img/Murat/Murat_Right_Walking1.png')

# coin
num_of_coins = 6  # Configure number of coins
coinImg = []
coinX = []
coinY = []
coin_img = pygame.image.load('img/coin/indomie.png')

# Enemy
num_of_enemies = 6     # Configure number of enemies
enemyX = []
enemyY = []
enemy_img = []
for i in range(1, 15):
    enemy_img.append(pygame.transform.scale(pygame.image.load(f'img/enemy/{i}.png'), (80, 80)))


def print_murat(x, y):
    if direction == -4:
        screen.blit(img_right_standing, (x, y))
    if direction == -3:
        screen.blit(img_left_standing, (x, y))
    if direction == -2:
        screen.blit(img_back_standing, (x, y))
    if direction == -1:
        screen.blit(img_front_standing, (x, y))
    if direction == 0:
        screen.blit(player_img_front[counter1 // 75], (x, y))
    if direction == 1:
        screen.blit(player_img_back[counter1 // 75], (x, y))
    if direction == 2:
        screen.blit(player_img_left[counter1 // 75], (x, y))
    if direction == 3:
        screen.blit(player_img_right[counter1 // 75], (x, y))


def print_enemy(x, y):
    screen.blit(enemy_img[counter2 // 150], (x, y))


def print_coin(x, y):
    screen.blit(coin_img, (x, y))


def is_collision(coin_x, coin_y, murat_x, murat_y):
    # print((math.pow(murat_x - coin_x, 2)) + (math.pow(coin_y - murat_y, 2)))
    dist = math.sqrt((math.pow(murat_x - coin_x, 2)) + (math.pow(coin_y - murat_y, 2)))
    if dist < 70:
        return True
    else:
        return False


def is_enemy_collision(enemy_x, enemy_y, murat_x, murat_y):
    dist = math.sqrt((math.pow(murat_x - enemy_x, 2)) + (math.pow(enemy_y - murat_y, 2)))
    if dist < 48:
        return True
    else:
        return False


# score
textX = 530
textY = 30
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    score2 = font.render("SCORE : " + str(score), True, (255, 255, 255))
    screen.blit(score2, (x, y))


keys = {
    pygame.K_w: False,
    pygame.K_s: False,
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False
}
running = True
score = 0
x_start = 200
y_start = 200
direction = -1
first_loop = True
speed = 1.3     # Configure Player Speed

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # print coins
    for i in range(num_of_coins):
        if first_loop:
            coinX.append(random.randint(0, 1125))
            coinY.append(random.randint(0, 425))
            # Collision

        collision = is_collision(coinX[i], coinY[i], x_start, y_start)
        if collision:
            # coinX.remove(coinX[i])
            # coinY.remove(coinY[i])
            coin_sound = mixer.Sound("sound/coin.mp3")
            coin_sound.play()
            coinX[i] = -100
            coinY[i] = -100
            score += 1
        print_coin(coinX[i], coinY[i])
    for j in range(num_of_enemies):
        if first_loop:
            enemyY.append(random.randint(5, 450))
            if enemyY[j] <= 170:
                enemyX.append(random.randint(5, 920))
            else:
                enemyX.append(random.randint(210, 920))
        if counter2 < 2099:
            counter2 += 1
        else:
            counter2 = 0
        enemyX[j] += 1
        if enemyX[j] >= 1170:
            enemyX[j] = 5
            enemyY[j] += 25
        if enemyY[j] >= 490:
            enemyY[j] = 5
        enemy_collision = is_enemy_collision(enemyX[j], enemyY[j], x_start, y_start)

        # Game Over
        if enemy_collision:
            mixer.music.load('sound/gameover.mp3')
            mixer.music.play(-1)
            while running:
                background = pygame.image.load('img/bg/game-over.png')
                screen.fill((0, 0, 0))
                screen.blit(background, (0, 0))
                show_score(500, 400)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                pygame.display.update()
            print("Game Over")
            print("Score : " + str(score))
            exit()

        print_enemy(enemyX[j], enemyY[j])

    first_loop = False
    if counter1 < 149:
        counter1 += 1
    else:
        counter1 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key in keys:
                keys[event.key] = True

        # Handle key release events
        if event.type == pygame.KEYUP:
            # aswd
            if event.key in keys:
                keys[event.key] = False
            if event.key == pygame.K_s and not any(keys.values()):
                direction = -1
            if event.key == pygame.K_w and not any(keys.values()):
                direction = -2
            if event.key == pygame.K_a and not any(keys.values()):
                direction = -3
            if event.key == pygame.K_d and not any(keys.values()):
                direction = -4

            # up down left right
            if event.key == pygame.K_DOWN and not any(keys.values()):
                direction = -1
            if event.key == pygame.K_UP and not any(keys.values()):
                direction = -2
            if event.key == pygame.K_LEFT and not any(keys.values()):
                direction = -3
            if event.key == pygame.K_RIGHT and not any(keys.values()):
                direction = -4
    # aswd
    if keys[pygame.K_w]:
        y_start -= speed
        direction = 1
    elif keys[pygame.K_s]:
        y_start += speed
        direction = 0
    elif keys[pygame.K_a]:
        x_start -= speed
        direction = 2
    elif keys[pygame.K_d]:
        x_start += speed
        direction = 3

    # up down left right
    if keys[pygame.K_UP]:
        y_start -= speed
        direction = 1
    elif keys[pygame.K_DOWN]:
        y_start += speed
        direction = 0
    elif keys[pygame.K_LEFT]:
        x_start -= speed
        direction = 2
    elif keys[pygame.K_RIGHT]:
        x_start += speed
        direction = 3

    # Boundaries
    if x_start <= -35:
        x_start = -35
    if x_start >= 1125:
        x_start = 1125
    if y_start <= -35:
        y_start = -35
    if y_start >= 425:
        y_start = 425

    # Win
    if score == num_of_coins:
        mixer.music.load('sound/level-passed.mp3')
        mixer.music.play(-1)
        while running:
            background = pygame.image.load('img/bg/win.jpg')
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.update()
        print("You Win")
        exit()
    print_murat(x_start, y_start)
    show_score(textX, textY)
    pygame.display.update()
