import pygame
import time

TALKING = False

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile (self, filename, id=None):
        if id == None: id = filename
        self.pics[id] = pygame.image.load (filename).convert()

    def loadFromSurface (self, surface, id):
        self.pics[id] = surface.convert_alpha()

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
pygame.display.set_caption("A.A.R.O.N")
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)
handler = imageHandler()

def display():

# Idle Animation
    handler.loadFromFile("D://Jarvis/venv/face2/idle/1.jpg", "1")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/2.jpg", "2")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/3.jpg", "3")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/4.jpg", "4")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/5.jpg", "5")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/6.jpg", "6")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/7.jpg", "7")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/8.jpg", "8")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/9.jpg", "9")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/10.jpg", "10")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/11.jpg", "11")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/12.jpg", "12")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/13.jpg", "13")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/14.jpg", "14")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/15.jpg", "15")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/16.jpg", "16")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/17.jpg", "17")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/18.jpg", "18")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/19.jpg", "19")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/20.jpg", "20")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/21.jpg", "21")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/22.jpg", "22")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/23.jpg", "23")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/24.jpg", "24")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/25.jpg", "25")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/26.jpg", "26")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/27.jpg", "27")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/28.jpg", "28")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/29.jpg", "29")

    # Talking Animation
    handler.loadFromFile("D://Jarvis/venv/face2/talking/101.jpg", "101")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/102.jpg", "102")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/103.jpg", "103")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/104.jpg", "104")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/105.jpg", "105")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/106.jpg", "106")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/107.jpg", "107")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/108.jpg", "108")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/109.jpg", "109")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/110.jpg", "110")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/111.jpg", "111")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/112.jpg", "112")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/113.jpg", "113")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/114.jpg", "114")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/115.jpg", "115")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/116.jpg", "116")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/117.jpg", "117")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/118.jpg", "118")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/119.jpg", "119")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/120.jpg", "120")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/121.jpg", "121")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/122.jpg", "122")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/123.jpg", "123")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/124.jpg", "124")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/125.jpg", "125")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/126.jpg", "126")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/127.jpg", "127")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/128.jpg", "128")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/129.jpg", "129")


display()

def face():
    # Variables#
    A = 0  # Left and Right on Screen
    B = 0  # Up and Down on Screen
    x = 400  # Size width
    y = 400  # Size Length

    Count = 1
    global TALKING
    while True:
        if TALKING == False:
            if Count >= 100:
                Count = Count - 100
            print(Count)
            img = str(Count)
            handler.render(screen,img,(A,B),True,(x,y))
            pygame.display.update(A,B,x,y)
            time.sleep(.08)
            Count = Count +1
            if Count == 30:
                Count = 1

            elif TALKING == True:
                if Count <=100:
                    Count = Count + 100
                print(Count)
                img = str(Count)
                handler.render(screen, img, (A, B), True, (x, y))
                pygame.display.update(A, B, x, y)
                time.sleep(.08)
                Count = Count + 1
                if Count == 130:
                    Count = 101


face()