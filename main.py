import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock()

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