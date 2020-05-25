import pgzrun
from random import randint
WIDTH = 450 
HEIGHT =360 
score = 0  

game_over = False 

# Fox image, and initial position
fox = Actor("fox")
fox.pos = 100, 100

# Get coin image, and initial position
#coin1=[]
coin=Actor("coin")
num=6
spike = Actor("spike")
spike.pos = 200, 200
def multi():
        global c
        c=[]
        for i in range(3):
                c.append(Actor("coin",(randint(20,450),randint(20,340))))

def draw():

        screen.blit("spike",(0,0))
        fox.draw()
        
        for i in c:
                i.draw()
       
        screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))
	

	# Game Over Screen
        if game_over:
		
                screen.fill("yellow") 
                screen.draw.text("Times Up! :( ", topleft=(10,60), fontsize=60) 

                screen.draw.text("Final Score: " + str(score), color="black", topleft=(10,10), fontsize=60) 
		
def time_up():
        global game_over
        global c
        game_over = True

def update():
        global c
        
        global score

        global game_over

        if keyboard.left:
                fox.x = fox.x - 5
		
        if keyboard.right:
                fox.x = fox.x + 5
                fox.image = "fox"
        if keyboard.up:
                fox.y = fox.y - 5

        if keyboard.down:
                fox.y = fox.y + 5
        
        
        for i in range(3):
        
                if not game_over:
                        if fox.colliderect(c[i]):
                                score = score + 1
                                multi()
                               
                                
                        
                
		





multi()

clock.schedule_interval(multi,5)
clock.schedule(time_up, 16.0)
pgzrun.go()
