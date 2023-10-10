import pygame
import random
import math
from pygame import mixer

# initialise the pygame
pygame.init()

# background image
background = pygame.transform.scale(pygame.image.load(f'img/bg/bg.png'), (1000, 800))

# create a screen
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background music
mixer.music.load('sound/background.mp3')
mixer.music.play(-1)

# Other audio
jump_audio = mixer.Sound('sound/jump.mp3')
death_audio = mixer.Sound('sound/death.mp3')
# game_over_audio = mixer.Sound('sound/gameOver.mp3')

# title and icon
pygame.display.set_caption("Game")
icon = pygame.image.load('img/player/icon.png')
pygame.display.set_icon(icon)

# Player
PLAYER_X = 125
PLAYER_Y = 422
player_stand_img = []
player_die_img = []
player_run_img = []
player_jump_img = []
player_fall_img = []

# Stand
for num1 in range(1, 5):
    player_stand_img.append(pygame.transform.scale(pygame.image.load(f'img/player/stand/stand{num1}.png'), (128, 128)))

# Jump
for num2 in range(1, 7):
    player_jump_img.append(pygame.transform.scale(pygame.image.load(f'img/player/jump/Jump_{num2}.png'), (250, 128)))

# Run
for num3 in range(1, 8):
    player_run_img.append(pygame.transform.scale(pygame.image.load(f'img/player/run/Walking_{num3}.png'), (178, 128)))

# Fall
for num4 in range(1, 4):
    player_fall_img.append(pygame.transform.scale(pygame.image.load(f'img/player/fall/Fall_{num4}.png'), (178, 128)))

# die
for num8 in range(1, 6):
    player_die_img.append(pygame.transform.scale(pygame.image.load(f'img/player/die/Dying_{num8}.png'), (178, 128)))

# Enemy
# Slime
slime_img = []
for num5 in range(1, 11):
    slime_img.append(pygame.transform.scale(pygame.image.load(f'img/enemy/slime/green_slime{num5}.png'), (42, 66)))

# Skull
skull_img = []
for num6 in range(1, 17):
    skull_img.append(pygame.transform.scale(pygame.image.load(f'img/enemy/skull/skull{num6}.png'), (100, 100)))

# Score nums
score_img = []
for num7 in range(0, 10):
    score_img.append(pygame.transform.scale(pygame.image.load(f'img/num/{num7}.png'), (32, 72)))


class Terrain:
    def __init__(self, start_x, start_y, terrain_width):
        self.start_x = start_x
        self.start_y = start_y
        self.terrain_width = terrain_width


# Print Player
def print_player(x, y, position):
    if position == "stand":
        screen.blit(player_stand_img[counter1 // 30], (x, y))

    if position == "run":
        screen.blit(player_run_img[counter2 // 30], (x, y))

    if position == "fall":
        screen.blit(player_fall_img[counter3 // 60], (x, y))

    if position == "jump":
        screen.blit(player_jump_img[counter4 // 35], (x, y))


def print_start_flag(x, y):
    start_flag_img = pygame.transform.scale(pygame.image.load('img/bg/Start (Idle).png'), (100, 100))
    screen.blit(start_flag_img, (x, y))


# Score
textX = 410
textY = 295
font = pygame.font.Font('freesansbold.ttf', 32)


def print_score():
    score_tmp = score
    score_x = 515
    for index in range(0, len(str(score))):
        score_x -= 40
        tmp = score_tmp % 10
        screen.blit(score_img[tmp], (score_x, 60))
        score_tmp = score_tmp // 10


def print_terrain(x, y, width):
    for i in range(0, width):
        screen.blit(terrain_img, (x, y))
        x += 70


def print_enemy(x, y, mob):
    if mob == "slime":
        screen.blit(slime_img[counter5 // 30], (x, y))
    if mob == "skull":
        screen.blit(skull_img[counter5 // 18], (x, y))


# Counters
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0


def counter():
    global counter1
    global counter2
    global counter3
    global counter4
    global counter5

    if is_first_loop:
        # Counter for 'standing'
        if counter1 < 119:
            counter1 += 1
        else:
            counter1 = 0

        # Counter for slime and skull
        if counter5 < 62:
            counter5 += 1
        else:
            counter5 = 0
    else:
        # Counter for 'running'
        if counter2 < 179:
            counter2 += 1
        else:
            counter2 = 0

        # Counter for 'falling'
        if counter3 < 119:
            counter3 += 1
        else:
            counter3 = 0

        # Counter for 'Jumping'
        if counter4 < 174:
            counter4 += 1
        else:
            counter4 = 0

        # Counter for slime
        if counter5 < 269:
            counter5 += 1
        else:
            counter5 = 0


def is_falling():
    if (PLAYER_Y + 128 <= terrain_one.start_y + 5) and (
            PLAYER_Y + 128 >= terrain_one.start_y) and terrain_one.start_x + (
            TERRAIN_WIDTH * 70) + 10 >= PLAYER_X >= terrain_one.start_x - 100 or (
            (PLAYER_Y + 128 <= terrain_two.start_y + 5) and (
            PLAYER_Y + 128 >= terrain_two.start_y) and terrain_two.start_x + (
                    TERRAIN_WIDTH * 70)) + 10 >= PLAYER_X >= terrain_two.start_x - 100:
        return False

    else:
        return True


# Checks for collision
def is_collision(var, skull_y):
    if var == "slime":
        dist = math.sqrt((math.pow(SLIME_X - PLAYER_X, 2)) + (math.pow(SLIME_Y - PLAYER_Y, 2)))
        if dist < 150:
            return True

        else:
            return False
    if var == "skull":
        dist = math.sqrt((math.pow(SKULL_X - PLAYER_X, 2)) + (math.pow((skull_y - 40) - PLAYER_Y, 2)))
        if dist < 110:
            return True

        else:
            return False


# Initialises the game
def init():
    global TERRAIN1_X
    global TERRAIN1_Y
    global TERRAIN2_X
    global TERRAIN2_Y
    global terrain_one
    global terrain_two
    global PLAYER_X
    global PLAYER_Y
    global SLIME_X
    global SLIME_Y
    global SKULL_X
    global SKULL_Y1
    global SKULL_Y2
    global random_int
    global score
    global slime_spawnable
    global skull_spawnable
    global is_first_loop
    global is_first_run

    PLAYER_X = 125
    PLAYER_Y = 422
    TERRAIN1_X = 0
    TERRAIN1_Y = 550
    TERRAIN2_X = ((TERRAIN1_X + (6 * 70)) + 280)
    TERRAIN2_Y = TERRAIN1_Y + random.randint(-250, 100)
    terrain_one = Terrain(TERRAIN1_X, TERRAIN1_Y, TERRAIN_WIDTH)
    terrain_two = Terrain(TERRAIN2_X, TERRAIN2_Y, TERRAIN_WIDTH)
    random_int = random.randint(1, 6)
    is_first_loop = True
    is_first_run = True
    SLIME_X = terrain_two.start_x + random.randint(42, 200)
    SLIME_Y = terrain_two.start_y - 62
    random_int = random.randint(1, 6)
    slime_spawnable = False
    SKULL_X = 1400
    score = 0
    SKULL_Y1 = terrain_one.start_y - 170
    SKULL_Y2 = terrain_two.start_y - 170
    skull_spawnable = False


# Game Over screen
run = True
game_over_img = pygame.transform.scale(pygame.image.load('img/bg/gameOver.png'), (300, 300))
new_game_img = pygame.transform.scale(pygame.image.load('img/bg/new_game.png'), (200, 47))
stop_img = pygame.transform.scale(pygame.image.load('img/bg/stop.png'), (122, 47))
game_over_x = 340
game_over_y = -350


def game_over():
    counter6 = 0
    global run
    global skull_spawnable
    global slime_spawnable
    global game_over_y
    global counter5
    global PLAYER_Y

    # Game over audio
    mixer.music.load('sound/gameOver.mp3')
    mixer.music.play(-1)
    death_audio.play()
    while run:
        screen.fill('black')
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()

                if event.button == 1 and 313 <= pos_x <= 500 and 354 <= pos_y <= 393:
                    run = False
                    init()

                if event.button == 1 and 567 <= pos_x <= 673 and 357 <= pos_y <= 390:
                    exit()
        # Counter for slime
        if counter5 < 269:
            counter5 += 1

        else:
            counter5 = 0
        # Counter for dying
        if counter6 < 319:
            counter6 += 1

        else:
            counter6 = 319
        print_terrain(terrain_one.start_x, terrain_one.start_y, terrain_one.terrain_width)
        print_terrain(terrain_two.start_x, terrain_two.start_y, terrain_two.terrain_width)
        if is_falling():
            PLAYER_Y += gravity

        if PLAYER_Y > 950:
            PLAYER_Y = 950

        if game_over_y < 600:
            game_over_y += 2

        if game_over_y >= 40:
            game_over_y = 40

        # Generating a new terrain_one
        terrain_one.start_x -= terrain_speed
        terrain_two.start_x -= terrain_speed
        print_terrain(terrain_one.start_x, terrain_one.start_y, terrain_one.terrain_width)
        print_terrain(terrain_two.start_x, terrain_two.start_y, terrain_two.terrain_width)
        if terrain_one.start_x <= (terrain_one.terrain_width * -70):
            skull_spawnable = True
            terrain_one.start_x = 1050
            terrain_one.start_y = terrain_two.start_y + random.randint(-TERRAIN_GAP, TERRAIN_GAP)

            if terrain_one.start_y > 650:
                terrain_one.start_y = 650

            if terrain_one.start_y < 250:
                terrain_one.start_y = 250

        # Generating a new terrain_two
        if terrain_two.start_x <= (-70 * terrain_two.terrain_width):
            slime_spawnable = True
            skull_spawnable = True
            terrain_two.start_x = 1050
            terrain_two.start_y = terrain_one.start_y + random.randint(-TERRAIN_GAP, TERRAIN_GAP)

            if terrain_two.start_y > 650:
                terrain_two.start_y = 650

            if terrain_two.start_y < 250:
                terrain_two.start_y = 250

        score2 = font.render("SCORE : " + str(score), True, 'red')
        screen.blit(score2, (textX, textY))
        screen.blit(new_game_img, (310, 350))
        screen.blit(stop_img, (560, 350))
        screen.blit(player_die_img[counter6 // 80], (PLAYER_X, PLAYER_Y))
        screen.blit(game_over_img, (game_over_x, game_over_y))
        pygame.display.update()


# Terrain
# Configure Terrain color : 'green', 'pink', 'orange'       | Default = 'green'
terrain_color = "pink"
# Configure terrain speed                                   | Default = '1.8'
terrain_speed = 1.8
terrain_img = pygame.transform.scale(pygame.image.load(f'img/terrain/Terrain_{terrain_color}.png'), (70, 70))
TERRAIN_GAP = 350
TERRAIN1_X = 0
TERRAIN1_Y = 550
TERRAIN2_X = ((TERRAIN1_X + (6 * 70)) + 280)
TERRAIN2_Y = TERRAIN1_Y + random.randint(-250, 100)
TERRAIN_WIDTH = 6
terrain_one = Terrain(TERRAIN1_X, TERRAIN1_Y, TERRAIN_WIDTH)
terrain_two = Terrain(TERRAIN2_X, TERRAIN2_Y, TERRAIN_WIDTH)

# Start text image
start_text1_img = pygame.transform.scale(pygame.image.load(f'img/bg/text1_{terrain_color}.png'), (400, 32.6))
start_text2_img = pygame.transform.scale(pygame.image.load(f'img/bg/text2_{terrain_color}.png'), (330, 27))

# Slime
SLIME_X = terrain_two.start_x + random.randint(42, 200)
SLIME_Y = terrain_two.start_y - 62
slime_speed = 2.5
random_int = random.randint(1, 6)
slime_spawnable = False

# Skull
SKULL_X = 1400
SKULL_Y1 = terrain_one.start_y - 170
SKULL_Y2 = terrain_two.start_y - 170
skull_spawnable = False

# game loop
score = 0
gravity = 1.3
jump_height = 0
jump_count = 0
jump = False
running = True
is_first_loop = True
is_first_run = True

while running:
    # bg_audio.play()
    screen.fill('black')
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_RETURN:
                is_first_loop = False

            if event.key == pygame.K_SPACE and not is_first_loop and jump_count < 2:
                jump_audio.play()
                jump = True

    # Pre game-start
    if is_first_loop:
        print_terrain(terrain_one.start_x, terrain_one.start_y, terrain_one.terrain_width)
        print_terrain(terrain_two.start_x, terrain_two.start_y, terrain_two.terrain_width)
        screen.blit(start_text1_img, (300, 200))
        screen.blit(start_text2_img, (335, 260))
        print_player(PLAYER_X, PLAYER_Y, "stand")
        # Flag
        FLAG_X = 300
        FLAG_Y = 450
        print_start_flag(FLAG_X, FLAG_Y)

    # Post game-start
    else:
        terrain_one.start_x -= terrain_speed
        terrain_two.start_x -= terrain_speed
        print_terrain(terrain_one.start_x, terrain_one.start_y, terrain_one.terrain_width)
        print_terrain(terrain_two.start_x, terrain_two.start_y, terrain_two.terrain_width)

        # Generating a new terrain_one
        if terrain_one.start_x <= (terrain_one.terrain_width * -70):
            skull_spawnable = True
            terrain_one.start_x = 1050
            score += 1
            terrain_one.start_y = terrain_two.start_y + random.randint(-TERRAIN_GAP, TERRAIN_GAP)
            if terrain_one.start_y > 650:
                terrain_one.start_y = 650

            if terrain_one.start_y < 250:
                terrain_one.start_y = 250
            is_first_run = False

        # Generating a new terrain_two
        if terrain_two.start_x <= (-70 * terrain_two.terrain_width):
            slime_spawnable = True
            skull_spawnable = True
            terrain_two.start_x = 1050
            score += 1
            terrain_two.start_y = terrain_one.start_y + random.randint(-TERRAIN_GAP, TERRAIN_GAP)

            if terrain_two.start_y > 650:
                terrain_two.start_y = 650

            if terrain_two.start_y < 250:
                terrain_two.start_y = 250

        if is_first_run and terrain_one.start_x >= (terrain_one.terrain_width * -70):
            print_start_flag(FLAG_X, FLAG_Y)
            FLAG_X -= terrain_speed

        if not is_falling() and not jump:
            jump_count = 0
            print_player(PLAYER_X, PLAYER_Y, "run")

        if is_falling() and not jump:
            print_player(PLAYER_X, PLAYER_Y, "fall")
            PLAYER_Y += gravity

        if jump:
            jump_height += 1
            PLAYER_Y -= 3
            print_player(PLAYER_X, PLAYER_Y, "jump")

            if PLAYER_Y < 0:
                PLAYER_Y = 0

            # Configure jump height     | Default = '75'
            if jump_height == 75:
                jump_count += 1
                jump_height = 0
                jump = False
    counter()
    print_score()
    if slime_spawnable:
        random_int = random.randint(1, 7)
        SLIME_X = terrain_two.start_x + random.randint(300, 400)
        SLIME_Y = terrain_two.start_y - 62
        slime_spawnable = False

    if skull_spawnable:
        SKULL_X = 1400
        SKULL_Y1 = terrain_one.start_y - 170
        SKULL_Y2 = terrain_two.start_y - 170
        skull_spawnable = False

    # 28.5% possibility for only slime spawns
    # 14.25% possibility for only skull spawns
    # 14.25% possibility for slime and skull spawns
    turn = False
    if random_int == 3 or random_int == 4 or random_int == 7:
        if is_first_loop:
            print_enemy(SLIME_X, SLIME_Y, "slime")

        else:
            print_enemy(SLIME_X, SLIME_Y, "slime")
            SLIME_X -= terrain_speed

    if random_int % 6 == 0 or random_int == 7:

        if not is_first_loop and terrain_one.start_x > terrain_two.start_x:
            print_enemy(SKULL_X, SKULL_Y1, "skull")

            if is_collision("skull", SKULL_Y1):
                game_over()
            SKULL_X -= terrain_speed + 1.6

        if not is_first_loop and terrain_two.start_x > terrain_one.start_x and not is_first_run:
            print_enemy(SKULL_X, SKULL_Y2, "skull")

            if is_collision("skull", SKULL_Y2):
                game_over()
            SKULL_X -= terrain_speed + 1.6

    if is_collision("slime", -1):
        running = False
        game_over()

    if PLAYER_Y >= 850:
        game_over()
    pygame.display.update()
