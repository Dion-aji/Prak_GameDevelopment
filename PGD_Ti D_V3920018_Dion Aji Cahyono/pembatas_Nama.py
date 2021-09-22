from pygame.locals import * 
import time 
import pygame, sys  
from pygame import rect  
WIDTH, HEIGHT = 500, 500  # mengatur Ukuran Display lebar dan tinggi
pygame.display.set_caption('Smooth Movement')  # Title atau Nama di app bar display

pygame.init()  #  submodules di pygame
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Menampilkan lebar display yang sudah di atur Widht height
clock = pygame.time.Clock() 

#Membuat Warna RGB,akan di pakai untuk menentukan warna yang di inginkan 
hitam_Kebiruan = (12,24,36)
putih = (255, 255, 255)
# membuat sebuah class bernama player
class Player:
    def __init__(self, x, y):  # membuat fungsi constructor dengan memasukan objek self dan parameter x,y
        self.x = int(x)  # pada self x memberi variable integer nilai x
        self.y = int(y)  # pada self y memberi integer niali y
        self.rect = pygame.Rect(self.x, self.y, 40, 40)  # mengatur  ukuran kotak lebar 40 tinggi 40
        self.color = (putih)  # memberikan warna putih pada kotak
        self.velX = 0  #  kecepatan awal x sebesar 0
        self.velY = 0  # kecepatan awal y sebesar 0
        self.left_pressed = False #awal di tekan key kiri akan bernilai false
        self.right_pressed = False  #awal di tekan key kanan akan bernilai false
        self.up_pressed = False #awal di tekan key atas akan bernilai false
        self.down_pressed = False  #awal di tekan key bawah akan bernilai false
        self.speed = 6  # menentukan kecepatan objectnya,nilai awal 4 saya ganti 6 supaya semakin cepat
# membuat def draw
    def draw(self,win): 
        pygame.draw.rect(win, self.color, self.rect)

    def update(
            self):  # fungsi update dari objek self di atas.
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed and self.x > 0 :#pembatas kiri di mulai dari 0
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed and self.x < 460 :# Di Gunakan untuk mengatur pembatas kanan 
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed and self.y > 0 :#pembatas atas di mulai dari 0
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed and self.y < 460 :# Di Gunakan untuk mengatur pembatas bawah
            self.velY = self.speed
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 40, 40)
player = Player(WIDTH / 2, HEIGHT / 2)

# kemudian menentukan font dan teks, untuk menampilkan nama di display
font_color = (hitam_Kebiruan)#menentukan Warna ,yang di mengambil dari variable warna Hitam
font_obj = pygame.font.Font("C:\Font\GermanaNoia.ttf", 50)#untuk mengubah style Font,
text = "Dion Aji Cahyono"#Menampilkan Teks pada display
new_text= font_obj.render(text, True, (putih))#warna teks

rect = new_text.get_rect()
rect.center = (250, 100) # Untuk Mengatur letak Posisi teks 
cursor = Rect(rect.topright, (3, rect.height))
while True:  # akan menjalankan jika perulangannya True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    new_text = font_obj.render(text, True, )
                    rect.size = new_text.get_size()
                    cursor.topleft = rect.topright

    # memberikan warna pada backgroud
    win.fill((hitam_Kebiruan))#mengatur warna Ke hitam
    pygame.draw.rect(win, (putih), player)#Mengatur warna display ke putih

    win.blit(new_text, rect)
    player.update() #mengeupdate dari klass display
    pygame.display.flip()#mengembalikan display

    clock.tick(190)#Untuk mengatur Frame,jika semakin Tiggi Frame maka akan semakin Smooth
    pygame.display.update()
