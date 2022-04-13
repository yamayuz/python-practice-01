# フレームワーク
class Calc:
    def __init__(self, operation_list: list):
        self.operation_dict = {}
        for operation_tuple in operation_list:
            (operation, method) = operation_tuple
            self.operation_dict[operation] = method

    def run(self):
        while True:
            print('please input your calculation')
            input_text = input()
            words = input_text.split()
            
            if words[0] == 'exit':
                return
            if len(words) < 3:
                continue
            if words[0] not in self.operation_dict:
                continue

            fun = self.operation_dict[words[0]]
            print(fun(int(words[1]), int(words[2])))