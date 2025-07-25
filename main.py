import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create asteroid field
    field = AsteroidField()

    # Main game loop
    while True:

        # Listen for quit event to break out of main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for entity in drawable:
            # pygame.draw.circle(screen, "red", entity.position, entity.radius, 2)  # Draw hitboxes
            entity.draw(screen)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                exit(0)
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(144) / 1000


if __name__ == "__main__":
    main()
