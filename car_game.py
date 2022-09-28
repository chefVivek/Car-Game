import random
import pygame, sys
from pygame.locals import *
import tkinter as tk
from pygame import mixer

#Instantiate mixer for music
mixer.init()
#Load audio file
mixer.music.load('E:\Mero-Balma-Thanedar_320(PaglaSongs).mp3')
#Set preferred volume
mixer.music.set_volume(0.2)
#Play the music
mixer.music.play()





size = width ,height = (250,600)#creating a size variable to use it for relative coordinates
road_w = int(width/1.2)
roadmark_w = int(width/100)
right_lane = float(width/2+road_w/4)
left_lane = float(width/2-road_w/4)
speed = 1.0
score = 0
###INITIALIZING
pygame.init()
running = True

screen = pygame.display.set_mode(size)#set window size(width,height)
pygame.display.set_caption("car game")#set title
screen.fill(color="aqua")#set bg colour
pygame.display.update()

##LOAD IMAGES
#player vehicle
car = pygame.image.load(r"C:\Users\Vivek\Desktop\car game\Car-Game\car3.png")
car = pygame.transform.scale(car, (110, 110))
car_loc=car.get_rect()
car_loc.center = right_lane, height*0.86
#enemy vehicle
car2 = pygame.image.load(r"C:\Users\Vivek\Desktop\car game\Car-Game\policecar.png")
car2 = pygame.transform.scale(car2, (110, 110))
car2_loc=car2.get_rect()
car2_loc.center = left_lane, height*0.1


counter = 0 
clock = pygame.time.Clock()
#GAME LOOP
while running:#ittrate all the event of our application with a for loop
    counter +=1
    if counter == 2000.0:
        speed += 0.25
        counter = 0.0
        print("level up") 
    ##animate ENEMY CAR 
    
    car2_loc[1] += speed#putting the enemy car 1 pixel below
    #print("car2_loc: speed ",car2_loc[1],"  :  ",speed).......for testing
    #here [1] means height [0] means width
    if car2_loc[1] > height:
        score+=1
        if random.randint(0,1) == 0:
          car2_loc.center = right_lane,0
        else:
            car2_loc.center = left_lane,0
    #end game condition
    if car_loc[0] == car2_loc[0] :#if x cordinate of both car is same
        if car2_loc[1] > car_loc[1]-109: #if y cordinate of enemy car is greater than your car
         print ("game over")
         print("your score:",score)
         break
    
    # Flip everything to the display, controling speed of car
    pygame.display.flip()
    # Ensure program maintains a rate of 400 frames per second
    clock.tick(400)

    ##EVENT LISTENERS
    for event in pygame.event.get():# all the event of our application are stored in pygame.event module , and we are fetching them with get() method
        if event.type == QUIT:#we are just focusing on quit event here
            running= False
        if event.type == KEYDOWN:# all the keys entered by user
            if event.key in [K_a,K_LEFT]:
                if int(car_loc[0]) > int(road_w/2):
                 car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_d,K_RIGHT] and int(car_loc[0]) < int(road_w/2):
                car_loc = car_loc.move([int(road_w/2),0]) 
    
    ##DRAWING GRAPHICS
    pygame.draw.rect(#designing an rectangle on screen that will represent road here
        screen,
        (50,50,50),#colour of shape i.e black(r,g,b)
        (width/2-road_w/2,0,road_w,height))#(x_cordinate > width/2 i.e center of screen width, y_axis >0 i.e full y axis, width of shape i.e road_w, height of shape > heightn i.e height of screen ,full)
    #to put road in center we reduce x cordinate with road_w/2 

    pygame.draw.rect(#designing rectangle for center road strips
        screen,
        (255,255,255),
        (width/2 - roadmark_w/2,0 ,roadmark_w,height))
    

    pygame.draw.rect(#designing strips at left boarder of road
        screen,
        (255,255,255),
        (width/2 -road_w/2+ roadmark_w*2,0 ,roadmark_w,height))

    pygame.draw.rect(#designing strips at right border of road
        screen,
        (255,255,255),
        (width/2 + road_w/2- roadmark_w*3,0 ,roadmark_w,height))
    
    
   
    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()



###QUITING
pygame.quit()

#               #
#               #
#               #
#               #
#-results here- #
#               #
#               #
#               #
#               #

#designing form
root=tk.Tk()
canvas = tk.Canvas(root, width=350, height=600)
canvas.grid(columnspan=3,rowspan=10)

#text box
text_box= tk.Text(root,height=1,width=20,padx=15,pady=15)
text_box.insert(1.0, ["your_score_:",score])
text_box.tag_configure("center",justify="center")
text_box.tag_add("center",1.0,"end")
text_box.grid(column=1,row=3)
root.mainloop()




