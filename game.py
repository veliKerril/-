class Game:
    def __init__(self, word):
        self.word = word
        self.listWord = ['*'] * len(word)
        self.countOfMistakes = 0

    # def startGame(self):
    #     print('Добро пожаловать в игру Виселица!')
    # def endGame(self):
    #     print('Спасибо за игру!')

    def curWord(self):
        print('Текущее состояние:')
        print(''.join(self.listWord))
        print(f'Количество ошибок: {self.countOfMistakes}')

    def question(self):
        answer = input('Буква? ')
        for i in range(len(self.word)):
            if self.word[i] == answer:
                self.listWord[i] = answer
        if answer not in self.word:
            self.countOfMistakes += 1

    def win(self):
        if '*' in self.listWord:
            return False
        else:
            return True