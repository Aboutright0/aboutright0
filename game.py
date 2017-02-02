#Imports
import pygame
from pygame import *

#Screen Dimensions

WIN_WIDTH = 768
WIN_HEIGHT = 672
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

#Screen Defaults

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

#Init, Create Screen
pygame.init()
screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

##############Drawing Code##############

#Load Megaman Sprite Sheet
spritesheet = pygame.image.load("Media/Graphics/megamansprite.png")

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-78,-12))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
standleft = stage

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-53,-12))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
blinkleft = stage

standloopleft = [standleft, blinkleft]

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-237,-12))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
standright = stage

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-262,-12))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
blinkright = stage

standloopright = [standright, blinkright]

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-173,-38))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
stepright = stage

character = Surface((25,22),pygame.SRCALPHA)
character.blit(spritesheet,(-194,-38))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright1 = stage

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-220,-38))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright2 = stage

character = Surface((25,22),pygame.SRCALPHA)
character.blit(spritesheet,(-238,-38))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright3 = stage

walkloopright = [stepright, runright1, runright2, runright3]

character = Surface((19,22),pygame.SRCALPHA)
character.blit(spritesheet,(-142,-38))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
stepleft = stage

character = Surface((24,22),pygame.SRCALPHA)
character.blit(spritesheet,(-115,-38))
character = pygame.transform.scale(character,(24*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runleft1 = stage

character = Surface((16,22),pygame.SRCALPHA)
character.blit(spritesheet,(-97,-38))
character = pygame.transform.scale(character,(16*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runleft2 = stage

character = Surface((21,22),pygame.SRCALPHA)
character.blit(spritesheet,(-74,-38))
character = pygame.transform.scale(character,(21*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runleft3 = stage

walkloopleft = [stepleft, runleft1, runleft2, runleft3]

character = Surface((25,30),pygame.SRCALPHA)
character.blit(spritesheet,(-136,-63))
character = pygame.transform.scale(character,(25*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(108,0))
fallleft = stage

fallleftloop = [fallleft]

character = Surface((25,30),pygame.SRCALPHA)
character.blit(spritesheet,(-172,-63))
character = pygame.transform.scale(character,(25*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
fallright = stage

fallrightloop = [fallright]

character = Surface((31,22),pygame.SRCALPHA)
character.blit(spritesheet,(-132,-96))
character = pygame.transform.scale(character, (31*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(88,0)) 
shootleftstand = stage

shootleftstandloop = [shootleftstand]

character = Surface((32,22),pygame.SRCALPHA)
character.blit(spritesheet,(-99,-96))
character = pygame.transform.scale(character, (32*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(88,0))
shootleftrun1 = stage

character = Surface((26,22),pygame.SRCALPHA)
character.blit(spritesheet,(-69,-96))
character = pygame.transform.scale(character, (26*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(88,0))
shootleftrun2 = stage

character = Surface((30,22),pygame.SRCALPHA)
character.blit(spritesheet,(-36,-96))
character = pygame.transform.scale(character, (30*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(88,0))
shootleftrun3 = stage

shootleftrunloop = [shootleftstand, shootleftrun1, shootleftrun2, shootleftrun3]

character = Surface((31,22),pygame.SRCALPHA)
character.blit(spritesheet,(-172,-96))
character = pygame.transform.scale(character, (31*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightstand = stage

shootrightstandloop = [shootrightstand]

character = Surface((29,22),pygame.SRCALPHA)
character.blit(spritesheet,(-206,-96))
character = pygame.transform.scale(character, (29*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun1 = stage

character = Surface((26,22),pygame.SRCALPHA)
character.blit(spritesheet,(-239,-96))
character = pygame.transform.scale(character, (26*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun2 = stage

character = Surface((30,24),pygame.SRCALPHA)
character.blit(spritesheet,(-268,-96))
character = pygame.transform.scale(character, (30*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun3 = stage

shootrightrunloop = [shootrightstand, shootrightrun1, shootrightrun2, shootrightrun3]

character = Surface((29,30),pygame.SRCALPHA)
character.blit(spritesheet,(-75,-63))
character = pygame.transform.scale(character, (29*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(96,0))
shootfallleft = stage

shootleftfallloop = [shootfallleft]

character = Surface((29,30),pygame.SRCALPHA)
character.blit(spritesheet,(-230,-63))
character = pygame.transform.scale(character, (29*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootfallright = stage

shootrightfallloop = [shootfallright]

character = Surface((28,28),pygame.SRCALPHA)
character.blit(spritesheet,(-106,-122))
character = pygame.transform.scale(character, (28*4,28*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
takedamageleft = stage

takedamageleftloop = [takedamageleft]

character = Surface((26,28),pygame.SRCALPHA)
character.blit(spritesheet,(-136,-122))
character = pygame.transform.scale(character, (26*4,28*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
takedamageleftair = stage

character = Surface((26,28),pygame.SRCALPHA)
character.blit(spritesheet,(-172,-122))
character = pygame.transform.scale(character, (26*4,28*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
takedamagerightair = stage

character = Surface((28,28),pygame.SRCALPHA)
character.blit(spritesheet,(-200,-122))
character = pygame.transform.scale(character, (28*4,28*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
takedamageright = stage

#Load Buster Shots Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/bustershots2.png")

character = Surface((12,13),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-80))
character = pygame.transform.scale(character, (25*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(40,0))
bustershot1 = stage

character = Surface((21,13),pygame.SRCALPHA)
character.blit(spritesheet,(-64,-80))
character = pygame.transform.scale(character, (21*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershot2 = stage

character = Surface((13,13),pygame.SRCALPHA)
character.blit(spritesheet,(-94,-80))
character = pygame.transform.scale(character, (13*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershot3 = stage

character = Surface((19,13),pygame.SRCALPHA)
character.blit(spritesheet,(-113,-80))
character = pygame.transform.scale(character, (19*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershot4 = stage

#Load SMB Enemies Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/smbenemiessheet.png")

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(0,-4))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaleft = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-30,-4))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaright = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-60,0))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombadead = stage

goombawalk = [goombaleft, goombaright]

#Load Explosion Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/explosion.png")

explodex = 68
explodey = -6

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-117))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode1 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-181))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode2 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-245))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode3 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-309))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode4 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-373))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode5 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-437))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode6 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-502))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode7 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-566))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode8 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-631))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode9 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-696))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode10 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-760))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-761))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-826))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode12 = stage

explosion = [explode1,explode2,explode3,explode4,explode5,explode6,explode7,explode8,explode9,explode10,explode11,explode12]

#Load Bubble Bobble Enemies Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/bubblebobble.png")

character = Surface((14,16),pygame.SRCALPHA)
character.blit(spritesheet,(-6,-5))
character = pygame.transform.scale(character, (14*4,16*4))
stage = Surface((300,16*4),pygame.SRCALPHA)
stage.blit(character,(130,0))
toasterwalk1 = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-26,-5))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,16*4),pygame.SRCALPHA)
stage.blit(character,(130,0))
toasterwalk2 = stage

toasterwalkloop = [toasterwalk1,toasterwalk2]

#Load Item Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/item.png")

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-4))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe1 = stage

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-66))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe2 = stage

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-128))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe3 = stage

itemloop = [itemframe1, itemframe2, itemframe3]

########################################

#Main Function
def main():

    #Create clock, set caption
    timer = pygame.time.Clock()
    pygame.display.set_caption("Use arrows to move!")

    #Create Game
    game = Game()

    #Create Player
    player = Player(game)

    #Create Display
    display = Display("")

    #Create level
    room = Rooms(game,player)

    #Main Loop
    while 1:
        timer.tick(60)
        
        if game.screenfocus == "Title":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))
            game.title.update()

        if game.screenfocus == "Game":
            game.camera.update(game.camerafocus)
            player.update()
        
            for e in game.entities:
                screen.blit(e.image, game.camera.apply(e))
            for e in game.exitgroup:
                screen.blit(e.image, game.camera.apply(e))
            for e in game.itemgroup:
                e.update()
                screen.blit(e.image, game.camera.apply(e))
            for e in game.playerentity:
                screen.blit(e.image, game.camera.apply(e))
            for e in game.projectilegroup:
                e.update(game.platforms)
                screen.blit(e.image, game.camera.apply(e))
            for e in game.enemygroup:
                e.update(game.platforms,game.projectilegroup)
                screen.blit(e.image, game.camera.apply(e))

            #Uncomment To View Objects Detectable Area
            #for e in game.detectablegroup: screen.blit(e.image, game.camera.apply(e))
            
            display.update(player.lifetotal[player.currentlifetotal])
            screen.blit(display.image,(96,96))

        if game.screenfocus == "Game Over":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))

        if game.screenfocus == "Level Complete":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))

        if game.screenfocus == "Pause Menu":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))
            game.pausemenu.update()

        pygame.display.update()

class Game(object):
    def __init__(self):
        #Create Sprite Groups
        self.entities = pygame.sprite.Group()
        self.playerentity = pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemygroup = pygame.sprite.Group()
        self.exitgroup = pygame.sprite.Group()
        self.menugroup = pygame.sprite.Group()
        self.titlegroup = pygame.sprite.Group()
        self.detectablegroup = pygame.sprite.Group()
        self.itemgroup = pygame.sprite.Group()
        #Create Camera
        self.camera = ""
        self.camerafocus = ""
        #Create Platforms
        self.platforms = []
        #Create Screen Focus
        self.screenfocus = "Title"
        #Create Title
        self.title = Title(self)
        #Create Gameover
        self.gameover = GameOver(self)
        #Create Level Complete
        self.levelcomplete = LevelComplete(self)
        #Create Pause Menu
        self.pausemenu = PauseMenu(self)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y, w, h):
        Entity.__init__(self)
        self.rect = Rect(x*3,y*3,w*3,h*3)
    def update(self):
        pass
        
class Player(Entity):
    def __init__(self, game):
        Entity.__init__(self)
        #Add Player to Game
        self.game = game
        self.game.playerentity.add(self)
        #Set Player Velocities
        self.xvel = 0
        self.yvel = 0
        #Set Player Offsets
        self.xoffset = -128
        self.yoffset = 0
        #Counters
        self.walkcounter = 0
        self.standcounter = 0
        self.attackcounter = 0
        self.takedamagecounter = 0
        #States
        self.collideright = False
        self.onGround = True
        self.airborne = False
        self.faceright = True
        self.takingdamage = False
        self.attacking = False
        self.moving = False
        #Create Player Sprite
        self.image = Surface((300, 150),pygame.SRCALPHA)
        self.rect = Rect(0, 0, 300, 150)
        #Create Player Detectable Area
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(0, 0, 80, 90)
        self.detectable.image = Surface((80,90))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        self.game.detectablegroup.add(self.detectable)
        #Life Meter
        self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll"]
        self.currentlifetotal = 9
        #Inputs
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.space = False       
    def startingposition(self,x,y):
        self.rect = Rect(x, y, 300, 150)
        self.detectable.rect = Rect(x, y, 80, 90)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                self.up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                self.down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                self.left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                self.right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.space = True
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.game.pausemenu.createpausemenu()
                self.game.screenfocus = "Pause Menu"
            if e.type == KEYUP and e.key == K_SPACE:
                self.space = False    
            if e.type == KEYUP and e.key == K_UP:
                self.up = False
            if e.type == KEYUP and e.key == K_DOWN:
                self.down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                self.right = False
                self.counter = 0
            if e.type == KEYUP and e.key == K_LEFT:
                self.left = False
                self.counter = 0
    def update(self):
        self.inputhandler()
        
        #Apply Inputs
        if self.up:
            if self.onGround:
                self.yvel -= 10.6
            # Only jump if on the ground
        if self.down:
            pass
            # Does nothing
        if self.left:
            self.faceright = False
            if self.takingdamage == False:
                self.xvel = -8
                self.moving = True
            # Move if not taking damage
        if self.right:
            self.faceright = True
            if self.takingdamage == False:
                self.xvel = 8
                self.moving = True
            # Move if not taking damage
        if self.space:
            projectile = Projectile(self,self.game)
            self.game.projectilegroup.add(projectile)
            self.space = False
            self.attacking = True
            #Create projectile on space


        #Apply States 
        if self.yvel < 0: self.airborne = True
            #Player is moving up
        if self.yvel > 1.2: self.airborne = True
            #Player is falling
        if self.onGround == True:
            if self.up == True:
                self.airborne == True
            else:
                self.airborne = False
            #Still airborne while pressing up
        if not self.onGround:
            self.yvel += 0.3
            #Apply gravity
            if self.yvel > 100:
                self.yvel = 100
                #Max falling speed
        if not(self.left or self.right):
            if not self.takingdamage:
                self.moving = False
                self.xvel = 0
            #Stop player if not taking damage
        if self.takingdamage:
            if self.collideright:
                self.xvel = -8
            else:
                self.xvel = 8
            #Move player if taking damage
        if self.attackcounter > 8:
            self.attacking = False
            self.attackcounter = 0
            self.standcounter = 0
            #Stop attacking after 9 updates
        if self.takedamagecounter > 13:
            self.takingdamage = False
            self.takedamagecounter = 0
            #Player stops taking damage after 14 updates
        

        #Increase or Reset Counters
        if self.attacking: self.attackcounter = self.attackcounter + 1
        if self.takingdamage: self.takedamagecounter = self.takedamagecounter + 1
        if not self.moving: self.standcounter = 0

        #Collisions
        self.detectable.rect.left += self.xvel
        self.collide(self.xvel, 0)
        self.detectable.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel)

        #Offsets
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()

    def collide(self, xvel, yvel):
        #Collide Platforms
        for p in self.game.platforms:
            if pygame.sprite.collide_rect(self.detectable, p):
                if xvel > 0:
                    self.detectable.rect.right = p.rect.left
                if xvel < 0:
                    self.detectable.rect.left = p.rect.right
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom

        #Collide Enemies
        for e in self.game.enemygroup:
            if pygame.sprite.collide_rect(self.detectable, e.detectable):
                leftdifference = self.detectable.rect.right - e.detectable.rect.left
                rightdifference = self.detectable.rect.left - e.detectable.rect.right
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                self.takingdamage = True
                self.currentlifetotal = self.currentlifetotal - 1
                if self.currentlifetotal <= 0:
                    self.game.gameover.creategameover()
                    self.game.screenfocus = "Game Over"
                    self.currentlifetotal = 0

        #Collide Items
        for i in self.game.itemgroup:
            if pygame.sprite.collide_rect(self.detectable, i.detectable):
                self.game.levelcomplete.createlevelcomplete()
                self.game.screenfocus = "Level Complete"

        #Collide Exits
        for x in self.game.exitgroup:
            if pygame.sprite.collide_rect(self.detectable, x):
                x.changeroom()

    def animate(self):
        
        state = []
        state.append(self.airborne)
        state.append(self.moving)
        state.append(self.faceright)
        state.append(self.takingdamage)
        state.append(self.attacking)

        #Moving
        if state[1]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:
                if state[2]:
                    self.walkloop(walkloopright)
                else:
                    self.walkloop(walkloopleft)
        else:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:
                if state[2]:
                    self.standloop(standloopright)
                else:
                    self.standloop(standloopleft)
        
        #Attacking
        if state[4]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(shootfallright)
                else:
                    self.updatecharacter(shootfallleft)
            else:
                if state[1]:
                    if state[2]:
                        self.walkloop(shootrightrunloop)
                    else:
                        self.walkloop(shootleftrunloop)
                else:
                    if state[2]:
                        self.updatecharacter(shootrightstand)
                    else:
                        self.updatecharacter(shootleftstand)

        #Hurt
        if state[3]:
            if state[2]:
                self.updatecharacter(takedamageright)
            else:
                self.updatecharacter(takedamageleft)

        

    #Standing Animation Loop    
    def standloop(self, loop):
        if self.standcounter == 0 or self.standcounter == 1:
            self.walkcounter = 0
            self.updatecharacter(loop[0])
        elif self.standcounter == 200: self.updatecharacter(loop[1])
        elif self.standcounter == 210:
            self.updatecharacter(loop[0])
            self.standcounter = 0
        self.standcounter = self.standcounter + 1

    #Walking Animation Loop
    def walkloop(self, loop):
        if self.walkcounter == 0 or self.walkcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[1])
        elif self.walkcounter == 5: self.updatecharacter(loop[1])
        elif self.walkcounter == 15: self.updatecharacter(loop[2])
        elif self.walkcounter == 25: self.updatecharacter(loop[3])
        elif self.walkcounter == 35: self.updatecharacter(loop[2])
        elif self.walkcounter == 45:
            self.updatecharacter(loop[1])
            self.walkcounter = 5
        self.walkcounter = self.walkcounter + 1

    #Update Current Frame
    def updatecharacter(self, ansurf): self.image = ansurf

class Projectile(Entity):
    def __init__(self, player,game):
        Entity.__init__(self)
        self.detectable = pygame.sprite.Sprite()
        #Place Projectile Facing Right
        if player.faceright == True:
            self.xvel = 15
            x = player.detectable.rect.right + 18
            y = player.detectable.rect.top + 18
            self.image = bustershot1
            self.detectable.rect = Rect(x, y, 32, 32)
        #Place Projectile Facing Left
        elif player.faceright == False:
            self.xvel = -15
            x = player.detectable.rect.left - 114
            y = player.detectable.rect.top + 18
            self.image = pygame.transform.flip(bustershot1, True, False)
            self.detectable.rect = Rect(x, y, 32, 32)
        self.detectable.image = Surface((32,32))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        game.detectablegroup.add(self.detectable)
        self.image = pygame.transform.scale(self.image,(96,96))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
        
    def update(self, platforms):
        self.rect.left += self.xvel
        self.detectable.rect.left += self.xvel
        self.collide(platforms)
    
    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self.detectable, p):
                self.kill()

class Rooms(object):
    def __init__(self,game,player):
        self.width = 0
        self.height = 0
        self.game = game
        self.player = player
        self.createroom1("a")
    def dumpsprites(self):
        self.game.itemgroup.empty()
        self.game.enemygroup.empty()
        self.game.entities.empty()
        self.game.exitgroup.empty()
        self.game.platforms = []
    def resetcamera(self):
        total_level_width  = self.width*3
        total_level_height = self.height*3
        self.game.camera = Camera(complex_camera, total_level_width, total_level_height)
        self.game.camerafocus = self.player.detectable
    def setbackground(self, backgroundpath):
        self.dumpsprites()
        bg = Entity()
        bg.image = pygame.image.load(backgroundpath)
        self.width = bg.image.get_width()
        self.height = bg.image.get_height()
        bg.rect = Rect(0,0,self.width*3,self.height*3)
        bg.image = pygame.transform.scale(bg.image,(self.width*3,self.height*3))
        self.game.entities.add(bg)
        self.resetcamera()
    def createroom1(self, entrance):
        
        #Set Background
        self.setbackground("Media/Graphics/Backgrounds/room1.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(160,318)
        elif entrance == "b": self.player.startingposition(2992,1086)

        #Set Up Enemies
        self.game.enemygroup.add(Goomba(748, 534, -2))
        self.game.enemygroup.add(Toaster(868, 1016, 200, -2))
        self.game.enemygroup.add(Toaster(1672, 1209, 600, -2))
        self.game.enemygroup.add(Toaster(1868, 1209, 600, -2))
        self.game.enemygroup.add(Goomba(2868, 1109, -2))

        #Set Up Platforms
        self.game.platforms.append(Platform(48,424,976,40))
        self.game.platforms.append(Platform(0,0,48,468))
        self.game.platforms.append(Platform(48,136,32,16))
        self.game.platforms.append(Platform(128,200,128,16))
        self.game.platforms.append(Platform(64,264,48,16))
        self.game.platforms.append(Platform(80,328,112,16))
        self.game.platforms.append(Platform(224,360,80,16))
        self.game.platforms.append(Platform(896,392,128,32))
        self.game.platforms.append(Platform(928,280,96,48))
        self.game.platforms.append(Platform(1026,393,64,32))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,1025,328,40,64,3,"a"))
        
    def createroom2(self, entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room2.png")

        #Set Up Player
        if entrance == "a": self.player.startingposition(0,366)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,152,48,72))
        self.game.platforms.append(Platform(48,168,48,56))
        self.game.platforms.append(Platform(96,184,64,40))
        self.game.platforms.append(Platform(160,168,48,56))
        self.game.platforms.append(Platform(208,152,48,72))
        self.game.platforms.append(Platform(224,88,32,64))
        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))
        self.game.platforms.append(Platform(0,0,48,88))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-32,88,32,64,3,"b"))

    def createroom3(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room3.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(8,1086)
        elif entrance == "b": self.player.startingposition(680,2622)
        elif entrance == "c": self.player.startingposition(8,2622)
        elif entrance == "d": self.player.startingposition(688,318)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,0,32,328))
        self.game.platforms.append(Platform(32,0,192,24))
        self.game.platforms.append(Platform(224,0,32,72)) 
        self.game.platforms.append(Platform(112,24,32,64))
        self.game.platforms.append(Platform(32,24,16,16))
        self.game.platforms.append(Platform(96,24,16,16))
        self.game.platforms.append(Platform(144,24,16,16))
        self.game.platforms.append(Platform(208,24,16,16))
        self.game.platforms.append(Platform(112,200,32,288))
        self.game.platforms.append(Platform(144,328,32,16))
        self.game.platforms.append(Platform(144,456,32,16))
        self.game.platforms.append(Platform(224,136,32,704))
        self.game.platforms.append(Platform(192,136,32,16))
        self.game.platforms.append(Platform(192,264,32,16))
        self.game.platforms.append(Platform(192,392,32,16))
        self.game.platforms.append(Platform(192,520,32,16))
        self.game.platforms.append(Platform(112,584,64,16))
        self.game.platforms.append(Platform(0,392,32,448))
        self.game.platforms.append(Platform(32,392,32,16))
        self.game.platforms.append(Platform(32,648,32,16))
        self.game.platforms.append(Platform(32,776,32,16))
        self.game.platforms.append(Platform(112,712,32,432))
        self.game.platforms.append(Platform(144,712,32,16))
        self.game.platforms.append(Platform(80,840,32,16))
        self.game.platforms.append(Platform(80,968,32,16))
        self.game.platforms.append(Platform(80,1096,32,16))
        self.game.platforms.append(Platform(144,1096,32,16))
        self.game.platforms.append(Platform(0,904,32,336))
        self.game.platforms.append(Platform(32,904,32,16))
        self.game.platforms.append(Platform(32,1032,32,16))
        self.game.platforms.append(Platform(32,1160,32,72))
        self.game.platforms.append(Platform(64,1192,32,40))
        self.game.platforms.append(Platform(96,1224,64,8))
        self.game.platforms.append(Platform(160,1192,32,40))
        self.game.platforms.append(Platform(192,1160,32,80))
        self.game.platforms.append(Platform(224,904,32,336))
        self.game.platforms.append(Platform(192,904,32,16))
        self.game.platforms.append(Platform(256,904,32,24))
        self.game.platforms.append(Platform(-32,904,32,16))
        self.game.platforms.append(Platform(-32,392,32,16))
        self.game.platforms.append(Platform(256,136,32,16))

        #Set Up Enemies
        self.game.enemygroup.add(Goomba(360, 510, 2))
        
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-40,328,40,64,1,"b"))
        self.game.exitgroup.add(RoomExit(self,256,840,32,64,2,"a"))
        self.game.exitgroup.add(RoomExit(self,-32,840,32,64,4,"a"))
        self.game.exitgroup.add(RoomExit(self,256,72,32,64,5,"a"))

    def createroom4(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room4.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(672,318)

        #Set Up Platforms
        self.game.platforms.append(Platform(48,168,160,40))
        self.game.platforms.append(Platform(0,0,48,208))
        self.game.platforms.append(Platform(48,0,160,24)) 
        self.game.platforms.append(Platform(208,0,48,56))
        self.game.platforms.append(Platform(208,136,48,72))
        self.game.platforms.append(Platform(256,136,32,16))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,256,56,32,80,3,"c"))

    def createroom5(self, entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room2.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(0,366)
        
        #Set Up Platforms
        self.game.platforms.append(Platform(0,152,48,72))
        self.game.platforms.append(Platform(48,168,48,56))
        self.game.platforms.append(Platform(96,184,64,40))
        self.game.platforms.append(Platform(160,168,48,56))
        self.game.platforms.append(Platform(208,152,48,72))
        self.game.platforms.append(Platform(224,88,32,64))
        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))
        self.game.platforms.append(Platform(0,0,48,88))
        
        #Set Up Items
        self.game.itemgroup.add(Item(46,109))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-32,88,32,64,3,"d"))

class RoomExit(Entity):
    def __init__(self, room, x, y, w, h, roomid, entrance):
        Entity.__init__(self)
        self.image = Surface((w*3, h*3))
        self.image.fill(Color("Blue"))
        self.rect = Rect(x*3, y*3, w*3, h*3)
        self.room = room
        self.roomid = roomid
        self.entrance = entrance
    def changeroom(self):
        if self.roomid == 1: self.room.createroom1(self.entrance)
        if self.roomid == 2: self.room.createroom2(self.entrance)
        if self.roomid == 3: self.room.createroom3(self.entrance)
        if self.roomid == 4: self.room.createroom4(self.entrance)
        if self.roomid == 5: self.room.createroom5(self.entrance)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Goomba(Entity):
    def __init__(self, x, y, xvel):
        Entity.__init__(self)
        #Set Velocities
        self.xvel = xvel
        self.yvel = 0
        #States
        self.onGround = False
        self.airborne = True
        self.destroyed = False
        #Offsets
        self.xoffset = -130
        self.yoffset = -30
        #Counter
        self.counter = 0
        #Create Sprite Image
        self.image = Surface((300, 450), pygame.SRCALPHA)
        self.image = goombaleft
        self.rect = Rect(x, y, 300, 450)
        #Create Detectable
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x, y, 64,64)
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):
        #Move
        if self.yvel < 0: self.airborne = True
        if self.onGround == True: self.airborne = False
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 1.2: self.airborne = True
            if self.yvel > 100: self.yvel = 100

        #Collisions
        self.detectable.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, projectilegroup)
        self.detectable.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel, platforms, projectilegroup)

        #Apply Offsets
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Platforms
        for p in platforms:
            if pygame.sprite.collide_rect(self.detectable, p):
                if xvel > 0:
                    self.detectable.rect.right = p.rect.left
                    self.xvel = -2
                if xvel < 0:
                    self.detectable.rect.left = p.rect.right
                    self.xvel = 2
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j):
                self.xvel = 0
                self.destroyed = True

    #Animate
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            self.walkloop(goombawalk)
    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10: self.updatecharacter(loop[0])
        elif self.counter == 20:
            self.updatecharacter(loop[1])
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0: self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 1
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf
        
class Toaster(Entity):
    def __init__(self, x, y, track, xvel):
        Entity.__init__(self)
        #Set Velocities
        self.xvel = xvel
        self.yvel = 0
        #States
        self.destroyed = False
        self.faceright = False
        self.onGround = False
        self.airborne = True
        #Offests
        self.xoffset = -130
        self.yoffset = 0
        #Counter
        self.counter = 0
        #Configure Track
        if xvel > 0:
            self.min = x
            self.max = x + track
        elif xvel < 0:
            self.max = x
            self.min = x - track
        #Create Sprite Image
        self.image = Surface((300, 450), pygame.SRCALPHA)
        self.image = toasterwalk1
        self.rect = Rect(x, y, 300, 450)
        #Create Dectectable
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x, y, 64,64)
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):
        #Move
        if self.xvel > 0: self.faceright = True
        if self.xvel < 0: self.faceright = False
        self.detectable.rect.left += self.xvel
        if self.detectable.rect.left == self.max: self.xvel = -abs(self.xvel)
        if self.detectable.rect.left == self.min: self.xvel = abs(self.xvel)
        self.detectable.rect.top += self.yvel

        #Collisions
        self.collide(0, self.yvel, platforms, projectilegroup)
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j):
                self.destroyed = True
                self.counter = 0
                self.xvel = 0

    #Animate          
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            self.walkloop(toasterwalkloop)
    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10:
            self.updatecharacter(loop[0])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[0], True, False))
        elif self.counter == 20:
            self.updatecharacter(loop[1])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[1], True, False))
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0:
            self.yoffset = -30
            self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 1
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf

class Item(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = itemframe1
        self.rect = Rect(x*3,y*3,78*3,59*3)
        self.counter = 0
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x*3, y*3, 64,64)
        self.detectable.rect.x = self.detectable.rect.x + 190
        self.detectable.rect.y = self.detectable.rect.y + 60
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
    def update(self):
        if self.counter == 0: self.image = itemloop[0]
        if self.counter == 10: self.image = itemloop[1]
        if self.counter == 20:
            self.image = itemloop[2]
            self.counter = 0
        self.counter = self.counter + 1

class PauseMenu(object):
    def __init__(self,game):
        self.game = game
    def createpausemenu(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Paused", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 290
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()

class LevelComplete(object):
    def __init__(self,game):
        self.game = game
    def createlevelcomplete(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Level Complete", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 200
        ss.rect.y = 400
        self.game.menugroup.add(ss)
        
class GameOver(object):
    def __init__(self,game):
        self.game = game
    def creategameover(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Game Over", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 240
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    
class Title(object):
    def __init__(self,game):
        self.game = game
        self.counter = 0
        self.createtitle()
    def createtitle(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()
        #Animate Title Screen
        if self.counter == 100:
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Starring", 1, (255, 255, 255))
            ss.rect = Rect(280,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = standleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 300:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Featuring", 1, (255, 255, 255))
            ss.rect = Rect(260,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = goombaleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 500:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Press Start", 1, (255, 255, 255))
            ss.rect = Rect(240,400,100,100)
            self.game.menugroup.add(ss)
        self.counter = self.counter + 1

class Display(Entity):
    def __init__(self, string):
        Entity.__init__(self)
        self.font = pygame.font.Font(None, 80)
        self.image = self.font.render(string, 1, (255, 0, 0))
    def update(self, string):
        self.image = self.font.render(string, 1, (255, 0, 0))

if __name__ == "__main__":
    main()
