
import pygame

import sys

from setting import Setting
from ship import Ship

from bullet import Bullet


class AlienInvasion:#(Alien入侵游戏)资源：创建窗口、监控键鼠行为
    
    def __init__(self):##初始化游戏并创建游戏资源
        
        pygame.init()##初始化游戏背景
        self.settings = Setting()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))##初始化窗口大小
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)##设为全屏
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
       
        pygame.display.set_caption("外星人大战")##窗口命名
       
        ##飞船
        self.ship = Ship(self)
        
        ##创建用于存储子弹的编组
        self.bullets = pygame.sprite.Group()
        
            
    def run_game(self):##开始游戏循环
        while True:##监控键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
        
           
    def _check_events(self):#辅助方法与事件管理类分离
        
        for event in pygame.event.get():##检测事件生成一个事件列表
            if event.type == pygame.QUIT:##pygame.QUIT表示玩家单击了游戏窗口的按钮
                sys.exit()##退出该程序   
        
             ##移动飞机
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            
            
    ##处理飞机移动                           
    def _check_keydown_events(self,event):##响应按键事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_front = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_back = True
        elif event.key == pygame.K_q:
            sys.exit()  
       ##发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self,event):##响应松键事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_front = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_back = False


    ##处理子弹发射
    def _fire_bullet(self): 
        ##创建前检查子弹数是否限制在10以内
        if len(self.bullets) < self.settings.bullets_allowed:
        ##创建一颗子弹，并将其加入编组bullets中    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)##每次循环重新绘制屏幕
        self.ship.blitme()##每次循环重新绘制飞船
         
       ##每次都绘制子弹到屏幕
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  
         
            
        pygame.display.flip()#在 pygame 库中，pygame.display.flip() 是一个非常重要的函数，
                            #它用于更新整个显示表面（或称为窗口）的内容。
            
            
    def _update_bullets(self):
        ##更新子弹
        ##更新位置
        self.bullets.update()
        
        ##删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        
        
        
        
        
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()