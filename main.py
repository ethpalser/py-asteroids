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

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color = (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        time_since = clock.tick(60) # pause until 1/60 of second passes
        dt = time_since / 1000

if __name__ == "__main__":
    main()