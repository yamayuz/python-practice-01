import getch

KEY_CTRL_C = 3  # 終了: ctrl+C
KEY_W = 119     # 上: w
KEY_A = 97      # 左: a
KEY_S = 115     # 右: s
KEY_Z = 122     # 下: z

class Hero:
    def __init__(self, x, y, is_movable, draw_map):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.draw_map = draw_map

    def run(self):
        print('-----------------------')
        print('w:up, a:left, s:right, z:down')
        print('ctrl-c:quit')
        print('-----------------------')
        self.draw_map()
        
        while True:
            key = ord(getch.getch())
            if key == KEY_CTRL_C: # Quit
                print('bye!!')
                break
            elif key == KEY_W: # Up
                self.icon = '^'
                if self.is_movable(self.x, self.y-1): self.y -= 1
            elif key == KEY_A: # Left
                self.icon = '<'
                if self.is_movable(self.x-1, self.y): self.x -= 1
            elif key == KEY_S: # Right
                self.icon = '>'
                if self.is_movable(self.x+1, self.y): self.x += 1
            elif key == KEY_Z: # Down
                self.icon = 'V'
                if self.is_movable(self.x, self.y+1): self.y += 1
            else:
                continue
            
            self.draw_map()