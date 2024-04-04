import math
import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My game")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
font = pygame.font.SysFont('Arial', 25, True, False)
text = font.render('Welcome to my Game', True, (0, 0, 0))
# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

    # ----- DRAWING -----
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.line(screen, (0, 255, 0), [10, 10], [10, 100], 5)
    pygame.draw.rect(screen, (0, 0, 0), [20, 20, 250, 100], 2)
    pygame.draw.ellipse(screen, (0, 0, 255), [20, 20, 250, 100], 3)
    pygame.draw.circle(screen, (255, 0, 0), [400, 350], 75)
    pygame.draw.arc(screen, (100, 100, 100), [200, 200, 150, 150], math.pi/2, math.pi, 2)
    pygame.draw.polygon(screen, (230, 182, 38), [[600, 10], [450, 50], [650, 70]], 2)
    screen.blit(text, [300, 100])
    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()