# The fuction works fine
#cyou can check the code on github:
# https://github.com/Guedd/Kodland-Python-asic-Eng-for-teachers-1/blob/main/N3.py


class chess:
    def init(self, first_column, first_row, second_column, second_row):
        self.first_column = first_column
        self.first_row = first_row
        self.second_column = second_column
        self.second_row = second_row

    def get_pos(self):
        print("The current Position is:\nRow number: {}\nColumn number:{}"
        .format(self.first_row, self.first_column))
        print("The next Position is:\nRow number: {}\nColumn number:{}"
        .format(self.second_row, self.second_column))
    
    
    def set_pos(self, fC, fR, sC, sR):
        self.first_column = fC
        self.first_row = fR
        self.second_column = sC
        self.second_row = sR

    def set_pos_man(self):
        self.first_column = int(input('What is the value of the First Column(1-8)?'))
        self.first_row = int(input('What is the value of the First Row(1-8)?'))
        self.second_column = int(input('What is the value of the Second Column(1-8)?'))
        self.second_row = int(input('What is the value of the Second Row(1-8)?'))

    def get_all_pos(self):
        return [self.first_column, self.first_row, self.second_column, self.second_row]

    def quene_move(self):
        if self.value_check():
            if (self.first_row == self.second_row) and (self.first_column != self.second_column):
                return True # verticall move, pass!!

            elif (self.first_row != self.second_row) and (self.first_column == self.second_column):
                return True # horizontal move, pass!!

            if abs(self.first_row - self.second_row) == abs(self.first_column - self.second_column):
                return True # diagonal move, pass!!
 
        return False # move wrong!!

    def value_check(self):
        values = list(map(lambda x: (x > 0) and (x < 9), self.get_all_pos()))
        return True if values else False # one or all the values great then 8 or less then 0


if __name__ == '__main__':
    test = chess()
    ques = input('If you want to test it click on ENTER, or try default by click on another button!!!')
    if ques == "":
        test.set_pos_man()
    else:
        fr, fc = 1, 4
        sr, sc = 5, 8
        test.set_pos(fc, fr, sc, sr)
        test.get_pos()

    if test.quene_move():
        print("Yes")
    else:
        print("No")
