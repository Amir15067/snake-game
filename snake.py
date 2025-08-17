import pygame

class Snake:
    def __init__(self,color,size):
        self.size = size
        self.color = color
        self.body = [(100,100), (120,100), (140,100)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[-1]
        if self.direction == "UP":
            y -= self.size
        elif self.direction == "DOWN":
            y += self.size
        elif self.direction == "LEFT":
            x -= self.size
        elif self.direction == "RIGHT":
            x += self.size
        self.body.append((x,y))
        self.body.pop(0)
    def grow(self):
        x, y = self.body[-1]
        if self.direction == "UP":
            y -= self.size
        elif self.direction == "DOWN":
            y += self.size
        elif self.direction == "LEFT":
            x -= self.size
        elif self.direction == "RIGHT":
            x += self.size
        self.body.append((x, y))
    def chenge_direction(self,new_directin):
        opposite = {
            "RIGHT" : "LEFT",
            "UP" : "DOWN",
            "LEFT": "RIGHT",
            "DOWN": "UP",
        }
        if new_directin != opposite.get(self.direction):
            self.direction = new_directin
        else:
            pass
    def draw(self,screen):
        for segment in self.body:
            rec = pygame.Rect(segment[0], segment[1], self.size, self.size)
            pygame.draw.rect(screen,self.color,rec)

    def crash(self,weight,height):
        head = self.body[-1]
        if head[0] < 0 or head[1] < 0 or head[0] >= weight or head[1] >= height :
            return True
        if head in self.body[:-1]:
            return True
        return False
