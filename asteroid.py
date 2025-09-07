import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_of_split = random.uniform(20, 50)
        asteroid_angle1 = pygame.Vector2(self.position.x, self.position.y).rotate(angle_of_split)
        asteroid_angle2 = pygame.Vector2(self.position.x, self.position.y).rotate(-angle_of_split)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_1.velocity = asteroid_angle1
        spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_2.velocity = asteroid_angle2
