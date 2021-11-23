import random

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
SKY_BLUE = (52, 229, 255)
WINTERSKY_PINK = (238, 38, 119)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<Your Title Here>>"

class Block(pygame.sprite.Sprite):
    """"Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surgace that is the visual
            representation of out Block
        rect: numerical representation of out Block [x, y, width, height]
        """
    def __init__(self, color: tuple, width: int, height: int):
        """
        Argumants
        :param color: 3-tuple (r,g,b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100

    #Create the Player block
    player = Block(SKY_BLUE, 20, 15)

    # Create a group of sprites to store ALL SPRITES
    allSprite = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block (set its parameters)
        block = Block(BLACK, 20, 15)
        # Set a random location fro the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprite Group

        # Add the block to the all_sprite Group
        block_sprites.add(block)
        allSprite.add(block)

    # Add the Player to allSprites group
    allSprite.add(player)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        mousePos = pygame.mouse.get_pos()
        player.rect = mousePos
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw all sprites
        allSprite.draw(screen)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()