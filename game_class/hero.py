import getch

KEY_CTRL_C = 3  # 終了: ctrl+C
KEY_W = 119     # 上: w
KEY_A = 97      # 左: a
KEY_S = 115     # 右: s
KEY_Z = 122     # 下: z
KEY_D = 100     # メッセージ取得

class Hero:
    def __init__(self, x, y, is_movable, get_message, draw_map):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.get_message = get_message
        self.draw_map = draw_map


    def talk(self):
        message = ''
        if self.icon == '^':
            message = self.get_message(self.x, self.y-1)
        if self.icon == '<':
            message = self.get_message(self.x-1, self.y)
        if self.icon == '>':
            message = self.get_message(self.x+1, self.y)
        if self.icon == 'V':
            message = self.get_message(self.x, self.y+1)
        return message


    def run(self):
        print('-----------------------')
        print('w:up, a:left, s:right, z:down')
        print('ctrl-c:quit')
        print('-----------------------')
        self.draw_map('')
        
        while True:
            message = ''

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
            elif key == KEY_D: 
                message = self.talk()
            else:
                continue
            
            self.draw_map(message)