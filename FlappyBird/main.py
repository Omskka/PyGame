import pygame
import random
from pygame import mixer

# Initializes the Pygame
pygame.init()

# Creates a screen
HEIGHT = 710
WIDTH = 460
COUNTER1 = 0
COUNTER2 = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
# Configure background image :  'day',  'night'     |        default = 'day'
background_img = "day"
background = pygame.transform.scale(pygame.image.load(f'img/bg/background-{background_img}.png'), (460, 710))

# Title and icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load('img/favicon.ico')
pygame.display.set_icon(icon)

# audio
wing_sound = mixer.Sound("sound/wing.wav")
point_sound = mixer.Sound("sound/point.wav")
die_sound = mixer.Sound("sound/die.wav")
hit_sound = mixer.Sound("sound/hit.wav")

# Base
base_img = []
for i in range(1, 7):
    base_img.append(pygame.transform.scale(pygame.image.load(f'img/base/{i}.png'), (460, 160)))

# Bird
birdX = 200
birdY = 300

# Vertical velocity
bird_velocity = 0

# Gravity force
gravity = 0.18

# Force applied when jumping
jump_force = -5

# Configure bird color :'bluebird' & 'redbird & 'yellowbird' & 'Muratbird'       |       default = 'yellowbird'
bird_color = "yellowbird"
bird_img = [pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-1.png'), (64, 48)),
            pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-2.png'), (64, 48)),
            pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-3.png'), (64, 48))]

bird_down_img = [pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-d1.png'), (48, 64)),
                 pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-d2.png'), (48, 64)),
                 pygame.transform.scale(pygame.image.load(f'img/bird/{bird_color}-d3.png'), (48, 64))]

# pipes
pipe_height = 290
pipe_width = 85
pipe_list_y1 = []
pipe_list_y2 = []
pipe_list_x = []


class pipes:
    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        pipe_list_x.append(pipe_x)
        pipe_list_y1.append(pipe_y1)
        pipe_list_y2.append(pipe_y2)

    def print_pipe(self, pipe_list_xx, pipe_list_yy1, pipe_list_yy2):
        # Configure pipe color : 'red' & 'green'        | default = 'green'
        pipe_color = "green"
        pipe_top_img = pygame.transform.scale(pygame.image.load(f'img/pipe/{pipe_color}-top.png'),
                                              (pipe_width, pipe_height))
        pipe_bottom_img = pygame.transform.scale(pygame.image.load(f'img/pipe/{pipe_color}-bottom.png'),
                                                 (pipe_width, pipe_height))
        screen.blit(pipe_top_img, (pipe_list_xx, pipe_list_yy1))
        screen.blit(pipe_bottom_img, (pipe_list_xx, pipe_list_yy2))


def print_bird(x, y, ctrl):
    if ctrl == 1:
        screen.blit(bird_img[COUNTER2 // 25], (x, y))
    else:
        screen.blit(bird_down_img[COUNTER2 // 25], (x, y))


def print_base():
    screen.blit(base_img[COUNTER1 // 18], (0, 550))


# Game Over images
game_over_img = pygame.transform.scale(pygame.image.load('img/bg/gameover.png'), (340, 75))
score_board_img = pygame.transform.scale(pygame.image.load('img/bg/scorePage.png'), (350, 175))
nums = []
for j in range(0, 10):
    nums.append(pygame.image.load(f'img/num/{j}.png'))


def print_gameOver():
    screen.blit(game_over_img, (60, 155))
    screen.blit(score_board_img, (55, 255))
    # Prints score
    score_tmp = score
    score_x = 355
    for score_index in range(0, len(str(score))):
        score_x -= 20
        tmp = score_tmp % 10
        screen.blit(nums[tmp], (score_x, 305))
        score_tmp = score_tmp // 10


def is_collision(bird_x, bird_y, pipe_x, pipe_y):
    if bird_x <= pipe_x + 85 and birdX >= pipe_x - 50:
        if birdY >= (gap + pipe_y) + pipe_height - 30 or bird_y <= pipe_height + pipe_y:
            return True
        # Change score
        elif pipe_x >= 201 and pipe_x < 202:
            global score
            point_sound.play()
            score += 1
    else:
        return False


run = True


# Game Over Screen
def game_over():
    while run:
        screen.fill('black')
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running = False
                exit()

            if event.type == pygame.KEYDOWN:
                # Escape
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()
        # Counter
        global COUNTER2
        if COUNTER2 < 74:
            COUNTER2 += 1
        else:
            COUNTER2 = 0

        global bird_velocity
        global birdY

        bird_velocity += gravity
        birdY += bird_velocity
        if birdY >= 490:
            birdY = 490

        print_base()
        print_bird(birdX, birdY, 0)
        print_gameOver()
        pygame.display.update()


score = 0
index = 0
indx = 0
running = True
range_start = 0
range_end = 1
first_run = True
deleted_pipe = 0

while running:
    screen.fill('black')
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False
            exit()

        if event.type == pygame.KEYDOWN:
            # Escape
            if event.key == pygame.K_ESCAPE:
                running = False
                exit()

            # Space
            if event.key == pygame.K_SPACE:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_force
                    wing_sound.play()
                    first_run = False

        # Right click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird_velocity = jump_force
                first_run = False
                wing_sound.play()
    if not first_run:
        bird_velocity += gravity
        birdY += bird_velocity
    # If bird hits base
    if birdY > 500:
        die_sound.play()
        game_over()

    # Counters
    if COUNTER1 < 89:
        COUNTER1 += 1
    else:
        COUNTER1 = 0

    if COUNTER2 < 74:
        COUNTER2 += 1
    else:
        COUNTER2 = 0

    if not first_run:
        # Assigns x and y to pipes
        pipe_x = 500
        pipe_y1 = random.randint(-145, 0)
        pipe_y2 = 550 - (pipe_height - (pipe_height + pipe_y1) + 90)

        if indx < deleted_pipe + 50:
            pipe = pipes(pipe_x, pipe_y1, pipe_y2)
            indx += 1

        # When pipes reach 'gap'(250) on x-axis adds another set of pipes
        for index in range(range_start, range_end):
            # Configure gap between pipes     |      default = 250
            # !!! Change pipe_height as x = (550 - (gap + 90)) !!!
            gap = 170

            # Configure the speed of pipes         |      default = 1.2
            pipe_speed = 1.2
            pipe_list_x[index] -= pipe_speed
            if pipe_list_x[index] < gap:
                range_end += 1
                range_start += 1

        for index2 in range(0, range_end):
            # Places the pipes outside the map
            if pipe_list_x[index2] < gap and not (pipe_list_x[index2] < -85):
                pipe_list_x[index2] -= pipe_speed

            # prints the pipe
            pipe.print_pipe(pipe_list_x[index2], pipe_list_y1[index2], pipe_list_y2[index2])

            # Checks for Collision
            collision = is_collision(birdX, birdY, pipe_list_x[index2], pipe_list_y1[index2])
            if collision:
                hit_sound.play()
                game_over()

    print_base()
    print_bird(birdX, birdY, 1)
    score_tmp = score
    score_x = 240

    for score_index in range(0, len(str(score))):
        score_x -= 20
        tmp = score_tmp % 10
        screen.blit(nums[tmp], (score_x, 70))
        score_tmp = score_tmp // 10
    pygame.display.update()
