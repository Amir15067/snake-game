import os,pygame
class Score:
    def __init__(self):
        self.scoore = 0
        self.high_score = self.load()
        self.fount = pygame.font.SysFont('Arial', 30)
        self.clock = pygame.time.Clock()

    def load(self):
        if not os.path.exists("highscore.txt"):
            with open("highscore.txt", "w") as file:
                file.write("0")
   
        with open("highscore.txt", "r") as file:
            return int(file.read())
        
    def save(self):
        if self.high_score < self.scoore:
            with open("highscore.txt", "w") as file:
                file.write(str(self.scoore))
        else:
            pass
    def sum_score(self):
        self.scoore += 1
    def draw(self,screen):
        text1 = self.fount.render(f"score : {self.scoore}", True, (0,0,0))
        text2 = self.fount.render(f"high_score : {self.high_score}", True, (0,0,0))
        screen.blit(text1, (10,10))
        screen.blit(text2, (10,40))
    def cheak(self):
        if self.scoore >= 5 and self.scoore <= 10:
            self.clock.tick(100)