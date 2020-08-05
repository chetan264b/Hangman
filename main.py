import pygame
import random
import math

# initialize window
pygame.init()

words = ['CHETAN', 'CRICKET', 'DEVELOPER', 'ELEPHANT','PYGAME', 'PYTHON']

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Hangman Game")

logo = pygame.image.load('hangman.png')
pygame.display.set_icon(logo)
Letter_font = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans',70)
mode = True
state = 0
image = []
word = words[random.randint(0,5)]
guessed= []
for i in range(7):
    image.append(pygame.image.load('hangman' + str(i) + '.png'))

print(image)
letter= []
xs=43
ys=440
A=65
for i in range(26):
    if i ==13:
        xs=43
        ys=500
    letter.append([xs,ys,chr(A+i),True])
    xs+=60
def draw_game():
    screen.blit(image[state], (100, 150))
    # X=43
    # Y=440
    # A = 65
    display_word=""
    for j in word:
        if j in guessed:
            display_word += j + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,(0,0,0))
    screen.blit(text,(400,200))

    for i in range(26):
        if letter[i][3]:
            x,y,C=letter[i][0],letter[i][1],letter[i][2]
            pygame.draw.circle(screen, (0, 0, 0), (x,y), 20, 3)
            text = Letter_font.render(C, 1, (0, 0, 0))
            screen.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

running = True

while (running):
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            m_x, m_y = pygame.mouse.get_pos()
            for i in range(26):
                if letter[i][3]:
                    x,y,A=letter[i][0],letter[i][1],letter[i][2]
                    dist = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dist<20:
                        print(A)
                        letter[i][3]=False
                        if A in word:
                            guessed.append(A)
                        else:
                            if state==5:
                                screen.fill((255, 255, 255))
                                screen.blit(pygame.image.load('hangman6.png'), (100, 150))
                                text = WORD_FONT.render("YOU LOSE!!!", 1, (0, 0, 0))
                                screen.blit(text,(325, 265))
                                pygame.display.update()
                                pygame.time.delay(3000)
                                pygame.quit()
                            state+=1
    # screen.blit(cell,(200,300))
    won= True
    for i in word:
        if i not in guessed:
            won = False
            break
    if won:
        screen.fill((255,255,255))
        screen.blit(pygame.image.load('congratulation.png'), (100, 250))
        text=WORD_FONT.render("YOU WON!!!",1,(0,0,0))
        screen.blit(text,(325,265))
        pygame.display.update()
        pygame.time.delay(3000)
        break
    if mode:
        draw_game()

    pygame.display.update()
