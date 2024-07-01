import pygame
import sys
from pygame.locals import *
from data.engine import Object, RectFrame, ObjectSurface

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((1000,1000))
        self.assets = {
            "button": pygame.image.load("data/img/botton.png")
        }
        self.button1 = Object(self, width_and_height=(500, 250), friction_coefficient=0.05, stiffness=0.1, damping=0.9, static_position=(100, 50))
        self.button2 = Object(self, width_and_height=(500, 250), friction_coefficient=0.05, stiffness=0.2, damping=0.9, static_position=(100, 400))
        self.button3 = Object(self, width_and_height=(500, 250), friction_coefficient=0.05, stiffness=0.2, damping=0.9, static_position=(100, 700))

    def run(self):
        while True:
            self.display.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN: 
                    if (self.button1.pos[1] < event.pos[1] * 2 < self.button1.pos[1] + self.button1.width_and_height[1]):
                        self.button1.holding = True
                    elif (self.button2.pos[1] < event.pos[1] * 2 < self.button2.pos[1] + self.button2.width_and_height[1]):
                        self.button2.holding = True
                    elif (self.button3.pos[1] < event.pos[1] * 2 < self.button3.pos[1] + self.button3.width_and_height[1]):
                        self.button3.holding = True
                    print("true")
                elif event.type == MOUSEBUTTONUP:
                    self.button1.holding = False
                    self.button2.holding = False
                    self.button3.holding = False
                    print("false")

                if event.type == MOUSEMOTION:
                    if event.buttons[0]:
                        if (self.button1.pos[1] < event.pos[1] * 2 < self.button1.pos[1] + self.button1.width_and_height[1]) or self.button1.holding:
                            self.button1.vel[0] += event.rel[0] / 6
                            self.button1.vel[1] += event.rel[1] / 6
                        elif (self.button2.pos[1] < event.pos[1] * 2 < self.button2.pos[1] + self.button2.width_and_height[1]) or self.button2.holding:
                            self.button2.vel[0] += event.rel[0] / 6
                            self.button2.vel[1] += event.rel[1] / 6
                        elif (self.button3.pos[1] < event.pos[1] * 2 < self.button3.pos[1] + self.button3.width_and_height[1]) or self.button3.holding:
                            self.button3.vel[0] += event.rel[0] / 6
                            self.button3.vel[1] += event.rel[1] / 6
                    else:
                        self.button1.holding = False
                        self.button2.holding = False
                        self.button3.holding = False

            self.button1.update()
            self.button1.render(self.display, self.assets["button"])
            self.button2.update()
            self.button2.render(self.display, self.assets["button"])
            self.button3.update()
            self.button3.render(self.display, self.assets["button"])
            print(self.button3.vel)

            self.screen.blit(pygame.transform.scale(self.display, (500, 500)), (0, 0))
            pygame.display.update()
            self.clock.tick(90)

Game().run()