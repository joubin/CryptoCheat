import sys, os, gzip, re

class MakeWordList():
    """
    Given a path to a wordlist, make a small and portable dictionary and save it in the extras folder.

    I got my list from []
    """
    def __init__(self, path):
        self.path = path
        self.rawData = None
        self.writePath = os.path.dirname(os.getcwd())
        print os.sep
        self.extras = self.writePath+ os.sep + 'extras'
        if not os.path.exists(self.extras):
            os.makedirs(self.extras)
        self.__read()
        self.__makeZip()


    def __read(self):
        with open(self.path) as rawFile:
            self.rawData = rawFile.read().split(',')

        for i in range(len(self.rawData)):
            self.rawData[i] = self.rawData[i].split('\r\n')

        self.rawData =  [item for sublist in self.rawData for item in sublist]
       
        for i in range(len(self.rawData)):
            self.rawData[i] = self.rawData[i].split(' ')

        self.rawData =  [item for sublist in self.rawData for item in sublist]

        self.rawData = list(set(self.rawData))



    def __makeZip(self):
        with gzip.open(self.extras+ os.sep + 'words.gzip', 'w') as zipFile:
            zipFile.write(str(self.rawData))



if __name__ == "__main__":
    path = raw_input('Print provide a path to your world list: ').strip()
    go = MakeWordList(path)

