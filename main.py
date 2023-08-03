from game import Game
from draw import Draw
from database import DataBase

draw = Draw()
database = DataBase()

print('Добро пожаловать в игру!')
while True:
    s = input('Вы хотите сыграть в игру? д/н ')
    if s == 'д':
        word = database.getSomeWord()
        game = Game(word)
        while game.countOfMistakes <= 6:
            draw.drawGallows(game.countOfMistakes)
            game.curWord()
            game.question()
            if game.win():
                print('Ура! Вы выиграли!')
                break
            if game.countOfMistakes == 6:
                draw.drawGallows(game.countOfMistakes)
                print(f'Загаданное слово: {word}')
                print('Игра закончена!')
                break
    elif s == 'н':
        print('До скорых встреч!')
        break
    else:
        print('Попробуйте еще раз ввести \'д\' или \'н\'')
