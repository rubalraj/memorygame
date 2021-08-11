import pygame,sys,random
from pygame.locals import *
from random import randint
pygame.init()
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
fl=0
c=pygame.font.match_font('freemono')
d=pygame.font.match_font('ubuntumono')
bigFont=pygame.font.Font('main.ttf',80)
smallFont=pygame.font.Font('main.ttf',40)
kingFont=pygame.font.Font('KGTribecaStamp.ttf',80)
kingFont1=pygame.font.Font('Kingthings Calligraphica 2.ttf',40)
kingFont2=pygame.font.Font('Kingthings Knobson.ttf',80)
kingFont3=pygame.font.Font('Kingthings Sans.ttf',50)
kingFont4=pygame.font.Font('Kingthings Xander.ttf',80)
varFont=pygame.font.Font('VarianteInitials.otf',80)
wauFont=pygame.font.Font('WaukeganHustle-Regular.ttf',120)
timer_font=pygame.font.Font('font.ttf',100)
fontobj=pygame.font.Font(d,80)
message_font=pygame.font.Font(d,40)
score_font=pygame.font.Font(c,80)
BLUE=(0,0,255)
max_time=18
elapsed=0
message=""
Click = pygame.mixer.Sound("snd.ogg")
correct=pygame.mixer.Sound("yes!.wav")
correct1=pygame.mixer.Sound("yes!.wav")
level_change= [0 for x in range(10)]# generates 9 0's [0,0,0,0,0,0,0,0,0]
def level_timer():
        global max_time,level_change
        for i in list(range(0,10)):# generates integers from 0 to 9 [0,1,2,3,4,5,6,7,8,9]
                level_change[i]=max_time# as level  increase by 1 , maximum time(given time ) decrease by 1
                max_time-=1

level_time=0
Matrix = [[0 for x in range(4)] for x in range(4)]# creating 2 dimensional array having 4 row and 4 coloumn
point=0
Hash = [0 for x in list(range(201))]# will generate 200 0's

def add_num():# to insert random numbers b/w 0 to 200 behind the black screen
        global Hash,Matrix
        for i in list(range(0,4)):# generate [0,1,2,3]
                for p in list(range(0,4)):    # generate [0,1,2,3]
                        add_num=randint(0,200) #this is method the packge to choose a random integer b/w two values(0,200)
                        while Hash[add_num]==1:
                                add_num=randint(0,200)
                        Hash[add_num]=1
                        Matrix[p][i]=add_num
                #print Matrix[p][i]
randomNum = [0 for x in list(range(10))]# generate 9 0's [0,0,0,0,0,0,0,0,0]

def num_challenge():
        global randomNum,Matrix
        for z in list(range(0,10)):
                find_numX=randint(0,3)# row
                find_numY=randint(0,3)# coloumn
                randomNum[z]=Matrix[find_numX][find_numY]

#print randomNum
level=0
window2=pygame.display.set_mode((1000,600))
window=pygame.display.set_mode((600,600))

class Mainwindow:
        def draw(self):
                global fontobj,BLUE,textop1,textop2,textop3
                main=pygame.display.set_mode((1000,600))# intililize a window or screen to display
                main.fill(WHITE)
                pygame.display.set_caption("Find it Fast")
                search=pygame.image.load('bg1.jpg')
                search = pygame.transform.scale(search, (1000, 600))# resize an image use transform
                heading=kingFont.render("Find it Fast",False,(255,0,255))
                texthead=heading.get_rect()
                texthead.center=(500,100)
                op1=smallFont.render("Play",False,(255,255,0))
                textop1=op1.get_rect()
                textop1.center=(50,550)
                op2=smallFont.render("Help",False,(255,255,0))
                textop2=op2.get_rect()
                textop2.center=(950,550)
                op3=smallFont.render("Credits",False,(255,255,0))
                textop3=op3.get_rect()
                textop3.center=(550,550)
                #op4=smallFont.render("High_Score",False,(255,255,0))
                #textop4=op4.get_rect()
                #textop4.center=(650,550)
                main.blit(search,(0,0))
                main.blit(heading,texthead)
                main.blit(op1,textop1)
                main.blit(op2,textop2)
                main.blit(op3,textop3)
                #main.blit(op4,texttop4)
class Game:
       
        n='Score:'
       
        score=kingFont3.render(n,False,BLUE)

        textscore=score.get_rect()
        textscore.center=(750,50)
       
       
        pos=(0,0)
        string=""
        centerX=0
        centerY=0
       
        kelax=0
        kelay=pos[1]
       
        #def screen(self):
                       
        def draw(self):
                global WHITE,BLUE,BLACK,number,window,Matrix,level,point,timer,message,RED,menu,level_time
                window=pygame.display.set_mode((1000,600))
                window.fill(WHITE)
                pygame.display.set_caption("Find it Fast")
                back=pygame.image.load('yellow.jpg')
                back= pygame.transform.scale(back, (400, 600))
               
                pygame.draw.rect(window, (0,0,0), (0,0,600,600), 0)
                if self.pos[0]<=600 and self.pos[0]>0 and self.pos[1]<=600 and self.pos[1]>0:
                        #pygame.mouse.set_visible(False)        
                        pygame.draw.circle(window, (200,200,200,0.3), (self.pos[0],self.pos[1]), 60, 0)
                i=0
                factor=150
                #Matrix = [[0 for x in range(7)] for x in range(7)]
                for i in list(range(0,4)):
                        for p in list(range(0,4)):
                                pygame.draw.rect(window, (0,0,0), (p*factor,i*factor,factor,factor), 1)
                                #font=pygame.font.Font('main.ttf',80)
                                temp=Matrix[p][i]
                                #print temp
                                string=str(temp)
                                number=fontobj.render(string,False,BLACK)
                                num=number.get_rect()
                                centerX=p*factor+factor/2
                                centerY=i*factor+factor/2
                                num.center=(centerX,centerY)
                               
                                window.blit(number,num)
                #if level==10:
                #       find=bigFont.render("",False,BLUE)
                #else:
                find=kingFont4.render(str(randomNum[level]),False,(102,0,151))
                findNum=find.get_rect()
                findNum.center=(890,150)
                score_add=kingFont3.render(str(point),False,(0,102,0))
                timer_f=timer_font.render(str(timer),False,RED)
             
                mess=message_font.render(str(message),False,(153,0,0))
                message_p=mess.get_rect()
                message_p.center=(800,480)
                find_n=kingFont3.render("Find:  ",False,BLUE)
                find_number=find_n.get_rect()
                find_number.center=(750,150)
                main_menu=kingFont1.render("Main Menu",False,(20,143,180))
                menu=main_menu.get_rect()
                menu.center=(900,570)
                level_menu=kingFont3.render("Level: ",False,BLUE)
                lev_disp=level_menu.get_rect()
                lev_disp.center=(750,380)
                level_no=kingFont3.render(str(level_time+1),False,(0,102,0))
                lev_disp1=level_no.get_rect()
                lev_disp1.center=(830,380)
                timer_text=timer_f.get_rect()
                timer_text.center=(790,250)
                window.blit(back,(600,0))
                window.blit(timer_f,timer_text)
                window.blit(mess,message_p)
                score_now=score_add.get_rect()
                score_now.center=(850,50)
                window.blit(self.score,self.textscore)
                window.blit(score_add,score_now)
                window.blit(main_menu,menu)
                window.blit(find_n,find_number)
                window.blit(find,findNum)
                window.blit(level_no,lev_disp1)
                window.blit(level_menu,lev_disp)
        def update(self):
                self.pos=pygame.mouse.get_pos()
class Help:
        def draw(self):
                global GREEN,BLUE,textdisp
                help=pygame.display.set_mode((1000,600))
                pygame.display.set_caption("Help")
                text='Main Menu'
                text1='Try to find the given number in the grid within the limited time.'
                text2='Beware! A wrong choice will make you lose the game.'
                text3='Find Fast, Score High!'
                help.fill(WHITE)
                heading1=kingFont.render("Help",False,BLUE)
                texthead1=heading1.get_rect()
                texthead1.center=(500,75)
                search1=pygame.image.load('question.jpg')
                search1= pygame.transform.scale(search1, (1000, 600))
                bigFont=pygame.font.Font('Kingthings Calligraphica 2.ttf',35)
                text=smallFont.render(text,False,(0,0,255))
                textdisp=text.get_rect()
                textdisp.center=(500,550)
                text4=bigFont.render(text1,False,(0,0,0))
                textdisp3=text4.get_rect()
                textdisp3.center=(500,250)
                text5=bigFont.render(text2,False,(0,0,0))
                textdisp1=text5.get_rect()
                textdisp1.center=(500,300)
                text6=bigFont.render(text3,False,(0,0,0))
                textdisp2=text6.get_rect()
                textdisp2.center=(500,350)
                help.blit(search1,(0,0))
                help.blit(heading1,texthead1)
                help.blit(text4,textdisp3)
                help.blit(text5,textdisp1)
                help.blit(text6,textdisp2)
                help.blit(text,textdisp)
               
#class HighScore:
#         def draw(self):
#               global GREEN,BLUE,textdisp
#              highscore=pygame.display.set_mode((1000,600))
#               pygame.display.set_caption("High Scores")
#              text= 'Main Menu'
#             highscore.fill(WHITE)
#            heading1=kingFont.render("High Scores",False,(255,255,0))
#           texthead1=heading1.get_rect()
#           texthead1.center=(500,300)
#           highscore.blit(heading1,texthead1)
#           highscore.blit(text,textdisp)
               
class Credits:
        def draw(self):
                global GREEN,BLUE,ctextdisp
                credits=pygame.display.set_mode((1000,600))
                pygame.display.set_caption("Credits")
                text='Main Menu'
                text1='Silky Rani'
                text2='Shivani Kumari'
                text3='Rubal Raj'
                text4='Ankita Keshri'
                text5='Shushma Suman'
                credits.fill(WHITE)
                heading1=kingFont.render("Credits",False,(255,255,0))
                texthead1=heading1.get_rect()
                texthead1.center=(500,300)
                search1=pygame.image.load('global_illumination_with_c4d_by_laganification-d4f9o2x.jpg')
                search1= pygame.transform.scale(search1, (1000, 600))
                bigFont=pygame.font.Font('Kingthings Calligraphica 2.ttf',25)
                text=smallFont.render(text,False,(255,255,0))
                ctextdisp=text.get_rect()
                ctextdisp.center=(500,550)
                text6=bigFont.render(text1,False,(255,255,255))
                textdisp3=text6.get_rect()
                textdisp3.center=(100,400)
                text7=bigFont.render(text2,False,(255,255,255))
                textdisp1=text7.get_rect()
                textdisp1.center=(300,400)
                text8=bigFont.render(text3,False,(255,255,255))
                textdisp2=text8.get_rect()
                textdisp2.center=(500,400)
                text9=bigFont.render(text4,False,(255,255,255))
                textdisp4=text9.get_rect()
                textdisp4.center=(700,400)
                text10=bigFont.render(text5,False,(255,255,255))
                textdisp5=text10.get_rect()
                textdisp5.center=(900,400)
                text11=bigFont.render('BCA/40076/17',False,(255,255,255))
                textdisp6=text11.get_rect()
                textdisp6.center=(100,450)
                text12=bigFont.render('BCA/40077/17',False,(255,255,255))
                textdisp7=text12.get_rect()
                textdisp7.center=(300,450)
                text13=bigFont.render('BCA/40085/17',False,(255,255,255))
                textdisp8=text13.get_rect()
                textdisp8.center=(500,450)
                text14=bigFont.render('BCA/40088/17',False,(255,255,255))
                textdisp9=text14.get_rect()
                textdisp9.center=(700,450)
                text15=bigFont.render('BCA/40107/17',False,(255,255,255))
                textdisp10=text15.get_rect()
                textdisp10.center=(900,450)
       
                credits.blit(search1,(0,0))
                credits.blit(heading1,texthead1)
                credits.blit(text6,textdisp3)
                credits.blit(text7,textdisp1)
                credits.blit(text8,textdisp2)
                credits.blit(text9,textdisp4)
                credits.blit(text10,textdisp5)
                credits.blit(text11,textdisp6)
                credits.blit(text12,textdisp7)
                credits.blit(text13,textdisp8)
                credits.blit(text14,textdisp9)
                credits.blit(text15,textdisp10)
                credits.blit(text,ctextdisp)
screen1=Mainwindow()
screen2=Game()
screen3=Help()
screen4=Credits()
#screen5=High_Score()
state=0
FPS=30
fpsclock=pygame.time.Clock()

add_num()
num_challenge()
level_timer()
timer=level_change[0]
#print timer
#print level_change
while True:
        if state==0:
                screen1.draw()
        if state==1:
                elapsed=elapsed+fpsclock.tick()
                #print elapsed
                if elapsed>1000:
                        if timer>0:
                                timer-=1
                                Click.play()
                        else:
                                message="You lost the game"          
                        elapsed=0
                screen2.update()
                screen2.draw()
        if state==2:
                screen3.draw()
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                        if state==0:
                                pos= pygame.mouse.get_pos()
                                spotx=pos[0]
                                spoty=pos[1]
                                #if spotx >=25 and spotx <=75 and spoty >=525 and spoty<=575:
                                if textop1.collidepoint(event.pos):
                                        state=1
                                        level_time=0
                                        point=0
                                        level=0
                                        max_time=18
                                        elapsed=0
                                        message=""
                                        add_num()
                                        num_challenge()
                                        level_timer()
                                        timer=level_change[0]
                                        screen2.draw()
                                elif textop2.collidepoint(event.pos):
                                #elif spotx >=925 and spotx <=975 and spoty >=525 and spoty<=575:
                                        state=2
                                        screen3.draw()
                                elif textop3.collidepoint(event.pos):
                                #elif spotx >=925 and spotx <=975 and spoty >=525 and spoty<=575:
                                        state=3
                                        screen4.draw()
                        elif state==2:
                                pos= pygame.mouse.get_pos()
                                spotx=pos[0]
                                spoty=pos[1]
                                if textdisp.collidepoint(event.pos):
                                        state=0
                                        screen1.draw()
                        elif state==3:
                                pos= pygame.mouse.get_pos()
                                spotx=pos[0]
                                spoty=pos[1]
                                if ctextdisp.collidepoint(event.pos):
                                        state=0
                                        screen1.draw()
                        elif state==1:
                                pos=pygame.mouse.get_pos()
                                x_check=pos[0]//150
                                y_check=pos[1]//150
                                #print x_check,'\n',y_check
                                if pos[0]<600 and pos[1]<600:
                                        if level<10 and timer>0 and Matrix[x_check][y_check]==randomNum[level]:
                                                correct1.play()
                                                point+=timer+10*(level)
                                                timer=level_change[level_time]
                                                level+=1
                                                if level==10:
                                                        correct.play()
                                                        level_time+=1
                                                        timer=level_change[level_time]
                                                        add_num()
                                                        level=0
                                                        num_challenge()
                                                        if level_time==10:
                                                                message="You won the game"
                                        else:
                                                message="You lost the game"
                                                 
                                                timer=0
                                elif menu.collidepoint(event.pos):
                                #elif pos[0]>820 and pos[0]<=940 and pos[1]>540 and pos[1]<600:
                                        state=0
                                        screen1.draw()

                               
                                #print level,timer,Matrix[x_check][y_check],randomNum[level],"\n"
                                #screen2.screen()
        pygame.display.update()
