import pygame
import circleshape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS
)

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt