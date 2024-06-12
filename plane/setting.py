class Setting:##存放游戏设置：背景、窗口大小
    
    def __init__(self):
        self.screen_width = 400 ##窗口宽为1200
        self.screen_height = 650 ##窗口高为800
        self.bg_color = (135,206,235) ##窗口背景色为三色RGB（）
        
     ##飞船速度设置
        self.ship_speed = 1.5