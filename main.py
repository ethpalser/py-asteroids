# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    init_result = pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    for container in Player.containers:
        container.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update game state
        for obj in updatable:
            obj.update(dt)
        
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