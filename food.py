import random, pygame
class Food:
    def __init__(self,wight,hight,size):
        self.size = size
        self.wight = wight
        self.hight = hight
        self.color = (96, 60 , 168)
        self.relocation()
    def relocation(self):
        col = self.wight // self.size
        row = self.hight // self.size
        
        self.position = (random.randint(0, col-1) * self.size,random.randint(0,row-1) * self.size)

    def draw(self,screen):
        rec =pygame.Rect(self.position[0],self.position[1],self.size, self.size)
        pygame.draw.rect(screen,self.color,rec)