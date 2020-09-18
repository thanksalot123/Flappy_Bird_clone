import pygame, sys, random


game_active = True

def draw_floor():
    screen.blit(bg_base,(pos_x,500))
    screen.blit(bg_base,(pos_x+376,500))

def creat_pipe():
    random_pipe_hgt = random.choice(pipe_height)
    bottom_pipe = pipe_sur.get_rect(midtop = (500,random_pipe_hgt))
    top_pipe = pipe_sur.get_rect(midbottom = (500,random_pipe_hgt-150))
    return bottom_pipe,top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes    

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_sur,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_sur,False,True)
            screen.blit(flip_pipe,pipe)   

def check_coll(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

        if bird_rect.top <= -100 or bird_rect.bottom >=700:
            return False

    return True            

pygame.init()

gravity = 0.20
brd_mov = 0

screen=pygame.display.set_mode((376,600)) #this bad boy starts the game
clock = pygame.time.Clock() #this thing here is for frame rate'
bg_surface = pygame.image.load('F:/games_by_ME/assets/sprites/background-day.png').convert()#this bad boy helps to run the file easily damn
bg_surface = pygame.transform.scale(bg_surface, (376, 600))
bg_base = pygame.image.load('F:/games_by_ME/assets/sprites/base.png').convert()
bg_base = pygame.transform.scale(bg_base, (376,100))
pos_x=0

#bird
bird_sur = pygame.image.load('F:/games_by_ME/assets/sprites/redbird-midflap.png').convert()
bird_sur = pygame.transform.scale(bird_sur,(45,32))
bird_rect = bird_sur.get_rect(center = (60,200))


pipe_sur = pygame.image.load('F:/games_by_ME/assets/sprites/pipe-green.png').convert()
pipe_sur = pygame.transform.scale(pipe_sur,(80,500))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [300,200,380]

while True:
    for event in pygame.event.get(): #event loop in pyhton it just knows all the event
        if event.type == pygame.QUIT: #to identify quit event
            pygame.quit() #quit
            sys.exit() #quit completely
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                brd_mov = 0
                brd_mov -= 8
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (60,200)
                brd_mov = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(creat_pipe())
    screen.blit(bg_surface,(0,0))
    if game_active:
        brd_mov+=gravity
        bird_rect.centery += brd_mov
        #pipes
        screen.blit(bird_sur,bird_rect)
        pos_x-=1
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_coll(pipe_list)
    draw_floor()
    if pos_x <= -376:
        pos_x=0
    pygame.display.update()
    clock.tick(120)