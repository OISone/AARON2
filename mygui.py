import pygame
import numpy
import time

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile (self, filename, id=None):
        if id == None: id = filename
        self.pics [id] = pygame.image.load (filename).convert()

    def loadFromSurface (self, surface, id):
        self.pics [id] = surface.convert_alpha()

    def render (self, surface, id, position = None, clear = False, size = None):
        if clear == True:
            surface.fill ( (5,2,23))

        if position == None:
            picX = int (surface.get_width()/2-self.pics[id].get_width()/2)
        else:
            picX = position[0]
            picY = position[1]

        if size == None:
            surface.blit (self.pics [id],(picX,picY))

        else:
            surface.blit (pygame.transform.smoothscale (self.pics [id],size),(picX,picY))

pygame.display.init()
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)
handler = imageHandler()

def display():

    #setup base animation
    basic_face = ['D:/jarvis/venv/face/frame_00_delay-0.08s.jpg','D:/jarvis/venv/face/frame_01_delay-0.08s.jpg']

    length = len(basic_face)
    for x in range(length):
        handler.loadFromFile(basic_face[x], x)#

display()

def face():
    #Variables#
    A = 0
    B = 0
    x = 400
    y = 400
    delay = 0.1

    handler.render (screen, "1", (A,B),True, (x,y))
    pygame.display.update(A,B,x,y)
    time.sleep(delay)
    handler.render (screen, "2", (A,B),True, (x,y))
    pygame.display.update(A,B,x,y)
    time.sleep(.2)
    handler.render(screen, "3", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "4", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "5", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "6", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "7", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "8", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "9", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
    handler.render(screen, "10", (A, B), True, (x, y))
    pygame.display.update(A, B, x, y)
    time.sleep(.2)
face()