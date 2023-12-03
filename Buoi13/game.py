import pygame

pygame.init()

pygame.display.set_caption("Rua va Tho")

canvas = pygame.display.set_mode((600, 600))

BG_COLOR = (70, 95, 70)

clock = pygame.time.Clock()

loop = True

paddle_image = pygame.image.load("Buoi13/assets/paddle.png")
ball_image = pygame.image.load("Buoi13/assets/ball.png")

# x1, y1 la toa do cua paddle ben trai
x1 = 0
y1 = 250

# x2, y2 la toa do cua paddle ben phai
x2 = 570
y2 = 250

w_pressed = False

while loop:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        elif (e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_w):
                w_pressed = True        
    if (y1 <= 0):
        w_pressed = False
    
    if (w_pressed == True):
        y1 += -5  

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))

    clock.tick(60)
    pygame.display.flip()
