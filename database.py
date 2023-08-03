from random import randrange


class DataBase:
    worldList = list()

    @staticmethod
    def createListOfNouns():
        f = open('russian_nouns.txt', encoding='utf-8')
        for word in f:
            curWord = str(word)[:-1]
            if 5 <= len(curWord) <= 6:
                DataBase.worldList.append(curWord)

    def getWorldList(self):
        DataBase.createListOfNouns()
        return DataBase.worldList

    def getSomeWord(self):
        DataBase.createListOfNouns()
        return DataBase.worldList[randrange(len(DataBase.worldList))]


if __name__ == '__main__':
    db = DataBase()
    print(db.getSomeWord())


