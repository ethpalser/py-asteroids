# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    init_result = pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update game state
        for obj in updatable:
            obj.update(dt)
        
        # check collision
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                exit()
        
        # rendering
        screen.fill(color = (0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # pause until 1/60 of second passes
        time_since = clock.tick(60)
        dt = time_since / 1000

if __name__ == "__main__":
    main()