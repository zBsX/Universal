import pygame

class Object: # basic physics
    def __init__(self, game, width_and_height=(0, 0), damping=0, stiffness=0, friction_coefficient=0, position=(0, 0), static_position=(0, 0), velocity=(0, 0), acceleration=(0, 0), edge_frame=None) -> None:
        self.game = game
        self.friction = friction_coefficient
        self.width_and_height = width_and_height
        self.edge_frame = edge_frame
        self.static_pos = static_position
        self.pos = list(position)       #
        self.vel = list(velocity)       # !ALL OF THESE ARE VECTORS!
        self.accel = list(acceleration) #
        self.holding = False
        self.stiffness = stiffness
        self.damping = damping

    def update(self):
        if not self.holding:
            self.accel[0] = self.stiffness * (self.static_pos[0] - self.pos[0])
            self.accel[1] = self.stiffness * (self.static_pos[1] - self.pos[1])
            self.vel[1] *= self.damping
            self.vel[0] *= self.damping
        else:
            if abs(self.vel[1]) > 0.5:
                self.accel[1] = round(-self.friction * self.vel[1], 4)
            elif 0 < abs(self.vel[1]) < 0.5 and not self.holding:
                self.accel[1] = 0
                self.vel[1] = 0
            if abs(self.vel[0]) > 0.5:
                self.accel[0] = round( -self.friction * self.vel[0], 4)
            elif 0 < abs(self.vel[0]) < 0.5 and not self.holding:
                self.accel[0] = 0
                self.vel[0] = 0

        self.vel[1] += self.accel[1]
        self.vel[0] += self.accel[0]
        # self.vel[1] = round(min(24, self.vel[1]), 4)
        # self.vel[1] = round(max(-24, self.vel[1]), 4)
        # self.vel[0] = round(min(24, self.vel[0]), 4)
        # self.vel[0] = round(max(-24, self.vel[0]), 4)

        self.pos[1] += int(self.vel[1])
        self.pos[0] += int(self.vel[0])

        if 0 < abs(self.vel[0]) < 0.3:
            self.vel[0] = 0
        if 0 < abs(self.vel[1]) < 0.3:
            self.vel[1] = 0


    def render(self, surf, asset):
        surf.blit(asset, tuple(self.pos))
    
class RectFrame(Object):
    def __init__(self, game, width_and_height=(0, 0), friction_coefficient=0, position=(0, 0), velocity=(0, 0), acceleration=(0, 0), edge_frame=None) -> None:
        super().__init__(game, width_and_height, friction_coefficient, position, velocity, acceleration, edge_frame)

    def rect(self, offset=(0, 0)):
        return pygame.Rect(self.pos[0] - offset[0], self.pos[1] - offset[1], self.width_and_height[0], self.width_and_height[1])
    
class ObjectSurface(Object):
    def __init__(self, game, width_and_height=(0, 0), friction_coefficient=0, position=(0, 0), velocity=(0, 0), acceleration=(0, 0), edge_frame=None) -> None:
        super().__init__(game, width_and_height, friction_coefficient, position, velocity, acceleration, edge_frame)

    def surface(self, offset=(0, 0)):
        return pygame.Surface(self.width_and_height)