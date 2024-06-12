import pygame

class Ship:##管理飞船类
    
    def __init__(self,ai_game):
        ##初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()##获取屏幕位置
       
        
        ##加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('C:\\Users\\wwc\\Desktop\\py\\素材库\\飞船.bmp')
        # 改变图片大小，例如缩小到 100x100  
        self.image = pygame.transform.scale(self.image, (75, 75))  
        self.rect = self.image.get_rect()
        
        ##对于新每艘飞船，都将其放在屏幕底部的中央位置
        self.rect.midbottom = self.screen_rect.midbottom
        
        ##在飞船的属性中存储小数值
        self.x  =float(self.rect.x)
        self.y = float(self.rect.y)
        
        
        ##移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_front = False
        self.moving_back = False
        
        
        
    def update(self):
            
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        if self.moving_front and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed 
        if self.moving_back and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        ##在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)