import pygame
from random import randint

pygame.init()

clock = pygame.time.Clock()

W = 600
H = 600
screen = pygame.display.set_mode((W, H))

BG = 0, 50, 80
color = 255, 255, 0

small_font = pygame.font.SysFont("Arial", 25)
large_font = pygame.font.SysFont("Arial", 62)

# loading images
img_list = []
scale = 0.2
rock_img = pygame.image.load('rock.png')
rock_w = rock_img.get_width()
rock_h = rock_img.get_height()
paper_img = pygame.image.load('paper.png')
paper_w = paper_img.get_width()
paper_h = paper_img.get_height()
scissors_img = pygame.image.load('scissors.png')
scissors_w = scissors_img.get_width()
scissors_h = scissors_img.get_height()
rock_img = pygame.transform.scale(rock_img, (rock_w * scale, rock_h * scale))
paper_img = pygame.transform.scale(paper_img,(paper_w * scale, paper_h * scale))
scissors_img = pygame.transform.scale(scissors_img, (scissors_w * scale, scissors_h * scale))
img_list.extend((rock_img, paper_img, scissors_img))

my_choice = None
c_choice = None
my_rock = False
my_paper = False
my_scissors = False

roll_text = small_font.render("Choose an item", True, (100, 100, 255))
draw_text = small_font.render("Draw", True, (100, 100, 255))
you_won_text = small_font.render("You won", True, (255, 255, 0))
c_won_text = small_font.render("Computer won", True, (255, 0, 0))


def set_initial_par():
    global my_choice, c_choice, my_rock, my_paper, my_scissors
    my_choice = None
    c_choice = None
    my_rock = False
    my_paper = False
    my_scissors = False


set_initial_par()

run = True

while run:

    clock.tick(10)

    screen.fill(BG)

    pos = pygame.mouse.get_pos()

    screen.blit(roll_text, (220, 10))

    if 120 < pos[0] < 120 + rock_w * scale and 70 < pos[1] < 70 + rock_h * scale or my_rock:
        pygame.draw.rect(screen, color, pygame.Rect(120 - 3, 70 - 3, rock_w * scale + 6, rock_h * scale + 6))
    if 270 < pos[0] < 270 + paper_w * scale and 70 < pos[1] < 70 + paper_h * scale or my_paper:
        pygame.draw.rect(screen, color, pygame.Rect(270 - 3, 70 - 3, paper_w * scale + 6, paper_h * scale + 6))
    if 420 < pos[0] < 420 + scissors_w * scale and 70 < pos[1] < 70 + scissors_h * scale or my_scissors:
        pygame.draw.rect(screen, color, pygame.Rect(420 - 3, 70 - 3, scissors_w * scale + 6, scissors_h * scale + 6))

    # my items
    screen.blit(rock_img, (120, 70))
    screen.blit(paper_img, (270, 70))
    screen.blit(scissors_img, (420, 70))

    if c_choice == 0:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(120 - 3, 370 - 3, rock_w * scale + 6, rock_h * scale + 6))
        if my_choice == 0:
            screen.blit(draw_text, (290, 260))
        elif my_choice == 1:
            screen.blit(you_won_text, (250, 260))
        elif my_choice == 2:
            screen.blit(c_won_text, (230, 260))

    elif c_choice == 1:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(270 - 3, 370 - 3, paper_w * scale + 6, paper_h * scale + 6))
        if my_choice == 0:
            screen.blit(c_won_text, (230, 260))
        elif my_choice == 1:
            screen.blit(draw_text, (290, 260))
        elif my_choice == 2:
            screen.blit(you_won_text, (250, 260))
    elif c_choice == 2:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(420 - 3, 370 - 3, scissors_w * scale + 6, scissors_h * scale + 6))
        if my_choice == 0:
            screen.blit(you_won_text, (250, 260))
        elif my_choice == 1:
            screen.blit(c_won_text, (230, 260))
        elif my_choice == 2:
            screen.blit(draw_text, (270, 260))

    # computer items
    screen.blit(rock_img, (120, 370))
    screen.blit(paper_img, (270, 370))
    screen.blit(scissors_img, (420, 370))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                set_initial_par()
        if event.type == pygame.MOUSEBUTTONDOWN and 120 < pos[0] < 120 + rock_w * scale and 70 < pos[1] < 70 + rock_h * scale:
            my_rock = True
            my_paper = False
            my_scissors = False
            my_choice = 0
            c_choice = randint(0, 2)
            if c_choice == 0:
                print("Draw")
            elif c_choice == 1:
                print("Computer won")
            elif c_choice == 2:
                print("You won")
        if event.type == pygame.MOUSEBUTTONDOWN and 270 < pos[0] < 270 + paper_w * scale and 70 < pos[1] < 70 + paper_h * scale:
            my_rock = False
            my_paper = True
            my_scissors = False
            my_choice = 1
            c_choice = randint(0, 2)
            if c_choice == 0:
                print("You won")
            elif c_choice == 1:
                print("Draw")
            elif c_choice == 2:
                print("Computer won")
        if event.type == pygame.MOUSEBUTTONDOWN and 420 < pos[0] < 420 + scissors_w * scale and 70 < pos[1] < 70 + scissors_h * scale:
            my_rock = False
            my_paper = False
            my_scissors = True
            my_choice = 2
            c_choice = randint(0, 2)
            if c_choice == 0:
                print("Computer won")
            elif c_choice == 1:
                print("You won")
            elif c_choice == 2:
                print("Draw")

    pygame.display.flip()

