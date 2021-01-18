import pygame
pygame.init()
b = pygame.image.load('background.png')
menu = pygame.image.load('menu(temp.).png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("log jumper")
icon = pygame.image.load('log.png')
pygame.display.set_icon(icon)
tree = pygame.image.load('log 2.png')
tx_change = -0.8
tx = 740
ty = 480
player = pygame.image.load('man.png')
py_change = 1.5
px = 40
py = 480
tree2 = pygame.image.load('log 2.png')
tx2_change = -0.8
tx2 = 540
ty2 = 480
tree_3 = pygame.image.load('log 2.png')
tx3_change = -0.8
tx3 = 340
ty3 = 480
gameover = pygame.image.load('game over.png')

pygame.mixer.music.load('Morning_Run.wav')
pygame.mixer.music.play(-1)


def tree1(x, y):
    screen.blit(tree, (x, y))


def tree_2(x, y):
    screen.blit(tree2, (x, y))


def tree3(x, y):
    screen.blit(tree_3, (x, y))


def p1(x, y):
    screen.blit(player, (x, y))


game_over = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                py_change = -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    tx += tx_change
    py += py_change
    tx2 += tx2_change
    tx3 += tx3_change
    if py >= 480:
        py = 480
    if py <= 360:
        py_change = 1
    if tx <= 0:
        tx = 740
    if tx2 <= 0:
        tx2 = 740
    if tx3 <= 0:
        tx3 = 740
    if px >= tx and py >= ty:
        game_over = True
        if game_over:
            tx_change = 0
            tx2_change = 0
            tx3_change = 0
    if px >= tx2 and py >= ty2:
        game_over = True
        if game_over:
            tx_change = 0
            tx2_change = 0
            tx3_change = 0
    if px >= tx3 and py >= ty3:
        game_over = True
        if game_over:
            tx_change = 0
            tx2_change = 0
            tx3_change = 0
    screen.fill((0, 0, 0))
    screen.blit(b, (0, 0))
    tree1(tx, ty)
    tree_2(tx2, ty2)
    tree3(tx3, ty3)
    p1(px, py)
    screen.blit(menu, (0, 0))
    pygame.display.update()
