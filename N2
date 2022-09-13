def poem():
    
    lines = int(input('How many lines will there be?'))
    poem_list = list()

    for line in range(lines):
        enter = str(input(f'\nEnter the line {line}: '))
        poem_list.append(enter)
    
    vowel_num = cal(poem_list, "aeiou")
    constante_num = cal(poem_list, "bcdfgjklmnpqstvxzwyrh")
    
    print('\nNumber of vowels: {}\nNumber of consonants: {}'
    .format(vowel_num, constante_num))
    
def cal(str_list, alph_list) -> int:
    total = list()
    for sentence in str_list:
        nums = sum([*map(sentence.lower().count, alph_list)])
        total.append(nums)
        
    return sum(total)

if __name__ == '__main__':
    poem()
