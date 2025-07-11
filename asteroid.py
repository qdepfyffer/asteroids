import pygame
import random
from circleshape import CircleShape
from constants import *
from math import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.__num_sides = random.randrange(3, 12)
        self.__leeway = 50 // self.__num_sides
        self.__rotation_direction = random.choice([-1, +1])

    def draw(self, screen):
        pts = []
        angle_offset = radians(self.rotation)
        for i in range(self.__num_sides):
            # base angle around circle
            θ = i / self.__num_sides * tau
            # add the current rotation (in radians)
            θ += angle_offset
            x = cos(θ) * self.radius + self.position.x
            y = sin(θ) * self.radius + self.position.y
            pts.append((x, y))
        pygame.draw.polygon(screen, "white", pts, 1)


    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rotation += ASTEROID_TURN_SPEED * (dt * self.__rotation_direction)

    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        if distance + self.__leeway < (self.radius + other.radius):
            return True
        return False

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0, 50.0)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = v2 * 1.2
