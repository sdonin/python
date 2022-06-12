#функция проведения одного цикла игры от загадывания буквы до отображения доски загаданного слова и виселицы
def hangupman():
    global board, rletters, num_wrong_tries, alphabet_list
    print(board)
    #проверка, есть ли еще неотгаданные буквы в board - не нужна,
    #так как есть в основном цикле программы перед вызовом функции
    letter = 'none'
    #цикл ввода буквы, пока не введем неиспользованную русскую букву
    while letter == 'none':
        letter = input('Угадайте букву:'+'\n')
        if letter in used_letters:
            print(f'Буква {letter} уже использована! Введите другую букву!')
            letter = 'none'
        elif letter not in alphabet_list:
            print(f'{letter} не является буквой русского алфавита! Введите русскую букву!')
            letter = 'none'
    #проверка, правильно ли угадана буква
    num_includes = rletters.count(letter)
    #включение буквы в список использованных букв
    used_letters.append(letter)
    #если число вхождений больше нуля
    if num_includes > 0:
        print('Верно!')
        #замена каждого вхождения правильно угаданной буквы на '$'
        for letter_iteration in range(num_includes):
            letter_index = rletters.index(letter)
            rletters[letter_index] = '$'
            board_list = board.split(' ')
            board_list[letter_index] = letter
            board = ' '.join(board_list)
        #если слово угадано полностью - не осталось неотгаданных букв
        if '_' not in board:
            print('Вы выиграли!')
    else:
        print('Неверно!')
        num_wrong_tries += 1
        print('Число неудачных попыток отгадать = ', num_wrong_tries)
        my_gibbet = gibbet[0:num_wrong_tries]
        for stage in my_gibbet:
            print(stage+'\n')
        #максимальное число строк виселицы - 6
        if num_wrong_tries == 6:
            print('Вы проиграли!')
#старт основного тела программы
#блок инициализации переменных
alphabet_list = ['а', 'б', 'в', 'г', 'д','е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о','п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц', 'ч', 'ш','щ', 'ъ', 'ы', 'ь', 'э','ю', 'я']
num_wrong_tries = 0
gibbet = ['________',
         '|       |',
         '|       O',
         '|      /|\\',
         '|      / \\',
         '|']
used_letters = []
#ввод загадываемого слова
word = 'none'
while word == 'none':
    word = input('Загадайте слово из строчных русских букв:'+'\n')
    for i in range(20):
        print('')
    #формирование списка загаданных букв
    rletters = list(word)
    #проверка каждой буквы загаданного слова на вхождение в алфавит
    for my_letter in rletters:
        if my_letter not in alphabet_list:
            print(f'Введенный символ {my_letter} не является строчной буквой русского алфавита!')
            word = 'none'
#формирование отображаемой доски загаданного слова
word_len = len(word)
board = '_ ' * word_len
#основной цикл игры
#условие число предпринятых неудачных попыток менее максимального и есть неугаданные буквы на доске
while num_wrong_tries < 6 and '_' in board:
    hangupman()
print("Загаданное слово: ", word)