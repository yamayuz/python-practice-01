import getch
from game_class.hero import *

KEY_CTRL_C = 3  # 終了: ctrl+C
KEY_W = 119     # 上: w
KEY_A = 97      # 左: a
KEY_S = 115     # 右: s
KEY_Z = 122     # 下: z

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hero = Hero(3, 3, self.is_movable, self.draw)

    def run(self):
        self.hero.run()

    def is_movable(self, x, y):
        if x < 0:
            return False
        elif self.width-1 < x:
            return False
        elif y < 0:
            return False
        elif self.height-1 < y:
            return False
        return True

    def draw(self):
        characters = {}
        characters[(self.hero.x, self.hero.y)] = self.hero.icon

        def get_row(y):
            row_list = []
            row_list.append('|')

            for x in range(0, self.width):
                if (x, y) in characters:
                    row_list.append(characters[(x, y)])
                else:
                    row_list.append(' ')
            row_list.append('|\n')
            return ''.join(row_list)

        map_list = []
        map_list.append('+{}+\n'.format('-' * self.width))
        
        for y in range(0, self.height):
            map_list.append(get_row(y))
        map_list.append('+{}+\n'.format('-'*self.width))
        print(''.join(map_list))
        
