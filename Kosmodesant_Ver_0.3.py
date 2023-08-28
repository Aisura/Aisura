import pygame
import time
from random import randint
import random
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)

dis_width = 800
dis_height  = 600

font_style=pygame.font.SysFont(None,50)
dis=pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption('Космодесатник')

Clock=pygame.time.Clock()

marine_block=10

def message(msg,color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_height*0.33333,dis_width/3])

def messg(msg,color):
    
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_height/2,dis_width/3])
    
def mess(msg,color):
    
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[0.2*dis_height,0.4*dis_width])
def mess2(msg,color):
    
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[0.5*dis_height,0.3333333*dis_width])
def mess3(msg,color):
    
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[0.36*dis_height,0.35*dis_width])    
def mess4(msg,color):
    
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[0.25*dis_height,0.333333*dis_width]) 
sound=0

mess4('Ультрамарины за Императора',blue)

def game_Loop():
    
    pygame.mixer.init()
    pygame.mixer_music.load("Warhammer_40K.mp3")
    pygame.mixer_music.play()
    
    ran1=randint(50,500)
    ran2=randint(50,700)
    
    game_over=False
    game_close=False
    game_dead=False
    game_victori=False
    
    x1=round(random.randrange(0, dis_width - marine_block) / 10.0) * 10.0
    y1=round(random.randrange(0, dis_height - marine_block) / 10.0) * 10.0
    
    x1_change = 0
    y1_change = 0
    
    KsenosiX=round(random.randrange(0, dis_width - marine_block) / 10.0) * 10.0
    KsenosiY=round(random.randrange(0, dis_height - marine_block) / 10.0) * 10.0
    
    KsenosiHP=100
    
    marine_speed=20
    hp=200
    
    if not x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 and KsenosiX >= dis_width or KsenosiX < 0 or KsenosiY >= dis_height or KsenosiY < 0:
        
        KsenosiY=round(random.randrange(0, dis_width - marine_block) / 10.0) * 10.0
        KsenosiX=round(random.randrange(0, dis_height - marine_block) / 10.0) * 10.0
        
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            
            x1=round(random.randrange(0, dis_width - marine_block) / 10.0) * 10.0
            y1=round(random.randrange(0, dis_height - marine_block) / 10.0) * 10.0
            
    
        if KsenosiX >= dis_width or KsenosiX < 0 or KsenosiY >= dis_height or KsenosiY < 0:
            
            KsenosiY=round(random.randrange(0, dis_width - marine_block) / 10.0) * 10.0
            KsenosiX=round(random.randrange(0, dis_height - marine_block) / 10.0) * 10.0
            
    
    pygame.display.update()
    time.sleep(2)
    
    
    while not game_over:
        
    
        
        while game_close == True:
            
            dis.fill(white)
            mess3(f'Вы сбежали с поле боя.', red)
            
            mess('На С вернуться Q быть расстреляным.',red)
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    game_over = True
                    game_close = False
                    
                    dis.fill(white)
                    
                    message('Вы были расстреляны',red)
                    time.sleep(2)
                    pygame.display.update()
                    


                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        
                        dis.fill(white)
                        
                        message('Вы были расстреляны',red)
                        
                        time.sleep(2)
                        pygame.display.update()
                    
                        game_over = True
                        game_close = False
                    
                    elif event.key == pygame.K_c:
                        game_Loop()
        
        
        while game_victori==True:
                
            dis.fill(white)
                
            mess2('Победа',red)
            mess('На C начать заново, на Q закончить',red)
            
            pygame.display.update()
            
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    game_over = True
                    game_victori = False
                    
                    dis.fill(white)
                    
                    mess2('Вы молодцы',red)
                    pygame.display.update()
                    time.sleep(2)
            
            
                if event.key == pygame.K_q:
                        
                    dis.fill(white)
                        
                    mess2('Вы молодцы',red)
                        
                    pygame.display.update()
                    time.sleep(2)
                    
                    game_over = True
                    game_victori = False
                    
                elif event.key == pygame.K_c:
                    dis.fill(white)
                    mess2('Вперед к Победам',red)
                    mess('За Императора!!!',red)
                    pygame.display.update()
                    time.sleep(2)
                    game_Loop()
        
        
        
        while game_dead==True:
            
            dis.fill(white)
            
            print('Люблю тебя! Будь осторожен в следующий раз солнышко.')
            
            mess2('Вы умерли.',red)
            
            mess('На C начать заново, на Q закончить',red)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    game_over = True
                    game_dead = False
                    
                    dis.fill(white)
                    
                    mess2('Вы умерли',red)
                    
                    pygame.display.update()
                    time.sleep(2)
                
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        
                        game_over = True
                        game_dead = False
                        
                        dis.fill(white)
                        
                        mess2('Вы умерли',red)
                        
                        pygame.display.update()
                        time.sleep(2)
                        
                        
                    elif event.key == pygame.K_c:
                        
                        dis.fill(white)
                        
                        mess2('Смерть не повод сдаться',red)
                        time.sleep(2)
                        pygame.display.update()
                        game_Loop()
                    
        for event in pygame.event.get():
            
            
            if event.type == pygame.QUIT:
                game_over = True
                dis.fill(white)
                message('Вы предали Императора',red)
                pygame.display.update()
                time.sleep(2)
            
            if event.type == pygame.KEYDOWN:
                
                
                if event.key == pygame.K_LEFT:
                    x1_change = -marine_block
                    y1_change = 0
    
                elif event.key == pygame.K_RIGHT:
                    x1_change = marine_block
                    y1_change = 0
                
                elif event.key == pygame.K_UP:
                    y1_change = -marine_block
                    x1_change = 0
                
                elif event.key == pygame.K_DOWN:
                    y1_change = marine_block
                    x1_change = 0
                
                elif event.key==pygame.K_LCTRL:
                    x1_change=0
                    y1_change=0
                
                if marine_speed == marine_speed:
                    if marine_speed == 100:
                        marine_speed = 90
                    
                    if marine_speed > 100:
                        marine_speed = 90
                    
                    if marine_speed == 0:
                        marine_speed = 10
                    
                    elif event.key == pygame.K_z:
                        marine_speed -= 10
                    if marine_speed == 0:
                        marine_speed =10
                    
                    elif event.key == pygame.K_x:
                        marine_speed += 10
                    
                    
                    
                    if y1==KsenosiY and x1 < KsenosiX:
                        if event.key==pygame.K_d:
                        
                            KsenosiHP-=20
                            print('Урон hp -40')
                            a=randint(1,3)
                            if a==1:
                                print('Бдыщ!!')
                            if a==2:
                                print('Баах!')
                            if a==3:
                                print('Папах!!!')
                        
                        
                    if y1==KsenosiY and x1 > KsenosiX:
                        if event.key==pygame.K_a:
                            
                            KsenosiHP-=20
                            print('Урон hp -40')
                            a=randint(1,3)
                            if a==1:
                                print('Бдыщ!!')
                            if a==2:
                                print('Баах!')
                            if a==3:
                                print('Папах!!!')
                        
                    
                    if x1 == KsenosiX and y1>KsenosiY:
                        if event.key==pygame.K_w:
                            KsenosiHP-=20
                            print('Урон hp -40')
                            a=randint(1,3)
                            if a==1:
                                print('Бдыщ!!')
                            if a==2:
                                print('Баах!')
                            if a==3:
                                print('Папах!!!')
                    
                    
                    if x1 == KsenosiX and y1 < KsenosiY:
                        if event.key==pygame.K_s:
                            KsenosiHP-=20
                            a=randint(1,3)
                            if a==1:
                                print('Бдыщ!!')
                            if a==2:
                                print('Баах!')
                            if a==3:
                                print('Папах!!!')
    


        
        if KsenosiHP==0:
            game_victori=True
        
        if hp==0:
            game_dead=True
        
        if x1 == KsenosiX and y1 == KsenosiY:
            hp-=20
            print('HP -20')
        
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close=True
        
        x1+=x1_change
        y1+=y1_change
        
        dis.fill(white)
        
        pygame.draw.rect(dis,red,[KsenosiX,KsenosiY, marine_block,marine_block])
        pygame.draw.rect(dis,blue,[x1,y1,marine_block,marine_block])
        pygame.display.update() 
        Clock.tick(marine_speed)
    
    
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()


game_Loop()