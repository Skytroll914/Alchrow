import pygame
import os

pygame.font.init()

TEST=0
WIDTH, HEIGHT = 1000, 620
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alch-row")

LINE_BORDER = pygame.Rect(200, 150, 600, 5)
LINE_BORDER1 = pygame.Rect(200, 255, 600, 5)
LINE_BORDER2 = pygame.Rect(200, 360, 600, 5)
LINE_BORDER3 = pygame.Rect(200, 465, 600, 5)

PLAY1_WIN_FONT=pygame.font.SysFont('comicsans', 90)
PLAY2_WIN_FONT=pygame.font.SysFont('comicsans', 90)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
MANA_FONT = pygame.font.SysFont('comicsans', 20)

BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)

VEL=105
ARROW_VEL=2
FPS=60

PLAY1_HIT=pygame.USEREVENT+1
PLAY2_HIT=pygame.USEREVENT+2
PLAY1_BARRIER_HIT=pygame.USEREVENT+3
PLAY2_BARRIER_HIT=pygame.USEREVENT+4
ANIMATION=pygame.USEREVENT+5
PLAY1_STUN=pygame.USEREVENT+6
PLAY2_STUN=pygame.USEREVENT+7
STUN_DURATION1=pygame.USEREVENT+8
STUN_DURATION2=pygame.USEREVENT+9
STUN_ANIMATION1=pygame.USEREVENT+10
STUN_ANIMATION2=pygame.USEREVENT+11
EXPLOSION_ANIMATION=pygame.USEREVENT+12

STUN_WIDTH,STUN_HEIGHT=20,30

ARROW_X,ARROW_Y,ARROW_TYPE=None, None, None
EXPLOSION_WIDTH, EXPLOSION_HEIGHT=20,20

BACKGROUND=pygame.transform.scale(
    pygame.image.load(os.path.join('Assets2','Background.png')),(WIDTH, HEIGHT))

BARRIER_WIDTH, BARRIER_HEIGHT= 30, 400
BULLET_WIDTH, BULLET_HEIGHT = 90, 80 #BULLET >> ARROW
CHARACTER_WIDTH, CHARACTER_HEIGHT = 80, 100

CHARACTER1_IMAGE= pygame.image.load(
    os.path.join('Assets2','Character.png'))
CHARACTER2_IMAGE= pygame.image.load(
    os.path.join('Assets2','Character 2.png'))

CHARACTER1=pygame.transform.scale(
    CHARACTER1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER2=pygame.transform.scale(
    CHARACTER2_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BARRIER_IMAGE=pygame.image.load(os.path.join('Assets2','Barrier.png'))

BARRIER=pygame.transform.scale(BARRIER_IMAGE, (BARRIER_WIDTH, BARRIER_HEIGHT))

PLAY1_LEFT_IMAGE=pygame.image.load(os.path.join('Assets2','water_animation_1.png'))
PLAY1_RIGHT_IMAGE=pygame.image.load(os.path.join('Assets2','fire_animation_1.png'))
PLAY1_UP_IMAGE=pygame.image.load(os.path.join('Assets2','air_animation_1.png'))
PLAY1_DOWN_IMAGE=pygame.image.load(os.path.join('Assets2','rock_animation_1.png'))


PLAY1_LEFT=pygame.transform.scale(PLAY1_LEFT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-30))
PLAY1_RIGHT=pygame.transform.scale(PLAY1_RIGHT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-30))
PLAY1_UP=pygame.transform.scale(PLAY1_UP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
PLAY1_DOWN=pygame.transform.rotate(pygame.transform.scale(
    PLAY1_DOWN_IMAGE, (BULLET_WIDTH-20, BULLET_HEIGHT-20)),180)
PLAY2_LEFT=pygame.transform.rotate(pygame.transform.scale(
    PLAY1_LEFT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-30)),180)
PLAY2_RIGHT=pygame.transform.rotate(pygame.transform.scale(
    PLAY1_RIGHT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-30)),180)
PLAY2_UP=pygame.transform.rotate(pygame.transform.scale(
    PLAY1_UP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)),180)
PLAY2_DOWN=pygame.transform.scale(
    PLAY1_DOWN_IMAGE, (BULLET_WIDTH-20, BULLET_HEIGHT-20))

def projectile_animation(animation_queue):
    global PLAY1_LEFT
    global PLAY1_RIGHT
    global PLAY1_UP
    global PLAY1_DOWN
    global PLAY2_LEFT
    global PLAY2_RIGHT
    global PLAY2_UP
    global PLAY2_DOWN
    
    waterLst=["water_animation_1.png","water_animation_2.png","water_animation_3.png",
              "water_animation_2.png","water_animation_1.png"]
    airLst=["air_animation_1.png","air_animation_2.png","air_animation_3.png",
            "air_animation_2.png","air_animation_1.png"]
    fireLst=["fire_animation_1.png","fire_animation_2.png","fire_animation_3.png",
             "fire_animation_4.png","fire_animation_2.png"]
    earthLst=["rock_animation_1.png","rock_animation_2.png","rock_animation_3.png",
              "rock_animation_2.png","rock_animation_1.png"]

    water=waterLst[animation_queue]
    air=airLst[animation_queue]
    fire=fireLst[animation_queue]
    earth=earthLst[animation_queue]

    PLAY1_LEFT_IMAGE=pygame.image.load(os.path.join('Assets2',water))
    PLAY1_RIGHT_IMAGE=pygame.image.load(os.path.join('Assets2',fire))
    PLAY1_UP_IMAGE=pygame.image.load(os.path.join('Assets2',air))
    PLAY1_DOWN_IMAGE=pygame.image.load(os.path.join('Assets2',earth))


    PLAY1_LEFT=pygame.transform.scale(PLAY1_LEFT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
    PLAY1_RIGHT=pygame.transform.scale(PLAY1_RIGHT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-20))
    PLAY1_UP=pygame.transform.scale(PLAY1_UP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
    PLAY1_DOWN=pygame.transform.rotate(pygame.transform.scale(
        PLAY1_DOWN_IMAGE, (BULLET_WIDTH-20, BULLET_HEIGHT-20)),180)
    PLAY2_LEFT=pygame.transform.rotate(pygame.transform.scale(
        PLAY1_LEFT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)),180)
    PLAY2_RIGHT=pygame.transform.rotate(pygame.transform.scale(
        PLAY1_RIGHT_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT-20)),180)
    PLAY2_UP=pygame.transform.rotate(pygame.transform.scale(
        PLAY1_UP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)),180)
    PLAY2_DOWN=pygame.transform.scale(
        PLAY1_DOWN_IMAGE, (BULLET_WIDTH-20, BULLET_HEIGHT-20))

    

def handle_arrows(play1_arrows,play2_arrows,play1_arrows_type,play2_arrows_type, play1, play2,
                  barrier1, barrier2, play1_arrows_health, play2_arrows_health, play1_arrows_dmg_char,
                  play2_arrows_dmg_char, play1_arrows_dmg_proj, play2_arrows_dmg_proj, play1_arrows_dmg_bar,
                  play2_arrows_dmg_bar, play1_arrows_stun, play2_arrows_stun):
    removed1=0
    global DMG1
    global STUN1
    global ARROW_X,ARROW_Y,ARROW_TYPE
    
    for i in range(len(play2_arrows)):
        idx=i-removed1
        arrow2=play2_arrows[idx]
        arrow2_type=play2_arrows_type[idx]
        arrow2_dmg_char=play2_arrows_dmg_char[idx]
        arrow2_dmg_bar=play2_arrows_dmg_bar[idx]
        arrow2_stun=play2_arrows_stun[idx]
        arrow2.x-=(arrow2_type=="UP")*7+(arrow2_type=="DOWN")*3+(arrow2_type=="LEFT" or arrow2_type=="RIGHT" )*5

        if play1.colliderect(arrow2):
            pygame.event.post(pygame.event.Event(PLAY1_HIT))
            pygame.event.post(pygame.event.Event(PLAY1_STUN))
            STUN1=arrow2_stun
            DMG1=arrow2_dmg_char
            play2_arrows.pop(idx)
            play2_arrows_type.pop(idx)
            play2_arrows_dmg_char.pop(idx)
            play2_arrows_dmg_bar.pop(idx)
            play2_arrows_health.pop(idx)
            play2_arrows_dmg_proj.pop(idx)
            play2_arrows_stun.pop(idx)
            removed1+=1

        elif barrier1.colliderect(arrow2):
            pygame.event.post(pygame.event.Event(PLAY1_BARRIER_HIT))
            DMG1=arrow2_dmg_bar
            play2_arrows.pop(idx)
            play2_arrows_type.pop(idx)
            play2_arrows_dmg_char.pop(idx)
            play2_arrows_dmg_bar.pop(idx)
            play2_arrows_health.pop(idx)
            play2_arrows_dmg_proj.pop(idx)
            play2_arrows_stun.pop(idx)
            removed1+=1

    global DMG2
    global STUN2
    global ARROW_X,ARROW_Y,ARROW_TYPE
    
    removed2=0
    for i in range(len(play1_arrows)):
        idx=i-removed2
        arrow1=play1_arrows[idx]
        arrow1_type=play1_arrows_type[idx]
        arrow1_dmg_char=play1_arrows_dmg_char[idx]
        arrow1_dmg_bar=play1_arrows_dmg_bar[idx]
        arrow1_dmg_proj=play1_arrows_dmg_proj[idx]
        arrow1_stun=play1_arrows_stun[idx]
        arrow1.x+=(arrow1_type=="UP")*7+(arrow1_type=="DOWN")*3+(arrow1_type=="LEFT" or arrow1_type=="RIGHT" )*5

        removed3=0
        for i2 in range(len(play2_arrows)):
            idx2=i2-removed3
            arrow2=play2_arrows[idx2]
            arrow2_type=play2_arrows_type[idx2]
            arrow2_dmg_char=play2_arrows_dmg_char[idx2]
            arrow2_dmg_bar=play2_arrows_dmg_bar[idx2]
            arrow2_dmg_proj=play2_arrows_dmg_proj[idx2]
            
            if arrow1.colliderect(arrow2):
                
                play2_arrows_health[idx2]-=arrow1_dmg_proj
                play1_arrows_health[idx]-=arrow2_dmg_proj
                
                if play1_arrows_health[idx]<=0:
                   ARROW_X,ARROW_Y,ARROW_TYPE=arrow1.x, arrow1.y, arrow1_type
                   pygame.event.post(pygame.event.Event(EXPLOSION_ANIMATION))
                   play1_arrows.pop(idx)
                   play1_arrows_type.pop(idx)
                   play1_arrows_dmg_char.pop(idx)
                   play1_arrows_dmg_bar.pop(idx)
                   play1_arrows_health.pop(idx)
                   play1_arrows_dmg_proj.pop(idx)
                   play1_arrows_stun.pop(idx)
                   removed2+=1

                if play2_arrows_health[idx2]<=0:
                   ARROW_X,ARROW_Y,ARROW_TYPE=arrow2.x, arrow2.y, arrow2_type
                   pygame.event.post(pygame.event.Event(EXPLOSION_ANIMATION))
                   play2_arrows.pop(idx2)
                   play2_arrows_type.pop(idx2)
                   play2_arrows_dmg_char.pop(idx2)
                   play2_arrows_dmg_bar.pop(idx2)
                   play2_arrows_health.pop(idx2)
                   play2_arrows_dmg_proj.pop(idx2)
                   play2_arrows_stun.pop(idx2)
                   removed3+=1

        if play2.colliderect(arrow1):
            pygame.event.post(pygame.event.Event(PLAY2_HIT))
            pygame.event.post(pygame.event.Event(PLAY2_STUN))
            ARROW_X,ARROW_Y,ARROW_TYPE=arrow1.x, arrow1.y, arrow1_type
            pygame.event.post(pygame.event.Event(EXPLOSION_ANIMATION))
            STUN2=arrow1_stun
            DMG2=arrow1_dmg_char
            play1_arrows.pop(idx)
            play1_arrows_type.pop(idx)
            play1_arrows_dmg_char.pop(idx)
            play1_arrows_dmg_bar.pop(idx)
            play1_arrows_health.pop(idx)
            play1_arrows_dmg_proj.pop(idx)
            play1_arrows_stun.pop(idx)
            removed2+=1

        elif barrier2.colliderect(arrow1):
            pygame.event.post(pygame.event.Event(PLAY2_BARRIER_HIT))
            ARROW_X,ARROW_Y,ARROW_TYPE=arrow1.x, arrow1.y, arrow1_type
            pygame.event.post(pygame.event.Event(EXPLOSION_ANIMATION))
            DMG2=arrow1_dmg_bar
            play1_arrows.pop(idx)
            play1_arrows_type.pop(idx)
            play1_arrows_dmg_char.pop(idx)
            play1_arrows_dmg_bar.pop(idx)
            play1_arrows_health.pop(idx)
            play1_arrows_dmg_proj.pop(idx)
            play1_arrows_stun.pop(idx)
            removed2+=1

    
def fire_explosion():
    pass
    

def rock_explosion():
    pass

def water_explosion():
    pass

def air_explosion():
    pass
    


def draw_window(play1,play2, play1_mana, play2_mana, play1_health, play2_health,
                barrier1, barrier2, play1_arrows, play2_arrows, play1_arrows_type,
                play2_arrows_type, play1_stun, play2_stun, stun1, stun2):
    
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN,BLACK,LINE_BORDER)
    pygame.draw.rect(WIN,BLACK,LINE_BORDER1)
    pygame.draw.rect(WIN,BLACK,LINE_BORDER2)
    pygame.draw.rect(WIN,BLACK,LINE_BORDER3)
    

    WIN.blit(CHARACTER1, (play1.x-CHARACTER_WIDTH, play1.y))
    WIN.blit(CHARACTER2, (play2.x, play2.y))
    WIN.blit((BARRIER), (barrier1.x-BARRIER_WIDTH-BARRIER_WIDTH, barrier1.y))
    WIN.blit((BARRIER), (barrier2.x, barrier2.y))
    

    play1_health_text=HEALTH_FONT.render("HEALTH: " + str(play1_health), 1, RED)
    play2_health_text=HEALTH_FONT.render("HEALTH: " + str(play2_health), 1, RED)
    play1_mana_text = MANA_FONT.render("MANA: " + str(play1_mana), 1, BLUE)
    play2_mana_text = MANA_FONT.render("MANA: " + str(play2_mana), 1, BLUE)
    WIN.blit(play1_health_text, (10,10))
    WIN.blit(play2_health_text, (WIDTH-play1_health_text.get_width()-10,10))
    WIN.blit(play1_mana_text, (10,play1_health_text.get_height()+5))
    WIN.blit(play2_mana_text, (WIDTH-play2_mana_text.get_width()-10,play1_health_text.get_height()+5))

    for arrow in play1_arrows:
        arrow_index=play1_arrows.index(arrow)
        arrow_type = play1_arrows_type[arrow_index]

        if arrow_type == "LEFT":
            WIN.blit(PLAY1_LEFT, (arrow.x,arrow.y))
        elif arrow_type == "RIGHT":
            WIN.blit(PLAY1_RIGHT, (arrow.x,arrow.y+10))
        elif arrow_type == "UP":
            WIN.blit(PLAY1_UP, (arrow.x,arrow.y))
        elif arrow_type == "DOWN":
            WIN.blit(PLAY1_DOWN, (arrow.x,arrow.y+10))

    for arrow in play2_arrows:
        arrow_index=play2_arrows.index(arrow)
        arrow_type = play2_arrows_type[arrow_index]

        if arrow_type == "LEFT":
            WIN.blit(PLAY2_LEFT, (arrow.x-BULLET_WIDTH,arrow.y))
        elif arrow_type == "RIGHT":
            WIN.blit(PLAY2_RIGHT, (arrow.x-BULLET_WIDTH,arrow.y+10))
        elif arrow_type == "UP":
            WIN.blit(PLAY2_UP, (arrow.x-BULLET_WIDTH,arrow.y))
        elif arrow_type == "DOWN":
            WIN.blit(PLAY2_DOWN, (arrow.x-BULLET_WIDTH,arrow.y+10))

    
    if play1_stun>0:
        WIN.blit(stun1,(play1.x-CHARACTER_WIDTH+(CHARACTER_WIDTH-STUN_WIDTH)//2, play1.y-STUN_HEIGHT))
   
    if play2_stun>0:
        WIN.blit(stun2,(play2.x+(CHARACTER_WIDTH-STUN_WIDTH)//2, play2.y-STUN_HEIGHT))
            
    pygame.display.update()


def draw_winner(text):
    play1_win_text=PLAY1_WIN_FONT.render(text,1,RED)
    WIN.blit(play1_win_text, (WIDTH//2-play1_win_text.get_width()/2,HEIGHT//2-play1_win_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

    
def main():
    play1 = pygame.Rect(150+CHARACTER_WIDTH, 155, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    play2 = pygame.Rect(770, 155, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    barrier1 = pygame.Rect(100+BARRIER_WIDTH+BARRIER_WIDTH, 130, BARRIER_WIDTH, BARRIER_HEIGHT)
    barrier2 = pygame.Rect(880, 130, BARRIER_WIDTH, BARRIER_HEIGHT)

    stunLst=["stun_1.png","stun_2.png","stun_3.png","stun_4.png",
            "stun_5.png","stun_6.png","stun_7.png"]
    stun_image=pygame.image.load(os.path.join("Assets2",stunLst[0]))
    stun1=pygame.transform.scale(stun_image, (STUN_WIDTH,STUN_HEIGHT))
    stun2=pygame.transform.scale(stun_image, (STUN_WIDTH,STUN_HEIGHT))

                
    animation_queue=0
    frames1=0
    frames2=0
    play1_stun=0
    play2_stun=0
    play1_mana=0
    play2_mana=0
    play1_health=100
    play2_health=100
    play1_arrows=[]
    play1_arrows_type=[]
    play2_arrows=[]
    play2_arrows_type=[]
    play1_arrows_health=[]
    play2_arrows_health=[]
    play1_arrows_dmg_char=[]
    play2_arrows_dmg_char=[]
    play1_arrows_dmg_proj=[]
    play2_arrows_dmg_proj=[]
    play1_arrows_dmg_bar=[]
    play2_arrows_dmg_bar=[]
    play1_arrows_stun=[]
    play2_arrows_stun=[]

    fire_explosion=[]
    fire_explosion_phase=[]
    water_explosion=[]
    water_explosion_phase=[]
    air_explosion=[]
    air_explosion_phase=[]
    earth_explosion=[]
    earth_explosion_phase=[]
    
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.time.set_timer(ANIMATION, 100)
    
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            keys=pygame.key.get_pressed()
            if event.type == pygame.USEREVENT:
                if play1_mana<10:
                    play1_mana+=1
                if play2_mana<10:
                    play2_mana+=1

            if event.type == ANIMATION:
                projectile_animation(animation_queue)
                animation_queue+=1
                if animation_queue == 5:
                    animation_queue=0
                
            
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j and play1.y-VEL>150 and play1_stun==0:
                    play1.y -= VEL
            
                if event.key == pygame.K_k and play1.y+VEL<370 and play1_stun==0:
                    play1.y += VEL

                if event.key == pygame.K_n and play2.y-VEL>150 and play2_stun==0:
                    play2.y -= VEL
            
                if event.key == pygame.K_m and play2.y+VEL<370 and play2_stun==0:
                    play2.y += VEL

                #player 1 shooting keys
                if keys[pygame.K_w] and keys[pygame.K_h] and play1_mana>0 and play1_stun==0:
                    arrow=pygame.Rect(play1.x,play1.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="UP"
                    play1_arrows.append(arrow)
                    play1_arrows_type.append(arrow_type)
                    play1_arrows_health.append(5)
                    play1_arrows_dmg_char.append(5)
                    play1_arrows_dmg_bar.append(5)
                    play1_arrows_dmg_proj.append(5)
                    play1_arrows_stun.append(200)
                    play1_mana-=1
                    
                if keys[pygame.K_s] and keys[pygame.K_h] and play1_mana>2 and play1_stun==0:
                    arrow=pygame.Rect(play1.x,play1.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="DOWN"
                    play1_arrows.append(arrow)
                    play1_arrows_type.append(arrow_type)
                    play1_arrows_health.append(15)
                    play1_arrows_dmg_char.append(10)
                    play1_arrows_dmg_bar.append(15)
                    play1_arrows_dmg_proj.append(15)
                    play1_arrows_stun.append(1000)
                    play1_mana-=3
                    
                if keys[pygame.K_a] and keys[pygame.K_h] and play1_mana>1 and play1_stun==0:
                    arrow=pygame.Rect(play1.x,play1.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="LEFT"
                    play1_arrows.append(arrow)
                    play1_arrows_type.append(arrow_type)
                    play1_arrows_health.append(5)
                    play1_arrows_dmg_char.append(5)
                    play1_arrows_dmg_bar.append(10)
                    play1_arrows_dmg_proj.append(10)
                    play1_arrows_stun.append(500)
                    play1_mana-=2
                    
                if keys[pygame.K_d] and keys[pygame.K_h] and play1_mana>1 and play1_stun==0:
                    arrow=pygame.Rect(play1.x,play1.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="RIGHT"
                    play1_arrows.append(arrow)
                    play1_arrows_type.append(arrow_type)
                    play1_arrows_health.append(5)
                    play1_arrows_dmg_char.append(10)
                    play1_arrows_dmg_bar.append(10)
                    play1_arrows_dmg_proj.append(10)
                    play1_arrows_stun.append(200)
                    play1_mana-=2

                #player 2 shooting keys
                if keys[pygame.K_UP] and keys[pygame.K_b] and play2_mana>0 and play2_stun==0:
                    arrow=pygame.Rect(play2.x,play2.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="UP"
                    play2_arrows.append(arrow)
                    play2_arrows_type.append(arrow_type)
                    play2_arrows_health.append(5)
                    play2_arrows_dmg_char.append(5)
                    play2_arrows_dmg_bar.append(5)
                    play2_arrows_dmg_proj.append(5)
                    play2_arrows_stun.append(500)
                    play2_mana-=1
                    
                if keys[pygame.K_DOWN] and keys[pygame.K_b] and play2_mana>2 and play2_stun==0:
                    arrow=pygame.Rect(play2.x,play2.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="DOWN"
                    play2_arrows.append(arrow)
                    play2_arrows_type.append(arrow_type)
                    play2_arrows_health.append(15)
                    play2_arrows_dmg_char.append(10)
                    play2_arrows_dmg_bar.append(15)
                    play2_arrows_dmg_proj.append(15)
                    play2_arrows_stun.append(1500)
                    play2_mana-=3
                    
                if keys[pygame.K_LEFT] and keys[pygame.K_b] and play2_mana>1 and play2_stun==0:
                    arrow=pygame.Rect(play2.x,play2.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="LEFT"
                    play2_arrows.append(arrow)
                    play2_arrows_type.append(arrow_type)
                    play2_arrows_health.append(5)
                    play2_arrows_dmg_char.append(5)
                    play2_arrows_dmg_bar.append(10)
                    play2_arrows_dmg_proj.append(10)
                    play2_arrows_stun.append(1000)
                    play2_mana-=2
                    
                if keys[pygame.K_RIGHT] and keys[pygame.K_b] and play2_mana>1 and play2_stun==0:
                    arrow=pygame.Rect(play2.x,play2.y+10,
                                      BULLET_WIDTH, BULLET_HEIGHT)
                    arrow_type="RIGHT"
                    play2_arrows.append(arrow)
                    play2_arrows_type.append(arrow_type)
                    play2_arrows_health.append(5)
                    play2_arrows_dmg_char.append(10)
                    play2_arrows_dmg_bar.append(10)
                    play2_arrows_dmg_proj.append(10)
                    play2_arrows_stun.append(500)
                    play2_mana-=2

            if event.type == PLAY1_HIT:
                play1_health-=DMG1
                
            if event.type == PLAY2_HIT:
                play2_health-=DMG2
                
            if event.type == PLAY1_BARRIER_HIT:
                play1_health-=DMG1
                
            if event.type == PLAY2_BARRIER_HIT:
                play2_health-=DMG2

            if event.type == PLAY1_STUN:
                frames1 = 0
                duration1 = STUN1
                play1_stun+=1
                pygame.time.set_timer(STUN_DURATION1, duration1)
                pygame.time.set_timer(STUN_ANIMATION1, duration1//7)

                stunLst=["stun_1.png","stun_2.png","stun_3.png","stun_4.png",
                        "stun_5.png","stun_6.png","stun_7.png"]
                stun_image=pygame.image.load(os.path.join("Assets2",stunLst[0]))
                stun1=pygame.transform.scale(stun_image, (STUN_WIDTH,STUN_HEIGHT))
                
            if event.type == STUN_DURATION1:
                frames1 = 0
                play1_stun=0
                pygame.time.set_timer(STUN_DURATION1, 0)
                pygame.time.set_timer(STUN_ANIMATION1, 0)
                
                
                
                
            if event.type == STUN_ANIMATION1:
                stunLst=["stun_1.png","stun_2.png","stun_3.png","stun_4.png",
                         "stun_5.png","stun_6.png","stun_7.png"]
                stun_image1=pygame.image.load(os.path.join("Assets2",stunLst[frames1]))
                stun1=pygame.transform.scale(stun_image1, (STUN_WIDTH,STUN_HEIGHT))
                frames1+=1
                    
                    

            if event.type == PLAY2_STUN:
                frames2 = 0
                duration2 = STUN2
                play2_stun+=1
                pygame.time.set_timer(STUN_DURATION2, duration2)
                pygame.time.set_timer(STUN_ANIMATION2, duration2//7)

                stunLst=["stun_1.png","stun_2.png","stun_3.png","stun_4.png",
                        "stun_5.png","stun_6.png","stun_7.png"]
                stun_image=pygame.image.load(os.path.join("Assets2",stunLst[0]))
                stun2=pygame.transform.scale(stun_image, (STUN_WIDTH,STUN_HEIGHT))


    

                    
            if event.type == STUN_DURATION2:
                frames2 = 0
                play2_stun=0
                pygame.time.set_timer(STUN_DURATION2, 0)
                pygame.time.set_timer(STUN_ANIMATION2, 0)
                
                
            if event.type == STUN_ANIMATION2:
                stunLst=["stun_1.png","stun_2.png","stun_3.png","stun_4.png",
                         "stun_5.png","stun_6.png","stun_7.png","stun_7.png"]
                stun_image2=pygame.image.load(os.path.join("Assets2",stunLst[frames2]))
                stun2=pygame.transform.scale(stun_image2, (STUN_WIDTH,STUN_HEIGHT))
                frames2+=1

        print(frames2)
                
            
        handle_arrows(play1_arrows,play2_arrows,play1_arrows_type,play2_arrows_type, play1, play2,
                      barrier1, barrier2, play1_arrows_health, play2_arrows_health, play1_arrows_dmg_char,
                      play2_arrows_dmg_char, play1_arrows_dmg_proj, play2_arrows_dmg_proj, play1_arrows_dmg_bar,
                      play2_arrows_dmg_bar, play1_arrows_stun, play2_arrows_stun)
        
        draw_window(play1, play2, play1_mana, play2_mana, play1_health, play2_health,
                    barrier1, barrier2, play1_arrows, play2_arrows, play1_arrows_type,
                    play2_arrows_type, play1_stun, play2_stun, stun1, stun2)

        winner_text=""
        if play1_health<=0:
            winner_text="Player 2 WINS!!!"
            
        if play2_health<=0:
            winner_text="Player 1 WINS!!!"

        if winner_text!="":
            pygame.time.set_timer(pygame.USEREVENT, 0)
            pygame.time.set_timer(ANIMATION, 0)
            pygame.time.set_timer(STUN_DURATION1, 0)
            pygame.time.set_timer(STUN_ANIMATION1, 0)
            pygame.time.set_timer(STUN_DURATION2, 0)
            pygame.time.set_timer(STUN_ANIMATION2, 0)
            draw_winner(winner_text)
            break
    main()
            
if __name__ == "__main__":
    main()
