import pygame
import random

from pygame.locals import *

from constantes import *


pygame.init()
playing = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Proyecto Código Facilito")
screen.fill(background) #Definimos el color del fondo, usamos un color verde sobre el que dibujaremos otras superficies

pygame.display.update() #Actualizamos la página para que la pantalla dibuje los objetos definidos anteriormente
player_car = pygame.image.load("images/cary.png") #Cargamos la imagen del automovil
player_car_location = player_car.get_rect() #Definimos la ubicación como un rectángulo
player_car_location.center = carril_derecho, height*0.8 #Definimos la posición inicial en la que se encuentra nuestro auto

police_car = pygame.image.load("images/carp.png") #Cargamos la imagen del automovil enemigo
police_car_location = police_car.get_rect() #Definimos la ubicación como un rectángulo
police_car_location.center = carril_izquierdo, height*0.2 #Definimos la posición inicial en la que se encuentra nuestro auto

contador = 0
score_t = 0
clock = pygame.time.Clock()
global_score = score_t
play_crash_sound = True

font = pygame.font.SysFont('consolas', 50)
font_2 = pygame.font.SysFont('consolas', 25)
font_score = pygame.font.SysFont('Arial', 18)

def open_file():
    f = open("scores.txt.", "r")
    file = f.readlines()
    last = int(file[0])
        
    return last

bs = open_file()

def updateFile():
    f = open("scores.txt","r")
    file = f.readlines()
    last = int(file[0])
    
    if last < int(global_score):
        f.close()
        file = open("scores.txt", "w")
        file.write(str(global_score))
        file.close()
            
        return global_score
        
    return last

while playing: #Ciclo principal del juego
    bs_text = ("El mejor score es")
    best_score = font_score.render(bs_text, True, black)
    best_score_rect = best_score.get_rect()
    best_score_rect.center = (width*.9, height*.05)
    
    bs_num = (str(bs))
    bs_t = font_score.render(bs_num, True, black)
    bs_t_rect = bs_t.get_rect()
    bs_t_rect.center = (width*.9, height*.1)
    
    clock.tick(60)
    contador += 1

    if contador == 300:
        velocidad_enemigo += 1
        print("levelup")
        contador = 0

    police_car_location[1] += velocidad_enemigo #Definimos la posición del auto enemigo, usamos sólo un argumento entre corchetes indicando que sólo usaremos la altura para determinar su ubicación inicial y que el objeto se moverá a la velocidad definida

    if police_car_location[1] > height: #Ciclo para que el auto enemigo aparezca continuamente
        if random.randint(0,1) == 0:
            police_car_location.center = carril_derecho, -100
        else:
            police_car_location.center = carril_izquierdo, -100
        print(police_car_location.center)
        score_t += 1
        global_score = score_t
        print(score_t)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            player_car_location = player_car_location.move([-int(road/4), 0])

        if pressed[pygame.K_d]:
            player_car_location = player_car_location.move([int(road/4), 0])

        if player_car_location[0] < 166:
            player_car_location[0] = 166

        if player_car_location[0] > 352:
            player_car_location[0] = 352

    game_over =''
    
    if player_car_location.colliderect(police_car_location):
        print ("Colisión")
        if play_crash_sound:
            crash_sound = pygame.mixer.Sound('sounds/crash.wav')
            crash_sound.play()
            play_crash_sound = False
        velocidad_enemigo = 0
        
        
        if global_score > bs:
            game_over = "Lograste superar el score máximo!!"
        else:
            game_over = "No lograste superar el score máximo :("    
        
        updateFile()
        
    go_text = font_2.render(game_over, True, black)    
    go_text_rect = go_text.get_rect()
    go_text_rect.center = width//2,height//2
    
    #if player_car_location[0] == police_car_location[0] and police_car_location[1] > player_car_location[1] - 250: # Determina la colisión de los autos
     #   print("GAME OVER")
    
    screen.fill(background)

    pygame.draw.rect(screen, (100,100,100),(width/2 - road/2,0,road,height))
    pygame.draw.rect(screen, (255,240,60),(width/2 - y_line/2,0,y_line,height))
    pygame.draw.rect(screen, (255,255,255),(width/2 - road/2 + y_line*2,0,y_line,height))
    pygame.draw.rect(screen, (255,255,255),(width/2 + road/2 - y_line*3,0,y_line,height))
    
    screen.blit(player_car, player_car_location)
    screen.blit(police_car, police_car_location)

    t_score = font.render(str(score_t), True, black)
    t_score_rect = t_score.get_rect()
    t_score_rect.center = (width*.1, height*.1)
           
    screen.blit(t_score, t_score_rect)
    
    screen.blit(go_text, go_text_rect)    
    
    screen.blit(best_score, best_score_rect)
    
    screen.blit(bs_t, bs_t_rect)
    
    pygame.display.update()

pygame.quit()
