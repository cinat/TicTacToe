import pygame as pg,sys
from pygame.locals import *
import time

#Initialization of variables 
height=400
width=400
current_player = 'x'
#TicTacToe 3x3 board
TTT =[[None]*3,[None]*3,[None]*3]
winner = None
draw= False
line_color=(10,10,10)
bg_color =(255,255,255)

#Initializing the window
pg.init()
fps=30
clock = pg.time.Clock()
screen=pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

#Loading the images
opening=pg.image.load('C:\\Users\\Rishav\\OneDrive\\Desktop\\TicTacToe\\start.png')
x_img=pg.image.load('C:\\Users\\Rishav\\OneDrive\\Desktop\\TicTacToe\\x.png')
o_img=pg.image.load('C:\\Users\\Rishav\\OneDrive\\Desktop\\TicTacToe\\o.png')

#resizing the images
x_img=pg.transform.scale(x_img,(80,80))
o_img=pg.transform.scale(o_img,(80,80))
opening=pg.transform.scale(opening,(400,500))


def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(2)
    screen.fill(bg_color)
 #drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(2*width/3,0),(2*width/3,height),7)
 #drawing horizontal lines
    pg.draw.line(screen, line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,2*height/3),(width,2*height/3),7)
    draw_status()

def draw_status():
    global draw

    if winner is None :
        message = current_player.upper() + " 's Turn"
    else:
        message = winner.upper() + "  won!"
    if draw :
        message= 'Game Draw!'
    
    font= pg.font.Font(None,30)
    text=font.render(message,1,(255,255,255))

    screen.fill((0,0,0),(0,400,500,100))
    text_rect=text.get_rect(center=(width/2,450))

    screen.blit(text,text_rect)
    pg.display.update()

def check_win():
    global TTT, winner, draw

    #check for winning rows
    for row in range (0,3):
        if ((TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0] is not None)):
           winner=TTT[row][0]
           pg.draw.line(screen,(190,10,10),(0,((row+1)*height/3-height/6)),(width,((row+1)*(height/3)-height/6)),8)

    #check for winning coloums  
    for col in range (0,3):
       if((TTT[0][col]==TTT[1][col]==TTT[2][col]) and (TTT[0][col] is not None)):
         winner=TTT[0][col]
         pg.draw.line(screen,(190,10,10),((col+1)*(width/3)-width/6,0),((col+1)*(width/3)-width/6,height),8)

    #check for winning diagonals
    if(TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0] is not None):
        winner=TTT[0][0]
        pg.draw.line(screen,(190,10,10),(width/6,height/6),((width-width/6),height-height/6),8)

    if(TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[0][2] is not None) :
         winner= TTT[0][2]
         pg.draw.line(screen,(190,10,10),((width-width/6),height/6),(width/6,(height-height/6)),8)

    if(all((all (row) for row in TTT)) and winner is None):
          draw= True
    draw_status()

# Drawing X or O
def drawcurrent_player(row,col):
    global TTT, current_player
    if row==1 :
     posx= 30
    if row==2:
     posx= width/3+30
    if row==3:
     posx=width/3*2+30
     
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30 
    TTT[row-1][col-1] = current_player
    if(current_player == 'x'):
        screen.blit(x_img,(posy,posx))
        current_player= 'o'
    else:
        screen.blit(o_img,(posy,posx))
        current_player= 'x'
    pg.display.update()
    
  #Detecting the position
def userclick():
      x,y= pg.mouse.get_pos()
      
      if(x<width/3):
         col=1
      
      elif(x<width/3*2):
          col=2
      
      elif(x<width):
         col=3    
         
      else  :
          col=None
       
      if(y<height/3):
         row=1
      elif(y<height/3*2):
          row=2
      elif(y<height):
          row=3
      else:
          row=None
      if(row and col and TTT[row-1][col-1]is None):
          global current_player
          drawcurrent_player(row,col)
          check_win()      
          
          
#Resetting the game
def reset_game():
    global TTT, winner,current_player, draw
    time.sleep(3)
    current_player = 'x'
    draw = False
    game_opening()
    winner=None
    TTT = [[None]*3,[None]*3,[None]*3]
    draw_status()

game_opening()

#run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type== QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            userclick()
            if(winner or draw):
             reset_game()
    pg.display.update()
    clock.tick(fps)         