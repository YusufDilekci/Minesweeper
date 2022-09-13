import random


class Mine:
    def __init__(self):
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.design = ' ___ ___ ___\n| 1 | 2 | 3 |\n ___ ___ ___\n| 4 | 5 | 6 |\n ___ ___ ___\n| 7 | 8 | 9 |\n ___ ___ ___'
        self.score = 0

    def place_the_bomb(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        self.matrix[row][column] = '💣'

    def select_number(self, number):
        dic = {1: self.matrix[0][0], 2: self.matrix[0][1], 3: self.matrix[0][2], 4: self.matrix[1][0],
                    5: self.matrix[1][1], 6: self.matrix[1][2],
                    7: self.matrix[2][0], 8: self.matrix[2][1], 9: self.matrix[2][2]}
        new_design = self.design.replace(str(number), dic[number])
        self.design = new_design

    def show_design(self):
        print(self.design)

    def increase_score(self):
        self.score += 1

    def show_score(self):
        print(f'Score: {self.score}')

