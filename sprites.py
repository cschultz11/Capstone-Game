import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert_alpha()
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        #self.animation_loop = 1
        
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    #Updates player and animations
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0
        
    #Sets movement as well as "camera"
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
    
    #Defines collision with blocks and prevents camera from moving past the boundaries
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
                    
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom

    #TODO: Add more 3 more animations (frames) for each direction of movement, then update array vars               
    def animate(self):
        #down_animations = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), self.game.character_spritesheet.get_sprite(0,0, self.width, self.height)]
        #up_animations = [self.game.character_spritesheet.get_sprite(32,0,self.width,self.height), self.game.character_spritesheet.get_sprite(32,0,self.width,self.height), self.game.character_spritesheet.get_sprite(32,0,self.width,self.height)]
        #right_animations = [self.game.character_spritesheet.get_sprite(64,0, self.width, self.height), self.game.character_spritesheet.get_sprite(64,0, self.width, self.height), self.game.character_spritesheet.get_sprite(64,0, self.width, self.height)]
        #left_animations = [self.game.character_spritesheet.get_sprite(96,0, self.width, self.height), self.game.character_spritesheet.get_sprite(96,0, self.width, self.height), self.game.character_spritesheet.get_sprite(96,0, self.width, self.height)]
        
        #DOWN ANIMATION
        if self.facing == "down":
                self.image = self.game.character_spritesheet.get_sprite(0,0,self.width,self.height)
                
        #if self.facing == "down":
        #    if self.y_change == 0:
        #        self.image = self.game.character_spritesheet.get_sprite(0,0,self.width,self.height)
        #else:
        #    self.image = down_animations[0]
        #    self.image = down_animations[math.floor(self.animation_loop)]
        #    self.animation_loop += 0.1
        #    if self.animation_loop >= 3:
        #        self.animation = 1
        
        #UP ANIMATION
        if self.facing == "up":
                self.image = self.game.character_spritesheet.get_sprite(32,0,self.width,self.height)
                
        #if self.facing == "up":
        #    if self.y_change == 0:
        #        self.image = self.game.character_spritesheet.get_sprite(32,0,self.width,self.height)
        #else:
        #    self.image = up_animations[0]
        #    self.image = up_animations[math.floor(self.animation_loop)]
        #    self.animation_loop += 0.1
        #    if self.animation_loop >= 3:
        #        self.animation = 1
            
        #RIGHT ANIMATION
        if self.facing == "right":
                self.image = self.game.character_spritesheet.get_sprite(64,0,self.width,self.height)
                
        #if self.facing == "right":
        #    if self.y_change == 0:
        #        self.image = self.game.character_spritesheet.get_sprite(64,0,self.width,self.height)
        #else:
        #    self.image = right_animations[0]
        #    self.image = right_animations[math.floor(self.animation_loop)]
        #    self.animation_loop += 0.1
        #    if self.animation_loop >= 3:
        #       self.animation = 1
        
        #LEFT ANIMATION
        if self.facing == "left":
                self.image = self.game.character_spritesheet.get_sprite(96,0,self.width,self.height)
                
        #if self.facing == "left":
        #    if self.y_change == 0:
        #        self.image = self.game.character_spritesheet.get_sprite(96,0,self.width,self.height)
        #else:
        #    self.image = left_animations[0]
        #    self.image = left_animations[math.floor(self.animation_loop)]
        #    self.animation_loop += 0.1
        #    if self.animation_loop >= 3:
        #        self.animation = 1
            
            
class TopFence(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class BottomFence(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(32,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class BottomFenceTopper(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(64,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(96, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
