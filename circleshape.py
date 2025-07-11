import pygame
from math import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):  # overridden by subclasses
        pass

    def update(self, dt):  # overriden by subclass
        pass

    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        if distance < (self.radius + other.radius):
            return True
        return False