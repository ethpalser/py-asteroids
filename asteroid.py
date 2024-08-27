import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity_left = self.velocity.rotate(-random_angle)
        velocity_right = self.velocity.rotate(random_angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        
        spawn1 = Asteroid(self.position.x, self.position.y, new_size)
        spawn1.velocity = velocity_left * 1.2

        spawn2 = Asteroid(self.position.x, self.position.y, new_size)
        spawn2.velocity = velocity_right * 1.2