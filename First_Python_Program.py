import pygame
import random

def two_point_form(x1, y1, x2, y2):
    def line_equation(x):
        return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

    return line_equation

pygame.init()
pygame.font.init()

# Initializing the clock
clock = pygame.time.Clock()

# Set up the display (window)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flopi birb")
fps = 60;

# Background
back_image = pygame.image.load('back.png')
back_rect1 = back_image.get_rect()
back_rect2 = back_image.get_rect()
back_rect2.x = screen.get_width()
backgroudMoveSpeed = 30

# Initializarea spriteului pasarii
sprite_image1 = pygame.image.load('birb_1.png')
sprite_image2 = pygame.image.load('birb_2.png')
sprite_image3 = pygame.image.load('birb_3.png')
curSpriteImage = sprite_image1
sprite_imagesVector = []
sprite_imagesVector.extend([sprite_image1,sprite_image2,sprite_image3])
sprite_imagesVectorCopy = sprite_imagesVector.copy()
curSpriteImageCopy = sprite_imagesVectorCopy[0]
#
copyOfImage = pygame.image.load('birb_1.png')
sprite_rect = sprite_image1.get_rect()
sprite_rect.center = (sprite_rect.width//2,sprite_rect.height//2)
# Put the birb in the middle of the screen
sprite_rect.x = screen.get_width()//2-100
sprite_rect.y = screen.get_height()//2
sprite_position = [float(sprite_rect.x-100),float(sprite_rect.y)]
birbDown = False


curSpriteImageIndex = 0
SpriteAnimSpeed = 0.1
AnimTick = 0
SpriteAnimDir = False
def TickBirbAnimation ():
    global AnimTick, curSpriteImage, curSpriteImageCopy, SpriteAnimDir, curSpriteImageIndex, sprite_imagesVector, sprite_imagesVectorCopy
    AnimTick += 1 * delta_time
    if AnimTick >= SpriteAnimSpeed:
        AnimTick = 0
        if SpriteAnimDir == False:
            curSpriteImageIndex += 1
            if curSpriteImageIndex == 2:
                SpriteAnimDir = True
        elif SpriteAnimDir == True:
            curSpriteImageIndex -= 1
            if curSpriteImageIndex == 0:
                SpriteAnimDir = False
        curSpriteImageCopy = sprite_imagesVectorCopy[curSpriteImageIndex]
        curSpriteImage = pygame.transform.rotate(curSpriteImageCopy,line_equation(verticalAccel))

# Vertical acceleration
maxVerticalAccel = 600
verticalAccel = 0
verticalDecel = 1000

# Space Pressed
spacePressed = False
accelWhenPress = -400

# Making the line equation to calculate the angle based on the Acceleration.
# Max Acceleration = -45 degrees
# Min Acceleration = 45 degrees
line_equation = two_point_form(maxVerticalAccel,-45,accelWhenPress,45)

# Variables for delta time calculation
clock = pygame.time.Clock()
delta_time = 0

# Pipes
isGameOver = False
pipesVector = []
pipeTextureUp = pygame.image.load("pipe_up.png")
pipeTextureDown = pygame.image.load("pipe_down.png")
maxHeightRandom = 150
pipeMoveSpeed = 200
distanceBetwenPipes = 300

# Define the color (red in RGB format)
red = (255, 0, 0)

class PipePair:

    def __init__(self):
        # Initialize the top and bottom rectangles of the pipe pair
        self.top_rect = pipeTextureUp.get_rect()
        self.bottom_rect = pipeTextureDown.get_rect()
        self.pointSurface = pygame.Surface((83, 206))
        self.pointSurface.fill(red)
        self.pointRect = self.pointSurface.get_rect()
        self.disablePoint = False

    def move(self):
        # Move both pipe rectangles to the left by pipeMoveSpeed
        self.top_rect.x -= pipeMoveSpeed * delta_time
        self.bottom_rect.x -= pipeMoveSpeed * delta_time
        self.pointRect.x -= pipeMoveSpeed * delta_time

    def draw(self, screen):
        # Draw both pipe rectangles on the screen
        screen.blit(pipeTextureUp,self.top_rect)
        screen.blit(pipeTextureDown,self.bottom_rect)
        #screen.blit(self.pointSurface,self.pointRect) DEBUG

    def setX(self, x):
        self.top_rect.x = x
        self.bottom_rect.x = x
        self.bottom_rect.y = self.top_rect.y + pipeTextureUp.get_height() + 206
        self.pointRect.x = self.top_rect.x + 30
        self.pointRect.y = self.top_rect.y + pipeTextureUp.get_height()

    def setY(self,y):
        self.top_rect.y = y
        self.bottom_rect.y = self.top_rect.y + pipeTextureUp.get_height() + 206
        self.pointRect.x = self.top_rect.x + 30
        self.pointRect.y = self.top_rect.y + pipeTextureUp.get_height()

    def respawnPipe (self):
        self.top_rect.x = 800
        self.bottom_rect.x = 800
        self.top_rect.y = -225 + random.randint(-maxHeightRandom,maxHeightRandom)
        self.bottom_rect.y = self.top_rect.y + pipeTextureUp.get_height() + 206
        self.pointRect.x = self.top_rect.x + 30
        self.pointRect.y = self.top_rect.y + pipeTextureUp.get_height()
        self.disablePoint = False

    def getX (self):
        return self.top_rect.x

    def getIfDisabledPoint(self):
        return self.disablePoint

    def setDisablePoint (self,state):
        self.disablePoint = state

    def isCollidingPipe (self):
        return self.top_rect.colliderect(collisionRect) or self.bottom_rect.colliderect(collisionRect)

    def isCollidingPoint (self):
        return self.pointRect.colliderect(collisionRect)
    
    def Restart():
        # Set the pipes start position
        pipePositionOffset = 800
        for pipe in pipesVector:
            pipe.setX(pipePositionOffset)
            pipePositionOffset += distanceBetwenPipes
            pipe.setY(-225 + random.randint(-maxHeightRandom,maxHeightRandom))
            pipe.disablePoint = False
        # Restart the bird
        # Initializarea spriteului pasarii
        global sprite_rect, sprite_position, birbDown, verticalAccel, curSpriteImage, curSpriteImageCopy
        sprite_rect = copyOfImage.get_rect()
        sprite_rect.center = (sprite_rect.width//2,sprite_rect.height//2)
        # Put the birb in the middle of the screen
        sprite_rect.x = screen.get_width()//2-100
        sprite_rect.y = screen.get_height()//2
        sprite_position = [float(sprite_rect.x-100),float(sprite_rect.y)]
        birbDown = False
        # Vertical acceleration
        verticalAccel = 0
        # Resets the angle
        curSpriteImage = curSpriteImageCopy
        
        

# Instantiate the 3 pipes at cord 0
pipe1 = PipePair()
pipe2 = PipePair()
pipe3 = PipePair()
# Create the pipes vector and insert them inside
pipesVector.extend([pipe1,pipe2,pipe3])
# Set the pipes start position
pipePositionOffset = 800
for pipe in pipesVector:
    pipe.setX(pipePositionOffset)
    pipePositionOffset += distanceBetwenPipes
    pipe.setY(-225 + random.randint(-maxHeightRandom,maxHeightRandom))

# Birb box for colision
# Create a surface with the specified size and color
collisionRectSize = 30
collisionSurface = pygame.Surface((collisionRectSize, collisionRectSize))
collisionSurface.fill(red)
# Get a rect object that corresponds to the surface
collisionRect = collisionSurface.get_rect()

class Score:

    # Static members
    font = pygame.font.Font(None, 48)
    white = (255, 255, 255)

    def __init__(self):
        self.score = 0
        self.scoreText = Score.font.render("Score: 0", True, Score.white)
        self.scoreTextRect = self.scoreText.get_rect()
        self.scoreTextRect.move_ip(10,10)

    def addPoint(self):
        self.score += 1
        scoreSting = "Score: " + str(self.score)
        self.scoreText = Score.font.render(scoreSting, True, Score.white)

    def Restart(self):
        self.score = 0
        self.scoreText = Score.font.render("Score: 0", True, Score.white)

    def GetScore(self):
        return self.score

class OverText:

    # Static members
    font = pygame.font.Font(None, 60)
    white = (255, 255, 255)
    isGameStart = True

    def __init__(self):
        self.startText = OverText.font.render("Press 'Space' to Start", True, OverText.white)
        self.startTextRect = self.startText.get_rect()
        self.startTextRect.move_ip((screen.get_width() // 2)-(self.startTextRect.width // 2),((screen.get_height()//2)-(self.startTextRect.height//2))-50)
        self.gameOverText = OverText.font.render("Game Over", True, OverText.white)
        self.gameOverTextRect = self.gameOverText.get_rect()
        self.gameOverTextRect.move_ip((screen.get_width() // 2)-(self.gameOverTextRect.width // 2),((screen.get_height()//2)-(self.gameOverTextRect.height//2))-50)

    def Draw (self,screen):
        if OverText.isGameStart == True:
            screen.blit(self.startText, self.startTextRect)
        if isGameOver == True:
            screen.blit(self.gameOverText,self.gameOverTextRect)

# Init Score
score = Score()
overText = OverText()

import Highscore as hs
# Highscore
hs.Highscore.init()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if isGameOver == False:
                OverText.isGameStart = False
            if spacePressed == False and isGameOver == False:
                spacePressed = True
                verticalAccel = accelWhenPress
            if birbDown == True and isGameOver == True:
                PipePair.Restart()
                score.Restart()
                birbDown = False
                isGameOver = False
                OverText.isGameStart = True
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if spacePressed == True:
                spacePressed = False

    # Calculate delta time
    delta_time = clock.tick(60) / 1000.0  # Assuming a target frame rate of 60 FPS

    if OverText.isGameStart == False:
        # Change the float position and increase the accel every tick until maxAccel isn't reached
        if birbDown == False:
            sprite_position[1] += verticalAccel * delta_time
            if verticalAccel < maxVerticalAccel:
                verticalAccel += verticalDecel * delta_time
    
        # Clip the position so the birb isn't exiting the window
        if sprite_rect.y < 0:
            sprite_rect.y = 0
            sprite_position[1] = 0
        elif sprite_rect.y > screen.get_height() - sprite_rect.height:
            sprite_rect.y = screen.get_height() - sprite_rect.height
            sprite_position[1] = screen.get_height() - sprite_rect.height
            isGameOver = True
            birbDown = True
            hs.Highscore.UpdateHighScore(score.GetScore())

        # Moving the sprite
        sprite_rect.y = sprite_position[1]
        # Move the collision rect to the bird position
        collisionRect.x = sprite_rect.x+15
        collisionRect.y = sprite_rect.y+15

        # Change the angle of the birb
        curSpriteImage = pygame.transform.rotate(curSpriteImageCopy,line_equation(verticalAccel))

        # Move the background
        #back_rect1.x -= backgroudMoveSpeed * delta_time
        #back_rect2.x -= backgroudMoveSpeed * delta_time
        #if back_rect1.x <= -800:
        #    back_rect1.x = 800
        #if back_rect2.x <= -800:
        #    back_rect2.x = 800

        # Move the pipes
        if isGameOver == False:
            for pipe in pipesVector:
                pipe.move()
                # Respawns the pipe to the right of the window when it gets to the left
                if pipe.getX() < -pipeTextureUp.get_width():
                    PipePair.respawnPipe(pipe)

        # Check if collision rect touches one of the pipes
        for pipe in pipesVector:
            if pipe.isCollidingPipe() == True:
                isGameOver = True
                hs.Highscore.UpdateHighScore(score.GetScore())
            if pipe.isCollidingPoint() == True and pipe.getIfDisabledPoint() == False:
                score.addPoint()
                pipe.setDisablePoint(True)
        # Animation Tick
        if (isGameOver == False):
            TickBirbAnimation()

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with a background color (e.g., black)

    # Draw the background then the sprite
    screen.blit(back_image,back_rect1)
    # Draw the pipes
    for pipe in pipesVector:
        pipe.draw(screen)
    # Draw the bird
    screen.blit(curSpriteImage, sprite_rect)
    # Draw the collider surface
    #screen.blit(collisionSurface,collisionRect)
    # Draw the score
    screen.blit(score.scoreText, score.scoreTextRect)
    # Draw over text
    overText.Draw(screen)
    # Draw highscore
    hs.Highscore.Draw(screen,isGameOver)

    pygame.display.update()  # Update the display
pygame.quit()