import random

class Game:
    def __init__(self):
        self.board_list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
        ]
        self.score = 0
        #判断空位 坐标 行列
        self.board_empty = []
    def start(self):
        self.restart()
        while True:
            self.print_board()
            code = input('请输入指令>>>>')
            if code == 'w':
                self.move_up()
            elif code == 'a':
                self.move_left()
            elif code == 's':
                self.move_down()
            elif code == 'd':
                self.move_right()
            elif code == 'r':
                self.restart()
                continue
            elif code == 'q':
                exit('退出')
            else :
                print('你的输入有误,请重新输入')
                continue
            if self.is_win():
                # 判断游戏是否win
                print('you win')
                break
            if self.gameOver():
                # 判断是否game over
                print('geme over')
                break
            self.add_piece()
            # 在空白地方随机添加2或者4

    # 打印棋盘
    def print_board(self):
        print("""
score:{}
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
|{:^5}+{:^5}+{:^5}+{:^5}+
+-----+-----+-----+-----+
w(up), s(down), a(left), d(right)
q(quit), r(restart)
""".format(self.score, *self.board_list[0],
           *self.board_list[1],
           *self.board_list[2],
           *self.board_list[3]))

    def is_win(self):
        # 判断游戏是否win
        #判断空位
        self.board_empty = []
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                if self.board_list[i][j] == 2048:
                    return True
                if self.board_list[i][j] == '':
                    self.board_empty.append((i, j))
        return False
    def gameOver(self):
        #判断游戏是否game over
        if not self.board_empty:
            #判断每行每列没有相邻的相等的元素
            #判断每一行
            for i in range(len(self.board_list)):
                for j in  range(len(self.board_list[i])-1):
                    if self.board_list[i][j] == self.board_list[i][j+1]:
                        return  False
            self.turn_right()
            for i in range(len(self.board_list)):
                for j in  range(len(self.board_list[i])-1):
                    if self.board_list[i][j] == self.board_list[i][j+1]:
                        self.turn_left()
                        return  False
            return True
        return  False
    def add_piece(self):
        #在空白的位置添加棋子(2, 4)
        #先随机位置，再随机数字
        if self.board_empty:
            p = self.board_empty.pop(random.randrange(len(self.board_empty)))
            self.board_list[p[0]][p[1]] = random.randrange(2, 5, 2)

    def restart(self):
        #初始化棋盘
        self.board_list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
        ]
        #随机两个位置
        while True:
            t1 = (random.randrange(len(self.board_list)), random.randrange(len(self.board_list[0])))
            t2 = (random.randrange(len(self.board_list)), random.randrange(len(self.board_list[0])))
            if t1 != t2:
                break
        #随机两个值
        self.board_list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
        self.board_list[t2[0]][t2[1]] = random.randrange(2, 5, 2)

    def move_up(self):
        self.turn_left()
        self.move_left()
        self.turn_right()

    def move_left(self):
        for i in range(len(self.board_list)):
            self.board_list[i] = self.row_left_oper(self.board_list[i])
    def move_down(self):
        self.turn_right()
        self.move_left()
        self.turn_left()

    def move_right(self):
        self.turn_left()
        self.move_up()
        self.turn_right()

    def row_left_oper(self, row):

        # l1 = [2, 4, 2, 4]  # =>[2, 2]=>[4]  =>[4,'','','']
        # 先挤到一起
        temp = []
        for item in row:
            if item != '':
                temp.append(item)
        new_row = []
        # 合并同类项
        flag = True

        for i in range(len(temp)):
            if flag:
                if i + 1 < len(temp) and temp[i] == temp[i + 1]:
                    new_row.append(temp[i] * 2)
                    flag = False
                else:
                    new_row.append(temp[i])
            else:
                flag = True
        # 补齐
        n = len(row)
        for i in range(n - len(new_row)):
            new_row.append('')
        return new_row

    def turn_right(self):
        self.board_list = [list(x[::-1]) for x in zip(*self.board_list)]

    def turn_left(self):
        for i in range(3):
            self.turn_right()


if __name__ == '__main__':
    game = Game()
    game.start()












