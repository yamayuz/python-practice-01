import getch

KEY_CTRL_C = 3

class Hero:
    def run(self):
        key = 0
        while True:
            # if kbhit(): key = int(getch())
            key = ord(getch.getch())
            if key == KEY_CTRL_C:
                print('bye!!')
                break
            print('key input: ' + str(key))


hero = Hero()
hero.run()