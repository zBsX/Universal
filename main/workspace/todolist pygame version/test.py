#  match (self.pos[1] < self.game.rect_frame.y, 
#                self.pos[0] < self.game.rect_frame.x, 
#                self.pos[1] > (self.game.rect_frame.bottom - self.width_and_height[1]),
#                self.pos[0] > (self.game.rect_frame.right - self.width_and_height[0]),
#                self.game.check_holding,
#                self.counter[0] < 12,
#                self.counter[1] < 12):
#             case (True, _, _, _, False, _, True):
#                 self.vel[1] += 1
#                 self.counter[1] += 1
#             case (_, True, _, _, False, True, _):
#                 self.vel[0] += 1
#                 self.counter[0] += 1
#             case (_, _, True, _, False, _, True):
#                 self.vel[1] -= 1
#                 self.counter[1] += 1
#             case (_, _, _, True, False, True, _):
#                 self.vel[0] -= 1
#                 self.counter[0] += 1
#             case _:
#                 self.counter = [0, 0]


# if self.pos[1] < self.game.rect_frame.y and not self.game.check_holding: # fix the speed resource-costing issue
        #     self.vel[1] += 1
        #     self.counter[1] += 1
        # if  self.pos[0] < self.game.rect_frame.x and not self.game.check_holding:
        #     self.counter[0] += 1
        #     self.vel[0] += 2
        # if self.pos[1] > (self.game.rect_frame.bottom - self.width_and_height[1]) and not self.game.check_holding:
        #     self.counter[1] += 1
        #     self.vel[1] -= 1
        # if self.pos[0] > (self.game.rect_frame.right - self.width_and_height[0]) and not self.game.check_holding:
        #     self.vel[0] -= 2
        #     self.counter[0] += 1


# match (self.pos[1] < self.game.rect_frame.y or self.pos[1] > (self.game.rect_frame.bottom - self.width_and_height[1]), 
#                self.pos[0] < self.game.rect_frame.x or self.pos[0] > (self.game.rect_frame.right - self.width_and_height[0]),
#                self.game.check_holding,
#                self.counter[1] < 12,
#                self.counter[0] < 12):
#             case (True, _, False, True, _):
#                 print("y")
#                 if self.pos[1] < self.game.rect_frame.y:
#                     self.vel[1] += 1
#                     self.counter[1] += 1
#                 elif self.pos[1] > (self.game.rect_frame.bottom - self.width_and_height[1]):
#                     self.vel[1] -= 1
#                     self.counter[1] += 1
#             case (_, True, False, _, True):
#                 print("x")
#                 if self.pos[0] < self.game.rect_frame.x:
#                     self.vel[0] += 1
#                     self.counter[0] += 1
#                 elif self.pos[0] > (self.game.rect_frame.right - self.width_and_height[0]):
#                     self.vel[0] -= 1
#                     self.counter[0] += 1
#             case _:
#                 self.counter = [0, 0]


# self.button_object_frame.pos[0] = event.pos[0] * 2 - self.button_object_frame.width_and_height[0] / 2
# self.button_object_frame.pos[1] = event.pos[1] * 2 - self.button_object_frame.width_and_height[1] / 2

import pygame
import math

# 初始化 Pygame
pygame.init()

# 设置屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spring Animation")

# 定义一些参数
pos = [300, 300]
target_pos = [300, 300]
velocity = [0, 0]
damping = 0.9
stiffness = 0.1

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                velocity[0] = event.rel[0] * 2
                velocity[1] = event.rel[1] * 2

    # 弹簧力计算
    force_x = stiffness * (target_pos[0] - pos[0])
    force_y = stiffness * (target_pos[1] - pos[1])
    
    velocity[0] += force_x
    velocity[1] += force_y
    
    # 阻尼力
    velocity[0] *= damping
    velocity[1] *= damping
    
    # 更新位置
    pos[0] += int(velocity[0])
    pos[1] += int(velocity[1])
    print(int(velocity[0]), int(velocity[1]))

    # 绘制
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (int(pos[0]), int(pos[1])), 20)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


# IO Backup
                # if event.type == KEYDOWN:
                #     if event.key == K_LEFT:
                #         self.scroll_frame.vel[0] -= 12
                #     elif event.key == K_RIGHT:
                #         self.scroll_frame.vel[0] += 12

                # if event.type == MOUSEBUTTONDOWN:
                #     if event.button == 1:
                #         self.scroll_frame.holding = True
                #         self.button_object_frame.holding = True
                #     if event.button == 4:
                #         self.scroll_frame.vel[1] += 12
                #     elif event.button == 5:
                #         self.scroll_frame.vel[1] -= 12
                # elif event.type == MOUSEBUTTONUP:
                #     if event.button == 1:
                #         self.scroll_frame.holding = False
                #         self.button_object_frame.holding = False

                # if event.type == MOUSEMOTION:
                #     if (self.scroll_frame.pos[0] + self.scroll_frame.width_and_height[0]) > event.pos[0]*2 > self.scroll_frame.pos[0] and (self.scroll_frame.pos[1] + self.scroll_frame.width_and_height[1]) > event.pos[1]*2 > self.scroll_frame.pos[1]:
                #         if event.buttons[0]:
                #             self.scroll_frame.holding = True
                #             # self.scroll_frame.accel[0] = event.rel[0] / 6
                #             # self.scroll_frame.accel[1] = event.rel[1] / 6
                #             # self.scroll_frame.vel[0] += self.scroll_frame.accel[0]
                #             # self.scroll_frame.vel[1] += self.scroll_frame.accel[1]
                #         elif not event.buttons[0]:
                #             self.scroll_frame.holding = False
                #     elif not event.buttons[0]:
                #         self.scroll_frame.holding = False
                #     if (self.button_object_frame.pos[0] + self.button_object_frame.width_and_height[0]) > event.pos[0]*2 > self.button_object_frame.pos[0] and (self.button_object_frame.pos[1] + self.button_object_frame.width_and_height[1]) > event.pos[1]*2 > self.button_object_frame.pos[1]:
                #         if event.buttons[0]:
                #             self.button_object_frame.holding = True
                #             self.button_object_frame.accel[0] = event.rel[0] / 6
                #             self.button_object_frame.accel[1] = event.rel[1] / 6
                #             self.button_object_frame.vel[0] += self.button_object_frame.accel[0]
                #             self.button_object_frame.vel[1] += self.button_object_frame.accel[1]
                #         elif not event.buttons[0]:
                #             self.scroll_frame.holding = False



# smooth friction animation

# if abs(self.vel[1]) > 0.5:
        #     self.accel[1] = round(-self.friction * self.vel[1], 4) # f_s = -friction * u
        # elif 0 < abs(self.vel[1]) < 0.5 and not self.holding:
        #     self.accel[1] = 0
        #     self.vel[1] = 0
        # if abs(self.vel[0]) > 0.5:
        #     self.accel[0] = round( -self.friction * self.vel[0], 4)
        # elif 0 < abs(self.vel[0]) < 0.5 and not self.holding:
        #     self.accel[0] = 0
        #     self.vel[0] = 0 