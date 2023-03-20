import pygame
from sys import exit

WIDTH, HEIGHT = 600, 500
TITLE = "Test "

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()



def draw():
    pass


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # game code

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    main()
