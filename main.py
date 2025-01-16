import pygame
from sys import exit 
from random import randint
from math import sqrt
pygame.init()
pygame.display.set_icon(pygame.image.load("flapflap.png"))
pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((400, 700))
background = pygame.image.load("bg.png")
ground = pygame.image.load("ground.png")
bird1 = pygame.image.load("bird1.png")
bird2 = pygame.image.load("bird2.png")
bird3 = pygame.image.load("bird3.png")
pipe = pygame.image.load("pipe.png")
pipe_reverse = pygame.transform.rotate(pygame.image.load("pipe.png"), 180)
score_sound = pygame.mixer.Sound("Score sound.wav")
flap_sound = pygame.mixer.Sound("Flap Sound.wav")
death_sound = pygame.mixer.Sound("Death sound.wav")
score = 0
white_counter = 0
class pipes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def spawner(self):
        screen.blit(pipe, (self.x, self.y))
        screen.blit(pipe_reverse, (self.x, self.y - 750))
        if self.x < -70:
            self.x = 630
            self.y = randint(200,450)
pipe1 = pipes(400,randint(200,450))
pipe2 = pipes(630,randint(200,450))
pipe3 = pipes(860,randint(200,450))
groundX = 0
speed = 0
playing = True
press = False
count = 0
count1 = 0
time = 0
birdY = 300
game = True
score_font = pygame.font.Font("freesansbold.ttf", 40)
sound_counter = 0
def score_func():
    score_text = score_font.render(str(score),True, (255,255,255))
    screen.blit(score_text, (185, 40))
while True: 
    if birdY > 560:
        game = False
        bird_array = [pygame.transform.rotate(bird1, -90), pygame.transform.rotate(bird1, -90), pygame.transform.rotate(bird1, -90)]
        birdY = 560
    else:
        if press == True:
            bird_array = [pygame.transform.rotate(bird1, 35), pygame.transform.rotate(bird2, 35), pygame.transform.rotate(bird3, 35)]
        elif press == False:
            count1 += 1
            if count1 > 11:
                bird_array = [pygame.transform.rotate(bird1, -50), pygame.transform.rotate(bird2, -50), pygame.transform.rotate(bird3, -50)]
            else:
                bird_array = [pygame.transform.rotate(bird1, 30), pygame.transform.rotate(bird2, 30), pygame.transform.rotate(bird3, 30)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game == True:
                    flap_sound.play()
                    press = True
                    birdY -= 80
                    count1 = 0
        elif event.type == pygame.KEYUP:
            press = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pipe1.x)
    
            
    screen.blit(background, (0,-50))
    pipe1.spawner()
    pipe2.spawner()
    pipe3.spawner()
    groundX -= speed
    if groundX < -35:
        groundX = 0
    if playing is True:
        if game == False:
            speed = 0
            birdY += 10
        else:
            speed = 4
        pipe1.x -= speed
        pipe2.x -= speed
        pipe3.x -= speed
        if press is True:
            birdY += 0
        elif press is False:
            if count1 > 5:
                birdY += 7
            else:
                birdY += 2
    elif playing is False:
        speed = 0
    if count == 3:
        count = 0
    screen.blit(bird_array[count], (20,birdY))
    time += 1
    if time == 5:
        count += 1
        time = 0
    distance1 = sqrt(pow((pipe1.x - 20), 2) + pow(pipe1.y - birdY, 2))
    distance2 = sqrt(pow((pipe2.x - 20), 2) + pow(pipe2.y - birdY, 2))
    distance3 = sqrt(pow((pipe3.x - 20), 2) + pow(pipe3.y - birdY, 2))
    distancer = sqrt(pow((pipe1.x - 20), 2) + pow((pipe1.y - 750) - birdY, 2))


   
    
    if pipe1.x < 80 and pipe1.x >= -50:
        if (birdY + 50) < pipe1.y and (birdY + 200) > (pipe1.y):
            if pipe1.x == -12:
                score += 1
                score_sound.play()
            elif pipe1.x == -10:
                score += 1
                score_sound.play()
        else:
            game = False
    if pipe2.x < 80 and pipe2.x >= -50:
        if (birdY + 50) < pipe2.y and (birdY + 200) > (pipe2.y):
            if pipe2.x == -12:
                score += 1
                score_sound.play()
            elif pipe2.x == -10:
                score += 1
                score_sound.play()
        else:
            game = False
    if pipe3.x < 80 and pipe3.x >= -50:
        if (birdY + 50) < pipe3.y and (birdY + 200) > (pipe3.y):
            if pipe3.x == -12:
                score += 1
                score_sound.play()
            elif pipe3.x == -10:
                score += 1
                score_sound.play()
        else:
            game = False

    screen.blit(ground, (groundX,610))
    if game == False:
        sound_counter += 1
        if sound_counter == 1:
            death_sound.play()
        elif sound_counter > 5:
            sound_counter = 5
        white_counter += 1
        if white_counter < 4:
            pygame.draw.rect(screen, "white", (0,0, 600,800))
    score_func()   
    pygame.display.update()
    pygame.time.Clock().tick(60)