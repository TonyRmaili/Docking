import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Define colors
blue = (0, 0, 255)
red = (255, 0, 0)

# Square properties
square_size = 50
x, y = width // 2, height // 2
speed = 5

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill the screen with blue
    screen.fill(blue)

    # Draw the red square
    pygame.draw.rect(screen, red, (x, y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
