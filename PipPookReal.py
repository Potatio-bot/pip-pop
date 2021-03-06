from pygame import *

win_widg = 800
win_hight = 500
speedY = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x  = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateAwos(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hight - 170:
           self.rect.y += self.speed
    
    def updateWS(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight - 170:
            self.rect.y += self.speed

class Drifter(GameSprite):
    def drift(self):
        global speedY
        global run
        self.rect.x += self.speed
        self.rect.y += speedY

        if sprite.collide_rect(boll, blok_1):
            self.speed = -self.speed
            delta = boll.rect.y - blok_1.rect.y
            speedY += delta//10

        if sprite.collide_rect(boll, blok_2):
            self.speed = -self.speed
            delta = boll.rect.y - blok_2.rect.y
            speedY += delta//10

        if (self.rect.x < -10) or (self.rect.x > win_widg + 10): 
            run = False

        if (self.rect.y < 0) or (self.rect.y > win_hight - 40):
            speedY = -speedY

win = display.set_mode((win_widg, win_hight))
display.set_caption('Pin pong')

fon = (200, 255, 255)
griz = 'blok_grize.png'
kamen = 'kamen.png'
mizh = 'owal.png'

blok_1 = Player(griz, win_widg-90, win_hight//2 - 75 ,40 ,150 ,15)
blok_2 = Player(kamen, 50, win_hight//2 - 75 ,40 ,150 ,15)
boll = Drifter(mizh, win_widg//2 - 25, win_hight//2 - 25 ,50 ,50 ,10)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    win.fill(fon)
    # draw.rect(win, (0,0,255), (x, y, width, hight))
    blok_1.reset()
    blok_1.updateAwos()

    blok_2.reset()
    blok_2.updateWS()

    boll.reset()
    boll.drift()

    display.update()
    time.delay(50)