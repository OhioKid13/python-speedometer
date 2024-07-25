import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Speedometer')

# Load images with transparency support
needle = pygame.image.load('needle_transparent.png').convert_alpha()
circle = pygame.image.load('assets/circle.png').convert_alpha()

# Resize the needle to be half its original size
needle = pygame.transform.scale(needle, (needle.get_width() // 2, needle.get_height() // 2))

# Define the center of the circle and initial angle for the needle
circle_center = (window_size[0] // 2, window_size[1] // 2)
needle_angle = 0  # Initial angle

# Define the maximum and minimum angles for the needle
min_angle = -90  # leftmost position
max_angle = 90   # rightmost position

# Function to rotate the needle
def rotate_image(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses to adjust the needle angle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and needle_angle > min_angle:
        needle_angle -= 1  # Decrease angle to move needle left
    if keys[pygame.K_RIGHT] and needle_angle < max_angle:
        needle_angle += 1  # Increase angle to move needle right

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circle
    screen.blit(circle, circle.get_rect(center=circle_center))

    # Rotate and draw the needle
    rotated_needle, needle_rect = rotate_image(needle, needle_angle, circle_center)
    screen.blit(rotated_needle, needle_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
sys.exit()
