from typing import Any
import pygame 
from pygame.sprite import Sprite

##管理飞船的子弹类
class Bullet(Sprite):
    
    def __init__(self,ai_game):
        ##在飞船当前位置创建一个子弹对象
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        ##在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.midtop
        
        ##存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    
    def update(self): ##向上移动子弹
       self.y -= self.settings.bullet_speed
       ##更新表示子弹的位置的小数值
       self.rect.y = self.y
       
       
    def draw_bullet(self):##屏幕上绘制子弹
        ##pygame.draw 是 Pygame 库中的一个模块，它提供了一些函数来绘制简单的形状（如线条、矩形、圆形等）到 Surface 对象上。
        # Surface 对象可以看作是一个图像或者画布，你可以在其上绘制各种图形。
   
        #pygame.draw.rect(Surface, color, Rect, width=0)
        #参数说明：
        #Surface：需要绘制矩形的 Surface 对象。
        #color：一个 RGB 颜色值，例如 (255, 0, 0) 表示红色。也可以是一个 RGBA 颜色值，包含透明度信息。
        #Rect：一个 pygame.Rect 对象，定义了矩形的位置和大小。这个对象可以通过 pygame.Rect(x, y, width, height) 来创建，其中 (x, y) 是矩形左上角的坐标，width 和 height 是矩形的宽度和高度。
        #width（可选）：矩形边框的宽度。默认为 0，表示绘制一个填充的矩形。如果 width 大于 0，则绘制一个边框，内部不填充。"""

        pygame.draw.rect(self.screen,self.color,self.rect)