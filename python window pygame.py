import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock()

class Sprite:
    def __init__(self,img:pygame.Surface,pos:tuple = (400,300), color:tuple = (0, 0, 255)):
        super().__init__()
        self.pos = pos
        self.color = color
        self.rotate = 0
        self.base_image = img
        self.size = 1
    
    def draw(self, surface:pygame.Surface):
        image = pygame.transform.rotozoom(self.base_image, self.rotate, self.size)
        rect = image.get_rect(center=self.pos)
        surface.blit(image, rect.topleft)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill((255, 255, 255)) 
        pygame.display.flip()    
        clock.tick(60)         
        
if __name__ == "__main__":
    sys.exit(int(main()) or 0)