import pygame
import time
import random

pygame.init()

# Definiowanie kolorów
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# Parametry ekranu
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ChatGPT')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Czcionki
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
time_font = pygame.font.SysFont("bahnschrift", 25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def show_time(start_time):
    elapsed_time = int(time.time() - start_time)
    time_text = time_font.render("Time: " + str(elapsed_time) + "s", True, white)
    dis.blit(time_text, [dis_width - 150, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def fill_screen_with_snake():
    dis.fill(black)
    x, y = 0, 0
    direction = 'RIGHT'
    length = 1
    snake_list = [[x, y]]

    while length < (dis_width // snake_block) * (dis_height // snake_block):
        if direction == 'RIGHT':
            x += snake_block
            if x >= dis_width or [x, y] in snake_list:
                x -= snake_block
                y += snake_block
                direction = 'DOWN'
        elif direction == 'DOWN':
            y += snake_block
            if y >= dis_height or [x, y] in snake_list:
                y -= snake_block
                x -= snake_block
                direction = 'LEFT'
        elif direction == 'LEFT':
            x -= snake_block
            if x < 0 or [x, y] in snake_list:
                x += snake_block
                y -= snake_block
                direction = 'UP'
        elif direction == 'UP':
            y -= snake_block
            if y < 0 or [x, y] in snake_list:
                y += snake_block
                x += snake_block
                direction = 'RIGHT'

        snake_list.append([x, y])
        length += 1

        if length % 2 == 1:  # Dodanie odstępu co drugi krok
            our_snake(snake_block, snake_list)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            time.sleep(0.01)

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    start_time = time.time()

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            show_time(start_time)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

            fill_screen_with_snake()
            game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        show_time(start_time)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
