# The code works very well,
# it shows syntaxerror, for a reason that i don't know
# to check the code in github:
# https://github.com/Guedd/Kodland-Python-asic-Eng-for-teachers-1/blob/main/N2.py

class poems:

    def init(self, poem_list):
        self.poem_list = poem_list

    def get_poem(self):
        print("\nThe poem conatins: {lines}, Enjoy it\n: {poem}"
        .format(lines = len(self.poem_list), poem = self.poem_list))
    
    def set_poem(self):
        self.lines = int(input('How many lines will there be?'))
        self.poem_list = list()
        for line in range(self.lines):
            self.enter = str(input('\nEnter the line {}: '.format(line + 1)))
            self.poem_list.append(self.enter)

        self.get_poem()
        self.vowel_num = self.cal("aeiou")
        self.constante_num = self.cal("bcdfgjklmnpqstvxzwyrh")
    
        print('\nNumber of vowels: {}\nNumber of consonants: {}'
       .format(self.vowel_num, self.constante_num))
    
    def cal(self, alph_list):
        self.total = list()
        for sentence in self.poem_list:
            self.nums = sum([*map(sentence.lower().count, alph_list)])
            self.total.append(self.nums)
        
        return sum(self.total)

if __name__ == '__main__':
    test = poems()
    test.set_poem()
