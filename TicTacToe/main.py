import pygame

# initialise the pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((288, 288))

# background image
background = pygame.image.load('img/board.jpg')

# title and icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load('img/tictactoe.png')
pygame.display.set_icon(icon)

# x o img
img_x = pygame.image.load("img/x.png")
img_o = pygame.image.load("img/o.png")

# x list
list_x = []

# o list
list_o = []

# blocks
block = [
    [19, 19],  # 1
    [114, 19],  # 2
    [209, 19],  # 3
    [19, 114],  # 4
    [114, 114],  # 5
    [209, 114],  # 6
    [19, 209],  # 7
    [114, 209],  # 8
    [209, 209],  # 9
]


# print x o
def print_X(x_x, y_x):
    screen.blit(img_x, (x_x, y_x))


def print_O(x_o, y_o):
    screen.blit(img_o, (x_o, y_o))


# check if empty
def is_empty(i):
    indx = 0
    while indx < step_x:
        if list_x[indx] == i:
            return False
        indx += 1
    indx = 0
    while indx < step_o:
        if list_o[indx] == i:
            return False
        indx += 1
    return True

# check for winner
def check_win():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(pos in list_x for pos in combo):
            return "X"
        elif all(pos in list_o for pos in combo):
            return "O"

    # If no one has won and all cells are filled, it's a draw
    if step_x + step_o == 9:
        return "Draw"

    # If the game is still ongoing
    return None

def get_position(x, y):
    k = -1
    if 0 < x < 96 and 0 < y < 96:
        k = 0
    elif 192 > x > 96 > y > 0:
        k = 1
    elif 192 < x < 288 and 0 < y < 96:
        k = 2
    elif 0 < x < 96 < y < 192:
        k = 3
    elif 96 < x < 192 and 96 < y < 192:
        k = 4
    elif 288 > x > 192 > y > 96:
        k = 5
    elif 0 < x < 96 and 192 < y < 288:
        k = 6
    elif 96 < x < 192 < y < 288:
        k = 7
    elif 192 < x < 288 and 192 < y < 288:
        k = 8
    return k


running = True
step_x = 0
step_o = 0
Turn = "X"
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and Turn == "X":
                x, y = pygame.mouse.get_pos()
                i = get_position(x, y)
                if is_empty(i):
                    list_x.append(i)
                    step_x += 1
                    Turn = "O"
            elif event.button == 1 and Turn == "O":
                x, y = pygame.mouse.get_pos()
                i = get_position(x, y)
                if is_empty(i):
                    list_o.append(i)
                    step_o += 1
                    Turn = "X"
            # print("steps : " + str(step_x + step_o))

    index = 0
    while index < step_x and step_x > 0:
        a, b = block[list_x[index]]
        print_X(a, b)
        index += 1
    index = 0
    while index < step_o and step_o > 0:
        a, b = block[list_o[index]]
        print_O(a, b)
        index += 1

    winner = check_win()

    # X Wins
    if winner == "X":
        print("Player X wins!")
        while running:
            win_background = pygame.image.load("img/win.jpg")
            screen.fill((0, 0, 0))
            screen.blit(win_background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            font = pygame.font.Font('freesansbold.ttf', 32)
            over_font = pygame.font.Font('freesansbold.ttf', 50)
            over_text = font.render("GAME OVER!", True, (255, 153, 51))
            over_text2 = font.render("X WINS", True, (255, 153, 51))
            screen.blit(over_text, (40, 80))
            screen.blit(over_text2,(80,125))
            pygame.display.update()

    # O Wins
    elif winner == "O":
        print("Player O wins!")
        while running:
            win_background = pygame.image.load("img/win.jpg")
            screen.fill((0, 0, 0))
            screen.blit(win_background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            font = pygame.font.Font('freesansbold.ttf', 32)
            over_font = pygame.font.Font('freesansbold.ttf', 50)
            over_text = font.render("GAME OVER!", True, (255, 153, 51))
            over_text2 = font.render("O WINS", True, (255, 153, 51))
            screen.blit(over_text, (40, 80))
            screen.blit(over_text2,(80,125))
            pygame.display.update()
        break

    # It's a draw
    elif winner == "Draw":
        print("It's a draw!")
        while running:
            win_background = pygame.image.load("img/win.jpg")
            screen.fill((0, 0, 0))
            screen.blit(win_background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            font = pygame.font.Font('freesansbold.ttf', 32)
            over_font = pygame.font.Font('freesansbold.ttf', 50)
            over_text = font.render("GAME OVER!", True, (255, 153, 51))
            over_text2 = font.render("IT'S A DRAW", True, (255, 153, 51))
            screen.blit(over_text, (40, 80))
            screen.blit(over_text2,(40,125))
            pygame.display.update()
    pygame.display.update()
