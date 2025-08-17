import pygame,sys

from food import Food
from score import Score
from snake import Snake



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption("snake game")
        self.clock = pygame.time.Clock()
        self.snake = Snake((136,12,0), 20)
        self.food = Food(780,380,20)
        self.score = Score()
        self.count = 0
        self.running = True
   
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP:
                    self.snake.chenge_direction("UP")
                elif events.key == pygame.K_LEFT:
                    self.snake.chenge_direction("LEFT")
                elif events.key == pygame.K_RIGHT:
                    self.snake.chenge_direction("RIGHT")
                elif events.key == pygame.K_DOWN:
                    self.snake.chenge_direction("DOWN")
    def update(self):
        self.snake.move()
        self.count += 1
        if self.snake.body[-1] == self.food.position:
            self.snake.grow()
            self.food.relocation()
            self.score.sum_score()
        if self.snake.crash(800,400):
            self.running = False

            self.score.save()
    def draw(self):
        self.screen.fill((86,111,112))
        self.snake.draw(self.screen)
        self.score.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            if self.score.scoore >= 0 and self.score.scoore < 5:
                self.clock.tick(10)
            elif self.score.scoore >= 5 and self.score.scoore < 10:
                self.clock.tick(12)
            elif self.score.scoore <= 10 and self.score.scoore < 15:
                self.clock.tick(14)
            elif self.score.scoore <= 15 and self.score.scoore < 20:
                self.clock.tick(16)
            elif self.score.scoore <= 20 and self.score.scoore < 25:
                self.clock.tick(18)
            elif self.score.scoore <= 25 and self.score.scoore < 30:
                self.clock.tick(20)
            elif self.score.scoore <= 30 and self.score.scoore < 35:
                self.clock.tick(22)    
            elif self.score.scoore <= 35 and self.score.scoore < 40:
                self.clock.tick(24)
        pygame.quit()
       
                
