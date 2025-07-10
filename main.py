import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Get new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create pygame clock and initialize delta time (dt)
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:

        # Listen for quit event to break out of main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # Tick game time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
