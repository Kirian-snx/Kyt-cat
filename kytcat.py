import pygame
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((1600, 900), RESIZABLE)
pygame.display.set_caption("KYTCAT")

background = pygame.image.load("back_kitcat.png").convert()
win.blit(background, (0, 0))

perso = pygame.image.load("want_u.png").convert_alpha()
pos_perso = perso.get_rect()
win.blit(perso, pos_perso)

son = pygame.mixer.Sound("sega.ogg")

pygame.display.flip()
pygame.key.set_repeat(400, 30)
run = 1
while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			run = 0
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				run = 0
			if event.key == K_SPACE:
				son.play()
			if event.key == K_DOWN:
				pos_perso = pos_perso.move(0, 5)
			if event.key == K_UP:
				pos_perso = pos_perso.move(0, -5)
			if event.key == K_LEFT:
				pos_perso = pos_perso.move(-5, 0)
			if event.key == K_RIGHT:
				pos_perso = pos_perso.move(5, 0)
	win.blit(background, (0, 0))
	win.blit(perso, pos_perso)
	pygame.display.flip()