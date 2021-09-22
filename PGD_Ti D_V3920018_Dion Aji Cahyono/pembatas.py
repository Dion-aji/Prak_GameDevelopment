  # Nama  : Dion Aji Cahyono
  # Nim   : V3920018
  # Kelas : Ti D

  #Urutan = E,D,F,A,B,C
   #-----------------------------------------------------------------
   #Part E
import pygame,sys

from pygame import font

WIDTH , HEIGHT = 500,500# mengatur Ukuran Display lebar dan tinggi
TITLE = "smooth Movement"# Title atau Nama di app bar display

pygame.init()#  submodules di pygame
win = pygame.display.set_mode((WIDTH,HEIGHT)) # Menampilkan lebar display yang sudah di atur Widht height
pygame.display.set_caption(TITLE)
clock =pygame.time.Clock()
#---------------------------------------------------------------------------
# membuat sebuah class bernama player
   #Part D
class Player :
    def __init__(self, x,y): # membuat fungsi constructor dengan memasukan objek self dan parameter x,y
        self.x = int(x) # pada self x memberi variable integer nilai x
        self.y = int(y) # pada self y memberi integer niali y
        self.rect = pygame.Rect(self.x,self.y,32,32)  # mengatur  ukuran kotak lebar 40 tinggi 40
        self.color = (255,255,255) # memberikan warna putih pada kotak
        self.velx = 0 #  kecepatan awal x sebesar 0
        self.vely = 0  # kecepatan awal y sebesar 0
        self.left_pressed = False #awal di tekan key kiri akan bernilai false
        self.right_pressed = False  #awal di tekan key kanan akan bernilai false
        self.up_pressed = False #awal di tekan key atas akan bernilai false
        self.down_pressed = False #awal di tekan key bawah akan bernilai false
        self.speed = 6  # menentukan kecepatan objectnya,nilai awal 4 saya ganti 6 supaya semakin cepat
#----------------------------------------------------------------------------
        #Part F
    def draw(self,win):
        pygame.draw.rect(win, self.color,self.rect) 
#--------------------------------------------------------------------------
        #Part A
    def update (self):  # fungsi update dari objek self di atas.
        self.velx = 0 
        self.vely = 0 
        if self.left_pressed and not self.right_pressed and self.x > 0:#pembatas kiri di mulai dari 0
            self.velx = -self.speed 
        if self.right_pressed and not self.left_pressed and self.x < 460:# Di Gunakan untuk mengatur pembatas kanan 
            self.velx = self.speed
        if self.up_pressed and not self.down_pressed and self.y > 0:#pembatas atas di mulai dari 0
            self.vely = -self.speed
        if self.down_pressed and not self.up_pressed and self.y < 460:# Di Gunakan untuk mengatur pembatas bawah
            self.vely = self.speed
        self.x += self.velx
        self.y += self.vely
        self.rect = pygame.Rect(int(self.x),int(self.y),40,40)
#--------------------------------------------------------------
        #Part B
player = Player (WIDTH/2,HEIGHT/2)
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed=True
            if event.key == pygame.K_RIGHT:
                player.right_pressed=True
            if event.key == pygame.K_UP:
                player.up_pressed=True
            if event.key == pygame.K_DOWN:
                player.down_pressed=True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed=False
            if event.key == pygame.K_RIGHT:
                player.right_pressed=False
            if event.key == pygame.K_UP:
                player.up_pressed=False
            if event.key == pygame.K_DOWN:
                player.down_pressed=False
#-------------------------------------------------------------------
      #part C
    win.fill ((12,24,36))#untuk mengatur warna display 
    player.draw (win)
    player.update() #mengaupdate dari class player
    pygame.display.flip()#mengembalikan display
    clock.tick (120)#Untuk mengatur Frame,jika semakin Tiggi Frame maka akan semakin Smooth