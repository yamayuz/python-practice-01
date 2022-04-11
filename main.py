
class Score:
    def __init__(self):
        self.name = 'Unknown'
        self.math = 0
        self.english = 0
        self.japanese = 0

    def get_average(self):
        return (self.math + self.english + self.japanese) / 3


if __name__ == "__main__":
    taro = Score()
    taro.name = 'taro'
    taro.math = 60
    taro.english = 70
    taro.japanese = 80

    ave = taro.get_average()
    print(ave) 