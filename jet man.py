import pygame
import random
from pygame.locals import *



pygame.init()


SCREEN_with=400
SCREEN_hight=700
PLAYER_POS_X=SCREEN_with/2
PLAYER_POS_y=SCREEN_hight*.8
player_velocity=0

FPS_clock=pygame.time.Clock()
FPS=60

aso1=1
aso2=1
aso3=1


power_up_oxi=1
power_up_energy=1

traviled_distance=0

background=pygame.image.load('files\img\\background.jpeg')    #.convert_alpha()


colide=pygame.image.load('files\img\\bang_end.png')
colide=pygame.transform.scale(colide,(200,160))



energey=pygame.image.load('files\img\enrgey.png')
energey=pygame.transform.scale(energey,(45,45))

oxi=pygame.image.load('files\img\o2.png')
oxi=pygame.transform.scale(oxi,(45,45))

player=pygame.image.load('files\img\player_back.png')
player=pygame.transform.scale(player,(60,110))



player_back=pygame.image.load('files\img\player_back.png')
player_back=pygame.transform.scale(player_back,(60,110))

player_l=pygame.image.load('files\img\player_L.png')
player_l=pygame.transform.scale(player_l,(30,110))


player_R=pygame.image.load('files\img\player_R.png')
player_R=pygame.transform.scale(player_R,(30,110))


actro=pygame.image.load('files\img\\astroid.png')
actro=pygame.transform.scale(actro,(100,100))




class bm():

    pygame.mixer.init()
    pygame.mixer.music.load('files\\audio\\star war background.mp3')
    pygame.mixer.music.play(loops=10)

#------------------------------------------------------------------------------------------------------------------

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(loops=0)


def text(size,coluer,tt,x_pos,y_pos):
    try:
        font_=pygame.font.SysFont(None,size)
        ren=font_.render(tt,True,coluer)
        SCREEN.blit(ren,(x_pos,y_pos))
        # pygame.display.update()
    except:
        print ('')


def cresh():
    # if (PLAYER_POS_X>x1_astro and PLAYER_POS_X<x1_astro+100 and PLAYER_POS_y>y1_astro and PLAYER_POS_y<y1_astro+100) or (PLAYER_POS_X+player.get_width()>x1_astro and PLAYER_POS_X + player.get_width()<x1_astro+100 and PLAYER_POS_y+player.get_height()>y1_astro and PLAYER_POS_y+player.get_height()<y1_astro+100):
    #     print ('game over',PLAYER_POS_X )
    #     SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2)) 
    # if (PLAYER_POS_X>x2_astro and PLAYER_POS_X<x2_astro+100 and PLAYER_POS_y>y2_astro and PLAYER_POS_y<y2_astro+100 )or (PLAYER_POS_X+player.get_width()>x2_astro and PLAYER_POS_X + player.get_width()<x2_astro+100 and PLAYER_POS_y+player.get_height()>y2_astro and PLAYER_POS_y+player.get_height()<y2_astro+100):
    #     print ('game over',PLAYER_POS_X )
    #     SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2))
    # if (PLAYER_POS_X>x3_astro and PLAYER_POS_X<x3_astro+100 and PLAYER_POS_y>y3_astro and PLAYER_POS_y<y3_astro+100) or (PLAYER_POS_X+player.get_width()>x3_astro and PLAYER_POS_X + player.get_width()<x3_astro+100 and PLAYER_POS_y+player.get_height()>y3_astro and PLAYER_POS_y+player.get_height()<y3_astro+100):
    #     print ('game over',PLAYER_POS_X )
    #     SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2))
    if (PLAYER_POS_X>x1_astro and PLAYER_POS_X<x1_astro+actro.get_width()-5 and PLAYER_POS_y>y1_astro and PLAYER_POS_y<y1_astro+actro.get_width()-5) or (PLAYER_POS_X+player.get_width()>x1_astro and PLAYER_POS_X + player.get_width()<x1_astro+actro.get_width()-5 and PLAYER_POS_y+player.get_height()>y1_astro and PLAYER_POS_y+player.get_height()<y1_astro+actro.get_width()-5):
        print ('game over',PLAYER_POS_X )
        game_over_by_cresh()

        SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2)) 
    if (PLAYER_POS_X>x2_astro and PLAYER_POS_X<x2_astro+actro.get_width()-5 and PLAYER_POS_y>y2_astro and PLAYER_POS_y<y2_astro+actro.get_width()-5 )or (PLAYER_POS_X+player.get_width()>x2_astro and PLAYER_POS_X + player.get_width()<x2_astro+actro.get_width()-5 and PLAYER_POS_y+player.get_height()>y2_astro and PLAYER_POS_y+player.get_height()<y2_astro+actro.get_width()-5):
        print ('game over',PLAYER_POS_X )
        game_over_by_cresh()
        SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2))
    if (PLAYER_POS_X>x3_astro and PLAYER_POS_X<x3_astro+actro.get_width()-5 and PLAYER_POS_y>y3_astro and PLAYER_POS_y<y3_astro+actro.get_width()-5) or (PLAYER_POS_X+player.get_width()>x3_astro and PLAYER_POS_X + player.get_width()<x3_astro+actro.get_width()-5 and PLAYER_POS_y+player.get_height()>y3_astro and PLAYER_POS_y+player.get_height()<y3_astro+actro.get_width()-5):
        print ('game over',PLAYER_POS_X )
        SCREEN.blit(colide,(PLAYER_POS_X-colide.get_width()/2,PLAYER_POS_y-colide.get_height()/2))
        game_over_by_cresh()
        

def power():
    global y_energy,y_oxi

    if (PLAYER_POS_X>x_energy and PLAYER_POS_X<x_energy+energey.get_width() and PLAYER_POS_y>y_energy and PLAYER_POS_y<y_energy+energey.get_height()) or ( PLAYER_POS_X + player.get_width()>x_energy and PLAYER_POS_X + player.get_width()<x_energy+energey.get_width() and  PLAYER_POS_y+player.get_height()>y_energy and PLAYER_POS_y+player.get_height()<y_energy+energey.get_height()  ):
        play('files\\audio\enargy.mp3')
        print('energy') 
        y_energy=SCREEN_hight 

    if( PLAYER_POS_X + player.get_width()/2>x_energy and PLAYER_POS_X + player.get_width()/2<x_energy+energey.get_width() and  PLAYER_POS_y+player.get_height()>y_energy and PLAYER_POS_y+player.get_height()<y_energy+energey.get_height() ):
        pass 
        play('files\\audio\enargy.mp3')
        print('energy')  
        y_energy=SCREEN_hight

    if (PLAYER_POS_X>x_oxi and PLAYER_POS_X<x_oxi+energey.get_width() and PLAYER_POS_y>y_oxi and PLAYER_POS_y<y_oxi+energey.get_height()) or ( PLAYER_POS_X + player.get_width()>x_oxi and PLAYER_POS_X + player.get_width()<x_oxi+energey.get_width() and  PLAYER_POS_y+player.get_height()>y_oxi and PLAYER_POS_y+player.get_height()<y_oxi+energey.get_height()) :
        play('files\\audio\oxigan.mp3')
        print('oxigin')
        y_oxi=SCREEN_hight  
    if( PLAYER_POS_X + player.get_width()/2>x_oxi and PLAYER_POS_X + player.get_width()/2<x_oxi+energey.get_width() and  PLAYER_POS_y+player.get_height()>y_oxi and PLAYER_POS_y+player.get_height()<y_oxi+energey.get_height() ):
        pass
        play('files\\audio\oxigan.mp3')
        print('oxigin')
        y_oxi=SCREEN_hight  



def game_over_by_cresh():
    over_1=1


    global run,oxi,colide,traviled_distance,aso1,aso2,aso3,power_up_energy,power_up_oxi,PLAYER_POS_X,PLAYER_POS_y
    global run,player_velocity,player,x1_astro,x2_astro,x3_astro,y1_astro,y2_astro,y3_astro,x_energy,x_oxi,y_energy,y_oxi
    global y1_speed,y1_astro,y1_astro,y1_speed

    while over_1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB :
                    pass
                    traviled_distance=0
                    y1_astro=y3_astro=y2_astro=SCREEN_hight

                    maingame()




                    
                    return True
        text(50,(200,0,0),'YOU CRESHED',SCREEN_with/6,SCREEN_hight/2)        
        pygame.display.update()


#-----------------------------------------------------------------------------------------------------------------

SCREEN= pygame.display.set_mode((SCREEN_with,SCREEN_hight))

run =True
def maingame():
    global run,oxi,colide,traviled_distance,aso1,aso2,aso3,power_up_energy,power_up_oxi,PLAYER_POS_X,PLAYER_POS_y
    global run,player_velocity,player,x1_astro,x2_astro,x3_astro,y1_astro,y2_astro,y3_astro,x_energy,x_oxi,y_energy,y_oxi
    global y1_speed,y2_speed,y3_speed


    while run==True:

        SCREEN.blit(background,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                run =False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    # player=player_R
                    player_velocity-=5

                if event.key==pygame.K_LEFT:
                    # player=player_l

                    player_velocity+=5

            if event.type==pygame.KEYUP:
                    player=player_back
                    player_velocity=0
        traviled_distance+=.05
        print(traviled_distance)



        #--------------------------------------------------------------

        if aso1==1:
            x1_astro=random.randrange(0,SCREEN_with-110)
            y1_astro=random.randrange(-150,-100)
            y1_speed=random.uniform(3.1,5.1)
            aso1=0
        if aso2==1:   
            x2_astro=random.randrange(0,SCREEN_with-110)
            y2_astro=random.randrange(-150,-100)
            y2_speed=random.uniform(3.1,5.1)
            aso2=0
        
        if aso3==1:   
            x3_astro=random.randrange(0,SCREEN_with-110)
            y3_astro=random.randrange(-150,-100)
            y3_speed=random.uniform(3.1,5.1)
            aso3=0


        y1_astro=y1_astro+y1_speed
        y2_astro=y2_astro+y2_speed
        y3_astro=y3_astro+y3_speed

        if y1_astro>SCREEN_hight+150:
            aso1=1

        if y2_astro>SCREEN_hight+150:
            aso2=1
        if y3_astro>SCREEN_hight+150:
            aso3=1


        #--------------------------------------------------------------
        if power_up_energy==1:
            x_energy=random.randrange(0,SCREEN_with-100)
            y_energy=random.randrange(-100,-10)
            power_up_energy=0




        if power_up_oxi==1:
            x_oxi=random.randrange(0,SCREEN_with-100)
            y_oxi=random.randrange(-100,-10)
            power_up_oxi=0

        if y_energy >5000:
            power_up_energy=1

        if y_oxi >4000:
            power_up_oxi=1


        y_energy+=3

        y_oxi+=3


        PLAYER_POS_X=PLAYER_POS_X-player_velocity

        if PLAYER_POS_X<-30:
            PLAYER_POS_X=-29

        if PLAYER_POS_X> (SCREEN_with-player_R.get_width()):
            PLAYER_POS_X=SCREEN_with-33

        
        


        SCREEN.blit(player,(PLAYER_POS_X,PLAYER_POS_y))

        # SCREEN.blit(player_l,(40,30))
        # SCREEN.blit(player_R,(80,30))

        

        SCREEN.blit(energey,(x_energy,y_energy))
        SCREEN.blit(oxi,(x_oxi,y_oxi))
        SCREEN.blit(actro,(x1_astro,y1_astro))
        SCREEN.blit(actro,(x2_astro,y2_astro))
        SCREEN.blit(actro,(x3_astro,y3_astro))
        cresh()
        power()


        #------------------------------
        txt=f"Distance:{int(traviled_distance)}km"
        text(30,(200,200,200),txt,SCREEN_with-160,10)

        pygame.draw.rect(SCREEN,(0,250,0),[10,10,120,15])
        pygame.draw.rect(SCREEN,(0,0,250),[10,35,120,15])





        FPS_clock.tick(FPS)

        pygame.display.update()

maingame()